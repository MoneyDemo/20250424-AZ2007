"""
訂單模型模組
定義訂單相關的資料庫模型
"""
from datetime import datetime
from app import db

class Order(db.Model):
    """
    訂單模型類別
    
    屬性:
        id: 主鍵
        form_id: 表單編號
        food_id: 食物編號 (外鍵)
        user_name: 訂購者姓名
        quantity: 數量
        created_at: 建立時間
    """
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer, nullable=False, index=True)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """
        將模型轉換為字典格式
        
        回傳:
            dict: 訂單資訊字典
        """
        return {
            'id': self.id,
            'form_id': self.form_id,
            'food_id': self.food_id,
            'user_name': self.user_name,
            'quantity': self.quantity,
            'created_at': self.created_at.isoformat(),
            'food': self.food.to_dict() if self.food else None
        }