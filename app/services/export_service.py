"""
匯出服務模組
處理資料匯出相關的業務邏輯
"""
import os
import pandas as pd
from app.models.order import Order

class ExportService:
    """
    匯出服務類別
    處理統計資料匯出相關的功能
    """
    
    def export_to_csv(self, form_id):
        """
        將訂單統計資料匯出為 CSV 檔案
        
        參數:
            form_id: 表單編號
            
        回傳:
            str: CSV 檔案路徑
        """
        # 取得訂單資料
        orders = Order.query.filter_by(form_id=form_id).all()
        
        # 準備資料
        data = []
        for order in orders:
            data.append({
                '食物名稱': order.food.name,
                '訂購者': order.user_name,
                '數量': order.quantity,
                '單價': order.food.price,
                '總價': order.quantity * order.food.price,
                '訂購時間': order.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        
        # 建立 DataFrame
        df = pd.DataFrame(data)
        
        # 建立暫存目錄（如果不存在）
        temp_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'instance', 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        
        # 儲存為 CSV
        file_path = os.path.join(temp_dir, f'order_statistics_{form_id}.csv')
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        
        return file_path