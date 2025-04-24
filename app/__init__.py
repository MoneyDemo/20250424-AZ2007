"""
Flask 應用程式初始化模組
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

# 初始化資料庫物件
db = SQLAlchemy()
migrate = Migrate()

def multiply(a, b):
    """自定義的乘法過濾器"""
    return float(a) * float(b)

def create_app(config_name):
    """
    建立應用程式實例
    
    參數:
        config_name: 設定名稱（development、testing、production）
        
    回傳:
        app: Flask 應用程式實例
    """
    # 建立 Flask 應用程式
    app = Flask(__name__)
    
    # 載入設定
    app.config.from_object(config[config_name])
    
    # 初始化資料庫
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 註冊過濾器
    app.jinja_env.filters['multiply'] = multiply
    
    # 註冊藍圖
    from app.controllers.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app