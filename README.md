# 使用方法
1.安装python3环境
> * [windows安装方法](https://blog.csdn.net/qq_41952474/article/details/82630551)
> * [linux安装方法（centos7为例）](https://www.cnblogs.com/anxminise/p/9650206.html)

------

2.部署代码
linux：
```cmd
git clone https://github.com/Turnright-git/text2mysql.git
cd text2mysql.git
pip3 install -r requirements.txt
python3 main.py
```
windows:
> * [下载源码](https://github.com/Turnright-git/text2mysql/archive/master.zip)
> * 解压并进入master\text2mysql文件夹
> * pip install -r requirements.txt
> * python3 main.py

------

3.修改配置文件
项目中config.py为配置文件
```python
# 数据库信息
db_config = {
    'host': '127.0.0.1', # 连接
    'port': 3306, # 端口
    'user': 'root',# 用户名
    'passwd': 'root', # 密码
    'charset': 'utf8',# 数据库字符集
    'db': 'test'# 数据库名
}

# text文件路径
title_files = "title/title.txt" #存放文章标题，一行一个
content_files = "content/" #存放文章内容的文件夹，命名需与文章标题一致，如标题在第一行则内容为1.txt。注意“/”
```
------

4.注意事项
> * 1.txt编码应为utf8，以防乱码
> * 2.数据库未做去重，需导入到全新数据库

------