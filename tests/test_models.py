"""
模型測試
測試資料模型的功能
"""
import pytest
from app.models.food import Food
from app.models.order import Order
from app import db

def test_create_food(app):
    """測試建立食物項目"""
    with app.app_context():
        # 建立測試食物
        food = Food(name='測試食物', description='這是測試用的食物', price=100)
        db.session.add(food)
        db.session.commit()
        
        # 檢查食物是否正確儲存
        saved_food = Food.query.first()
        assert saved_food.name == '測試食物'
        assert saved_food.price == 100

def test_create_order(app):
    """測試建立訂單"""
    with app.app_context():
        # 建立測試食物
        food = Food(name='測試食物', description='這是測試用的食物', price=100)
        db.session.add(food)
        db.session.commit()
        
        # 建立測試訂單
        order = Order(
            form_id=1,
            food_id=food.id,
            user_name='測試使用者',
            quantity=2
        )
        db.session.add(order)
        db.session.commit()
        
        # 檢查訂單是否正確儲存
        saved_order = Order.query.first()
        assert saved_order.user_name == '測試使用者'
        assert saved_order.quantity == 2
        assert saved_order.food.name == '測試食物'

def test_food_to_dict(app):
    """測試食物轉換為字典格式"""
    with app.app_context():
        # 建立測試食物
        food = Food(name='測試食物', description='這是測試用的食物', price=100)
        db.session.add(food)
        db.session.commit()
        
        # 轉換為字典
        food_dict = food.to_dict()
        
        # 檢查轉換結果
        assert food_dict['name'] == '測試食物'
        assert food_dict['price'] == 100
        assert 'id' in food_dict
        assert 'created_at' in food_dict

def test_order_to_dict(app):
    """測試訂單轉換為字典格式"""
    with app.app_context():
        # 建立測試食物
        food = Food(name='測試食物', description='這是測試用的食物', price=100)
        db.session.add(food)
        db.session.commit()
        
        # 建立測試訂單
        order = Order(
            form_id=1,
            food_id=food.id,
            user_name='測試使用者',
            quantity=2
        )
        db.session.add(order)
        db.session.commit()
        
        # 轉換為字典
        order_dict = order.to_dict()
        
        # 檢查轉換結果
        assert order_dict['user_name'] == '測試使用者'
        assert order_dict['quantity'] == 2
        assert order_dict['food']['name'] == '測試食物'
        assert 'id' in order_dict
        assert 'created_at' in order_dict