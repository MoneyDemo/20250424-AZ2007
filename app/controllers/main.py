"""
主要控制器模組
處理路由和請求響應
"""
from flask import Blueprint, render_template, request, jsonify, send_file, redirect, url_for
from app.services.order_service import OrderService
from app.services.export_service import ExportService
from app import db
from app.models.food import Food
from datetime import datetime

# 建立藍圖
main = Blueprint('main', __name__)

# 注入服務
order_service = OrderService()
export_service = ExportService()

@main.route('/')
def index():
    """首頁路由"""
    return render_template('index.html', now=datetime.now())

@main.route('/form', methods=['POST'])
def create_form():
    """建立訂餐表單"""
    data = request.form
    title = data.get('title')
    description = data.get('description')
    foods_data = []
    
    # 處理動態的食物資料
    i = 0
    while f'foods[{i}][name]' in data:
        name = data.get(f'foods[{i}][name]')
        price = float(data.get(f'foods[{i}][price]', 0))
        if name and price > 0:
            food = Food(name=name, description='', price=price)
            db.session.add(food)
            foods_data.append(food)
        i += 1
    
    db.session.commit()
    
    # 取得第一個食物的 ID 作為表單 ID
    form_id = foods_data[0].id if foods_data else None
    
    if form_id:
        return redirect(url_for('main.order_form', form_id=form_id))
    return redirect(url_for('main.index'))

@main.route('/order/<int:form_id>')
def order_form(form_id):
    """
    訂餐表單頁面
    
    參數:
        form_id: 表單編號
    """
    # 取得相關的食物列表
    foods = Food.query.filter(Food.id >= form_id).all()
    if not foods:
        return redirect(url_for('main.index'))
    
    # 取得統計資料
    statistics = order_service.get_statistics(form_id)
    
    # 建立表單資料
    form = {
        'id': form_id,
        'title': f'訂餐表單 #{form_id}',
        'description': '請點選下方餐點進行訂購'
    }
    
    return render_template('order_form.html',
                         form=form,
                         foods=foods,
                         statistics=statistics,
                         now=datetime.now())

@main.route('/order/<int:form_id>/add', methods=['POST'])
def add_order(form_id):
    """
    新增訂單
    
    參數:
        form_id: 表單編號
    """
    data = request.get_json()
    result = order_service.add_order(form_id, data)
    return jsonify(result)

@main.route('/statistics/<int:form_id>')
def statistics(form_id):
    """
    統計頁面
    
    參數:
        form_id: 表單編號
    """
    stats = order_service.get_statistics(form_id)
    
    # 準備圓餅圖資料
    food_names = [stat['food']['name'] for stat in stats]
    food_amounts = [stat['total_quantity'] * stat['food']['price'] for stat in stats]
    
    return render_template('statistics.html', 
                         stats=stats,
                         form_id=form_id,
                         food_names=food_names,
                         food_amounts=food_amounts,
                         now=datetime.now())

@main.route('/statistics/<int:form_id>/export')
def export_statistics(form_id):
    """
    匯出統計資料
    
    參數:
        form_id: 表單編號
    """
    file_path = export_service.export_to_csv(form_id)
    return send_file(
        file_path,
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'order_statistics_{form_id}.csv'
    )

@main.context_processor
def utility_processor():
    """提供模板使用的公用函數"""
    return {
        'now': datetime.now()
    }