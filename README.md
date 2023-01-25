# Law case crawler | 法律案例爬虫
- [简体中文](README.zh-CN.md)

Law case crawler is a project which to crawl, scrape and visualize law cases from three search engine (Baidu, Sogou and Wechat) and two law case search websites (wusong and bashou). It executes with Selenium grid docker, Flask and gunicorn. This is the first version. In the next version, it will implement parallel processes and store the acquired data in the database to accelerate processing and minimize caching. 

## Structure
<img width="981" alt="image" src="https://user-images.githubusercontent.com/73490814/214577434-349674c2-eac8-4f93-9e51-dd609273c757.png">

## Screenshots
### Homepage
1. Search engines
<img width="1356" alt="image" src="https://user-images.githubusercontent.com/73490814/214578514-23a388bb-84a2-4b76-ad9b-c2a80eb5f800.png">

Three search engines can be chose.
![0 0 0 0_5000_ (3)](https://user-images.githubusercontent.com/73490814/214579469-29272eee-4b23-4e2b-b7d0-456f35757164.png)


2. Case webs
![0 0 0 0_5000_ (1)](https://user-images.githubusercontent.com/73490814/214578873-102ca7dc-d1eb-4b63-80ae-44840b914c9b.png)

It's able to select different types of cases.
![0 0 0 0_5000_ (2)](https://user-images.githubusercontent.com/73490814/214579157-7df4cf7b-7c25-47e2-90c1-e22a1e336a05.png)

### Result page
gridjs is used to realize the table. Grid.js is a Free and open-source JavaScript table plugin. It can implement these functions: search key words, sorting.
1. Search engines' results
![0 0 0 0_5000_search-web](https://user-images.githubusercontent.com/73490814/214580092-96316127-042a-481b-8517-1923099f7ade.png)
2. Case webs' results
<img width="1354" alt="image" src="https://user-images.githubusercontent.com/73490814/214585512-d7f1d19e-8f06-4fbd-b746-4aab39af825e.png">

![0 0 0 0_5000_search-case](https://user-images.githubusercontent.com/73490814/214585639-69165daf-0900-4cec-9c06-d93fd0e29eb5.png)

Click on "Show more": 
<img width="1361" alt="image" src="https://user-images.githubusercontent.com/73490814/214585922-06f21a67-8195-453c-8f75-a4c33381f439.png">

More details about this case will be displayed.

## How to Install and Run the Project
Put docker-compose.yaml into a folder

### Mac
On a Mac you just need to right click on the target folder, go to services and New Terminal at Folder
![image](https://user-images.githubusercontent.com/73490814/214628461-86d77f8c-de63-47da-bb91-88d53b161b7d.png)

```bash
docker-compose up
```
control + c to stop the Docker containers

### Windows
- Navigate to the target folder where docker-compose.yml lives in the explorer
- Click on the address bar in Windows Explorer
- Type cmd in the address bar and hit Enter

## How to Use the Project
Portal page:  http://0.0.0.0:8080/

Selenium grid processing page: http://127.0.0.1:4444/

If you want to discover what happens during the crawling, connecting to VNC viewer is available.:
http://127.0.0.1:6900/

## Future improvement
1. Parallel procession
2. Database
