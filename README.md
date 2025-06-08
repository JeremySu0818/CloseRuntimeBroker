English Version
# CloseRuntimeBroker

**CloseRuntimeBroker** is a lightweight Windows tool designed to safely terminate `RuntimeBroker.exe` when it causes UI lag, file lockups, or high CPU usage.  
The tool is intended for **manual use** — no background activity or automation is involved.

---

## 🧩 Features

- Lists all active `RuntimeBroker.exe` processes
- Allows one-click manual termination of all relevant instances
- Helps resolve issues such as:
  - File explorer hangs (e.g. opening PDFs, images, or media)
  - System settings interface becomes unresponsive
  - General UI lag or window dragging delays
  - High CPU usage or locked file handles by RuntimeBroker

---

## 🛠 How to Use

1. Run `CloseRuntimeBroker.exe` as **Administrator**
2. The tool will detect and terminate all matching RuntimeBroker processes
3. The window will close automatically once completed

---

## ⚠️ Notes

- Use only when RuntimeBroker is confirmed to cause system issues
- Some apps may need to be reopened after termination
- This is a single-use tool with no background tasks, no networking, and no auto-run

---

## 📁 File List

| Filename                | Description                              |
|------------------------|------------------------------------------|
| `CloseRuntimeBroker.exe` | Main executable (requires admin rights) |
| `close_runtimebroker.py` | Python source code (for verification or custom build) |
| `README.md`             | This documentation file                 |

---

## 🔒 Security Statement

This tool is compiled with PyInstaller and does **not** include any networking, backdoors, or malicious behavior.  
You may verify by reviewing or running the `.py` script directly.

---

## 🧑‍💻 Author

Maintained by [@jeremysu0818](https://github.com/jeremysu0818).  
Feel free to open an issue for bug reports or suggestions.


中文版
# CloseRuntimeBroker
**CloseRuntimeBroker** 是一款輕量級的 Windows 工具，用於安全終止 `RuntimeBroker.exe`，當它導致 UI 延遲、占用檔案或高 CPU 使用時。  
本工具設計為**手動操作**，不包含背景常駐行為，也不具備任何自動化功能，適合進階使用者在特定情況下快速排除問題。

---

## 🧩 工具特色

- 顯示所有執行中的 `RuntimeBroker.exe` 處理程序
- 一鍵手動終止所有相關程序
- 解決以下常見問題：
  - 開啟檔案（PDF、圖片、影片）時無回應
  - 系統設定畫面卡頓或按鈕無反應
  - UI 整體延遲、視窗拖曳延後
  - `RuntimeBroker.exe` 長時間佔用 CPU、鎖住檔案資源

---

## 🛠 使用方式

1. 以 **系統管理員身份** 執行 `CloseRuntimeBroker.exe`
2. 程式將列出並終止所有相關的 RuntimeBroker 處理程序
3. 執行結束後會自動關閉視窗

---

## ⚠️ 注意事項

- 僅在確認 `RuntimeBroker` 導致系統異常時使用
- 關閉處理程序後，部分應用程式可能需重新開啟
- 本工具不會常駐、不會連網、不會自動執行

---

## 📁 檔案清單

| 檔案名稱               | 說明                               |
|------------------------|------------------------------------|
| `CloseRuntimeBroker.exe` | 主程式，需以管理員執行               |
| `close_runtimebroker.py` | 原始 Python 程式碼，供技術參考或自行編譯 |
| `README.md`             | 本說明文件                           |

---

## 🔒 安全與開源聲明

本工具使用 PyInstaller 打包，不含任何網路連線、後門或惡意邏輯。  
如有疑慮，歡迎參考原始碼自行驗證或手動執行 `.py` 腳本。

---

## 🧑‍💻 製作與維護

製作人：[@jeremysu0818](https://github.com/jeremysu0818)  
歡迎提交錯誤回報或功能建議。


