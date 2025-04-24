"""
設定檔案，用於存放應用程式的所有設定
"""
import os
from datetime import timedelta

# 取得目前檔案所在的目錄路徑
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    基本設定類別
    
    屬性:
        SECRET_KEY: 用於加密的金鑰
        SQLALCHEMY_DATABASE_URI: 資料庫連線字串
        SQLALCHEMY_TRACK_MODIFICATIONS: 是否追蹤資料庫修改
    """
    # 設定 Flask 的密鑰
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-for-afternoon-tea'
    
    # 設定 SQLite 資料庫路徑
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'afternoon_tea.db')
    
    # 關閉 SQLAlchemy 的修改追蹤功能以提升效能
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    開發環境設定
    """
    DEBUG = True

class TestingConfig(Config):
    """
    測試環境設定
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'test.db')

class ProductionConfig(Config):
    """
    生產環境設定
    """
    pass

# 設定配置字典
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}