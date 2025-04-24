"""
訂單服務模組
處理訂單相關的業務邏輯
"""
from app import db
from app.models.food import Food
from app.models.order import Order

class OrderService:
    """
    訂單服務類別
    處理訂單相關的所有業務邏輯
    """
    
    def get_foods(self):
        """
        取得所有食物列表
        
        回傳:
            list: 食物列表
        """
        return Food.query.all()
    
    def add_order(self, form_id, data):
        """
        新增訂單
        
        參數:
            form_id: 表單編號
            data: 訂單資料
        
        回傳:
            dict: 訂單資訊
        """
        order = Order(
            form_id=form_id,
            food_id=data['food_id'],
            user_name=data['user_name'],
            quantity=data.get('quantity', 1)
        )
        db.session.add(order)
        db.session.commit()
        return order.to_dict()
    
    def get_statistics(self, form_id):
        """
        取得統計資料
        
        參數:
            form_id: 表單編號
        
        回傳:
            dict: 統計資料
        """
        # 取得該表單所有訂單
        orders = Order.query.filter_by(form_id=form_id).all()
        
        # 計算統計資料
        stats = {}
        for order in orders:
            food_id = order.food_id
            if food_id not in stats:
                stats[food_id] = {
                    'food': order.food.to_dict(),
                    'total_quantity': 0,
                    'users': set()
                }
            stats[food_id]['total_quantity'] += order.quantity
            stats[food_id]['users'].add(order.user_name)
        
        # 轉換為列表格式
        result = []
        for food_stats in stats.values():
            result.append({
                'food': food_stats['food'],
                'total_quantity': food_stats['total_quantity'],
                'user_count': len(food_stats['users']),
                'users': list(food_stats['users'])
            })
        
        return result