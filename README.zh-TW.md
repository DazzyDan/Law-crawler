# Law case crawler | 法律案例爬虫

-   [簡體中文](README.zh-CN.md)

案件爬蟲是一個從三大搜索引擎（百度、搜狗和微信）和兩個案件搜索網站（武松和巴手）抓取、抓取和可視化案件的項目。它與 Selenium grid docker、Flask 和 gunicorn 一起執行。這是第一個版本。在下一個版本中，它將實現並行處理並將獲取的數據存儲在數據庫中以加速處理並最大限度地減少緩存。

## 結構

<img width="981" alt="image" src="https://user-images.githubusercontent.com/73490814/214577434-349674c2-eac8-4f93-9e51-dd609273c757.png">

## 截圖

### 主頁

1.  搜索引擎<img width="1356" alt="image" src="https://user-images.githubusercontent.com/73490814/214578514-23a388bb-84a2-4b76-ad9b-c2a80eb5f800.png">

可以選擇三個搜索引擎。![0 0 0 0_5000\_ (3)](https://user-images.githubusercontent.com/73490814/214579469-29272eee-4b23-4e2b-b7d0-456f35757164.png)

2.  箱網![0 0 0 0_5000\_ (1)](https://user-images.githubusercontent.com/73490814/214578873-102ca7dc-d1eb-4b63-80ae-44840b914c9b.png)

它能夠選擇不同類型的案例。![0 0 0 0_5000\_ (2)](https://user-images.githubusercontent.com/73490814/214579157-7df4cf7b-7c25-47e2-90c1-e22a1e336a05.png)

### 結果頁面

gridjs是用來實現table的。 Grid.js 是一個免費的開源 JavaScript 表格插件。它可以實現這些功能：搜索關鍵詞，排序。

1.  搜索引擎的結果![0 0 0 0_5000_search-web](https://user-images.githubusercontent.com/73490814/214580092-96316127-042a-481b-8517-1923099f7ade.png)
2.  案例網的結果<img width="1354" alt="image" src="https://user-images.githubusercontent.com/73490814/214585512-d7f1d19e-8f06-4fbd-b746-4aab39af825e.png">

![0 0 0 0_5000_search-case](https://user-images.githubusercontent.com/73490814/214585639-69165daf-0900-4cec-9c06-d93fd0e29eb5.png)

點擊“顯示更多”：<img width="1361" alt="image" src="https://user-images.githubusercontent.com/73490814/214585922-06f21a67-8195-453c-8f75-a4c33381f439.png">

將顯示有關此案例的更多詳細信息。

## 如何安裝和運行項目

首先，您可以從 docker hub 中拉取該鏡像。

```bash
docker pull dazzydan/law_crawler:1.0
```

然後，運行這個圖像

```bash
docker-compose up -d
```

## 如何使用該項目

門戶頁面：<http://0.0.0.0:5000/>

Selenium網格處理頁面：<http://127.0.0.1:4444/>

如果您想發現在爬行過程中發生了什麼，可以連接到 VNC 查看器。：<http://127.0.0.1:6900/>

## 未來改進

1.  平行遊行
2.  數據庫
