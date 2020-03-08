# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2020/3/8 10:58
@Author  : Turnright-git
@Email   : weifeizxy@gmail.com
@Software: PyCharm
"""

from config import title_files, content_files
from utils.DBtools import MysqldbHelper
import uuid as uuid_tools
import time
import chardet


def get_all_title():
    f = open(title_files, "rb")
    r = f.readlines()
    f.close()
    index = 1
    title_list = []
    content_list = []
    for line in r:
        id = index
        f_charinfo = chardet.detect(line)
        title = line.decode(f_charinfo['encoding']).replace("\r", "").replace("\n", "")
        try:
            c = open("{}{}.txt".format(content_files, str(index)), "rb")
            rc = c.read()
            c_charinfo = chardet.detect(rc)
            content = rc.decode(c_charinfo['encoding'], "ignore").replace("\u3000\u3000", "  ")
            index += 1
        except:
            break
        else:
            uuid = str(uuid_tools.uuid4())
            description = content[0:20]
            publish_time = int(time.time())
            title_list.append([title, id, uuid, 2,  publish_time, description,uuid])
            content_list.append([uuid,content])
    return {'title_list':title_list,"content_list":content_list}


def inster_to_db():
    try:
        db=MysqldbHelper()
        data=get_all_title()
        title_list=data['title_list']
        content_list=data['content_list']
        db.insertMany('mip_articles',['title','id','uuid','cid','publish_time','description','content_id'],title_list)
        db.insertMany('mip_articles_content',['id','content'],content_list)
        insert_num=len(title_list)
        return insert_num
    except Exception as e:
        print(e)
        return False



if __name__ == "__main__":
    todo=inster_to_db()
    if not todo:
        pass
    else:
        print("成功插入{}条内容".format(todo))

