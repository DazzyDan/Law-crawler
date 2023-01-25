# Law case crawler | 法律案例爬虫

-   [简体中文](README.zh-CN.md)

案件爬虫是一个从三大搜索引擎（百度、搜狗和微信）和两个案件搜索网站（武松和巴手）抓取、抓取和可视化案件的项目。它与 Selenium grid docker、Flask 和 gunicorn 一起执行。这是第一个版本。在下一个版本中，它将实现并行处理并将获取的数据存储在数据库中以加速处理并最大限度地减少缓存。

## 结构

<img width="981" alt="image" src="https://user-images.githubusercontent.com/73490814/214577434-349674c2-eac8-4f93-9e51-dd609273c757.png">

## 截图

### 主页

1.  搜索引擎<img width="1356" alt="image" src="https://user-images.githubusercontent.com/73490814/214578514-23a388bb-84a2-4b76-ad9b-c2a80eb5f800.png">

可以选择三个搜索引擎。![0 0 0 0_5000\_ (3)](https://user-images.githubusercontent.com/73490814/214579469-29272eee-4b23-4e2b-b7d0-456f35757164.png)

2.  箱网![0 0 0 0_5000\_ (1)](https://user-images.githubusercontent.com/73490814/214578873-102ca7dc-d1eb-4b63-80ae-44840b914c9b.png)

它能够选择不同类型的案例。![0 0 0 0_5000\_ (2)](https://user-images.githubusercontent.com/73490814/214579157-7df4cf7b-7c25-47e2-90c1-e22a1e336a05.png)

### 结果页面

gridjs是用来实现table的。 Grid.js 是一个免费的开源 JavaScript 表格插件。它可以实现这些功能：搜索关键词，排序。

1.  搜索引擎的结果![0 0 0 0_5000_search-web](https://user-images.githubusercontent.com/73490814/214580092-96316127-042a-481b-8517-1923099f7ade.png)
2.  案例网的结果<img width="1354" alt="image" src="https://user-images.githubusercontent.com/73490814/214585512-d7f1d19e-8f06-4fbd-b746-4aab39af825e.png">

![0 0 0 0_5000_search-case](https://user-images.githubusercontent.com/73490814/214585639-69165daf-0900-4cec-9c06-d93fd0e29eb5.png)

Click on "Show more": 
<img width="1361" alt="image" src="https://user-images.githubusercontent.com/73490814/214585922-06f21a67-8195-453c-8f75-a4c33381f439.png">

将显示有关此案例的更多详细信息。

## 如何安装和运行项目

首先，您可以从 docker hub 中拉取该镜像。

```bash
docker pull dazzydan/law_crawler:1.0
```

然后，运行这个图像

```bash
docker-compose up -d
```

## 如何使用该项目

门户页面：[HTTP://0.0.0.0:5000/](http://0.0.0.0:5000/)

Selenium网格处理页面：[HTTP://127.0.0.1:4444/](http://127.0.0.1:4444/)

如果您想发现在爬行过程中发生了什么，可以连接到 VNC 查看器。：[HTTP://127.0.0.1:6900/](http://127.0.0.1:6900/)

## 未来改进

1.  平行游行
2.  数据库
