# Law-Crawler
python -m venv venv
### set python version is 3.8
virtualenv venv --python=/usr/local/bin/python3.8

source env/bin/activate

pip install -r requirements.txt

export FLASK_APP=app

export FLASK_ENV=development

flask run

lawsdata:
18145132237
bYK3B27i3jtF6

wusong
18145132237
EX0w&6t$4A0

## 因为GoogleChrome Driver 出现问题， 选择另一种方法进行下载
pip install chromedriver-py==108.0.5359.22
### 本机的版本是108.0.5359.22 所以选择下载这个
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)

### 经过尝试之后， 成功运行

