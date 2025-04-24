# 下午茶訂餐統計系統

這是一個簡單的下午茶訂餐統計系統，可以幫助團隊管理下午茶的訂購。

## 功能特色

- 不需要登入，即可快速使用
- 建立訂餐表單
- 新增多個餐點選項
- 即時統計訂購狀況
- 匯出訂購統計報表（CSV 格式）
- 美觀的使用者介面
- 動畫效果增加使用趣味性

## 系統需求

- Python 3.11.9 或以上版本
- Windows 11 作業系統
- 現代化網頁瀏覽器（支援 HTML5 和 CSS3）

## 安裝說明

1. 建立虛擬環境：
   ```bash
   python -m venv .eatenv
   ```

2. 啟動虛擬環境：
   ```bash
   .eatenv\Scripts\activate
   ```

3. 安裝相依套件：
   ```bash
   pip install -r requirements.txt
   ```

4. 初始化資料庫：
   ```bash
   flask db upgrade
   ```

5. 啟動應用程式：
   ```bash
   python run.py
   ```

## 使用說明

1. 開啟瀏覽器，前往 http://localhost:5000
2. 在首頁建立新的訂餐表單
3. 新增餐點選項
4. 分享訂餐表單連結給團隊成員
5. 在統計頁面查看訂購狀況
6. 需要時可以匯出 CSV 報表

## 測試

執行單元測試：
```bash
pytest
```

執行涵蓋率測試：
```bash
pytest --cov=app tests/
```

## 專案結構

```
afternoon_tea_order/
├── app/                    # 應用程式主要程式碼
│   ├── models/            # 資料模型
│   ├── controllers/       # 控制器
│   ├── services/          # 服務層
│   ├── static/           # 靜態檔案
│   └── templates/        # HTML 樣板
├── instance/              # 資料庫檔案
├── migrations/           # 資料庫遷移檔案
├── tests/                # 測試程式碼
├── config.py            # 設定檔
├── requirements.txt     # 相依套件清單
└── run.py              # 應用程式進入點
```

## 開發說明

- 使用 Flask 作為後端框架
- 使用 SQLite 作為資料庫
- 使用 Bootstrap 5 作為前端框架
- 使用 Font Awesome 提供圖示
- 所有 API 端點都有適當的註解說明
- 遵循 PEP 8 程式碼風格指南

## 更新記錄

詳見 [CHANGELOG.md](CHANGELOG.md)

## 授權資訊

本專案採用 MIT 授權。