"""
應用程式進入點
用於啟動 Flask 應用程式
"""
import os
from app import create_app
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 從環境變數取得設定，預設為開發環境
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)