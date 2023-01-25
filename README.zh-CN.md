# 法律案件爬虫
- [English](README.md)

法律案件爬虫是一个从三大搜索引擎（百度、搜狗和微信）和两个案件搜索网站（无讼案例和把手案例）爬取、可视化案件的项目。这个项目使用Selenium grid docker、Flask 和 gunicorn。这是第一个版本。在下一个版本中，它将实现并行处理并将获取的数据存储在数据库中以加速处理并最大限度地减少缓存。

## 结构

<img width="981" alt="image" src="https://user-images.githubusercontent.com/73490814/214577434-349674c2-eac8-4f93-9e51-dd609273c757.png">

## 截图

### 主页

1.  搜索引擎<img width="1356" alt="image" src="https://user-images.githubusercontent.com/73490814/214578514-23a388bb-84a2-4b76-ad9b-c2a80eb5f800.png">

可以选择三个搜索引擎。![0 0 0 0_5000\_ (3)](https://user-images.githubusercontent.com/73490814/214579469-29272eee-4b23-4e2b-b7d0-456f35757164.png)

2.  箱网![0 0 0 0_5000\_ (1)](https://user-images.githubusercontent.com/73490814/214578873-102ca7dc-d1eb-4b63-80ae-44840b914c9b.png)

它能够选择不同类型的案例。![0 0 0 0_5000\_ (2)](https://user-images.githubusercontent.com/73490814/214579157-7df4cf7b-7c25-47e2-90c1-e22a1e336a05.png)

### 结果页面

gridjs是用来实现和美化table的。 Grid.js 是一个免费的开源 JavaScript 表格插件。它可以实现这些功能：搜索关键词，排序。

1.  搜索引擎的结果![0 0 0 0_5000_search-web](https://user-images.githubusercontent.com/73490814/214580092-96316127-042a-481b-8517-1923099f7ade.png)
2.  案例网的结果<img width="1354" alt="image" src="https://user-images.githubusercontent.com/73490814/214585512-d7f1d19e-8f06-4fbd-b746-4aab39af825e.png">

![0 0 0 0_5000_search-case](https://user-images.githubusercontent.com/73490814/214585639-69165daf-0900-4cec-9c06-d93fd0e29eb5.png)

点击“显示更多”：<img width="1361" alt="image" src="https://user-images.githubusercontent.com/73490814/214585922-06f21a67-8195-453c-8f75-a4c33381f439.png">

将显示有关此案例的更多详细信息。

## 如何安装和运行项目
把 docker-compose.yaml 放在新建的文件夹里

### Mac
右键点击目标文件夹，选择新建位于文件夹位置的终端窗口
![image](https://user-images.githubusercontent.com/73490814/214628461-86d77f8c-de63-47da-bb91-88d53b161b7d.png)

```bash
docker-compose up
```
control + c to 停止docker的containers

### Windows
- 定位到你存有docker-compose.yaml的文件夹
- 点击地址栏
- 在地址栏输入cmd，按下回车

## 如何使用该项目

页面：[HTTP://0.0.0.0:8080/](http://0.0.0.0:8080/)

Selenium网格处理页面：[HTTP://127.0.0.1:4444/](http://127.0.0.1:4444/)

如果您想发现在爬行过程中发生了什么，可以连接到 VNC 查看器。：[HTTP://127.0.0.1:6900/](http://127.0.0.1:6900/)

## 未来改进

1.  并行处理
2.  数据库
