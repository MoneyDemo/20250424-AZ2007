"""
食物模型模組
定義食物相關的資料庫模型
"""
from datetime import datetime
from app import db

class Food(db.Model):
    """
    食物模型類別
    
    屬性:
        id: 主鍵
        name: 食物名稱
        description: 食物描述
        price: 價格
        created_at: 建立時間
    """
    __tablename__ = 'foods'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 關聯到訂單
    orders = db.relationship('Order', backref='food', lazy=True)
    
    def to_dict(self):
        """
        將模型轉換為字典格式
        
        回傳:
            dict: 食物資訊字典
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'created_at': self.created_at.isoformat()
        }