"""
服務層測試
測試服務層的業務邏輯
"""
import pytest
from app.services.order_service import OrderService
from app.services.export_service import ExportService
from app.models.food import Food
from app.models.order import Order
from app import db
import os

@pytest.fixture
def order_service():
    """建立訂單服務實例"""
    return OrderService()

@pytest.fixture
def export_service():
    """建立匯出服務實例"""
    return ExportService()

def test_add_order(app, order_service):
    """測試新增訂單功能"""
    with app.app_context():
        # 建立測試食物
        food = Food(name='測試食物', price=100)
        db.session.add(food)
        db.session.commit()
        
        # 新增訂單
        order_data = {
            'food_id': food.id,
            'user_name': '測試使用者',
            'quantity': 2
        }
        result = order_service.add_order(1, order_data)
        
        # 檢查結果
        assert result['user_name'] == '測試使用者'
        assert result['quantity'] == 2
        assert result['food']['name'] == '測試食物'

def test_get_statistics(app, order_service):
    """測試取得統計資料功能"""
    with app.app_context():
        # 建立測試食物
        food = Food(name='測試食物', price=100)
        db.session.add(food)
        db.session.commit()
        
        # 建立多筆訂單
        orders = [
            Order(form_id=1, food_id=food.id, user_name='使用者A', quantity=2),
            Order(form_id=1, food_id=food.id, user_name='使用者B', quantity=1)
        ]
        db.session.add_all(orders)
        db.session.commit()
        
        # 取得統計資料
        stats = order_service.get_statistics(1)
        
        # 檢查統計結果
        assert len(stats) == 1
        assert stats[0]['total_quantity'] == 3
        assert stats[0]['user_count'] == 2
        assert len(stats[0]['users']) == 2

def test_export_to_csv(app, export_service):
    """測試匯出 CSV 功能"""
    with app.app_context():
        # 建立測試資料
        food = Food(name='測試食物', price=100)
        db.session.add(food)
        db.session.commit()
        
        order = Order(form_id=1, food_id=food.id, user_name='測試使用者', quantity=2)
        db.session.add(order)
        db.session.commit()
        
        # 匯出 CSV
        file_path = export_service.export_to_csv(1)
        
        # 檢查檔案是否存在
        assert os.path.exists(file_path)
        
        # 檢查檔案內容
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
            assert '測試食物' in content
            assert '測試使用者' in content
            assert '2' in content
        
        # 清理檔案
        os.remove(file_path)