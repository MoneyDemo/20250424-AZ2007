"""
測試設定檔案
提供測試所需的 fixtures
"""
import os
import tempfile
import pytest
from app import create_app, db

@pytest.fixture
def app():
    """建立測試用的應用程式實例"""
    # 建立臨時資料庫檔案
    db_fd, db_path = tempfile.mkstemp()
    
    # 建立測試用的應用程式
    app = create_app('testing')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    
    # 建立資料庫結構
    with app.app_context():
        db.create_all()
    
    yield app
    
    # 清理
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """建立測試用的客戶端"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """建立測試用的 CLI runner"""
    return app.test_cli_runner()