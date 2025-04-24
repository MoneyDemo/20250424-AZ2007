幫我使用 Python 建立一個 WEB 用來做下午茶訂餐統計系統。
 
這個 WEB 需要有以下功能：
1. 不需要使用者登入
2. 首頁: 使用者可以建立下午茶訂餐的表單
  - 使用者可以選擇訂餐的餐點
3. 訂餐表單頁面: 使用者可以在這個頁面選擇不同的餐點 +1 的按鈕來增加訂餐的數量
  - 每次 +1 都需要輸入使用者的姓名
4. 統計頁面: 使用者可以看到所有人的訂餐統計
  - 統計頁面會顯示每個餐點的訂餐數量
  - 統計頁面會顯示每個餐點的訂餐人數
  - 統計頁面會顯示每個餐點的訂餐人數的姓名
5. 使用者可以在統計頁面下載訂餐的統計報表，使用 CSV 格式

系統的網站架構與設計應該要有:
- OS 是 Windows 11- 要使用 python 的虛擬環境來開發。
  - 虛擬環境的名稱為 .eatenv
- 使用 Python 3.11.9 以上的版本。
- 使用 Flask 作為後端框架。
- 資料儲存在 SQLite 資料庫中。
- 提供 README.md 檔案，說明如何啟動網站等常見 README 內容。
  - 要包含如何執行各種不同的測試。
- 程式碼必須包含適當的註解。
  - 所有的 Class 與 Method 一定要有註解
  - 所有的變數與參數一定要有註解
  - 適當地為所有程式碼加入註解
  - 符合 Clean Code 的原則
- 程式碼必須包含適當的單元測試。
  - 測試框架要使用 pytest
  - 測試只針對邏輯部分，前端、服務層、Controller 不需要測試。
- 使用 Bootstrap 5 來設計網站。
  - 使用 fontawesome 來提供 ICON。
  - 畫面要華麗
  - 可以加入一些動畫效果。
  - 畫面的整體色調要很色彩繽紛
- 使用 cloudflare CDN 來載入 Bootstrap 5 與 fontawesome。
  - 若有任何其他前段需要的 library 也要使用 jsdeliver CDN。

其他要求:
- Update relevant documentation in /docs when modifying features
- Keep README.md in sync with new capabilities
- Maintain changelog entries in CHANGELOG.md
- 所有回復請務必使用繁體中文
- 分階段實作，先產生計畫，並在 Github: https://github.com/lettucebo/20250422-AZ2007/ 上面新增 issue 來追蹤進度，每完成一步驟就加入 comment 補充說明
  - When creating issue, remember to add corresponding labels
  - note: remember always update the issue and add issue comment everytime when completing a task/step

先不要執行，請先產出一個執行計畫與檔案文件目錄結構給我看