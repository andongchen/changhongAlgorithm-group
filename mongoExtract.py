# -*- coding: utf-8 -*-
"""
20161013
从mongo中抽取文章内容
"""
import codecs
from pymongo import MongoClient
import os
import time
import sys
import traceback
import codecs

'''
start = time.clock()
#path = r'E:\changhong\dataextract525'
path = r'E:\changhong\dataextract802\27new'#存到本地的路径
client = MongoClient('10.9.201.190', 27017)
#db = client.community #连接的数据库
db = client.MALASQ

for a in db.mala_article_info_collect.find({'object_content':{'$ne':None}}):
      # a1 = a['content']
      # a2 = a['entityName']

    if a['siteId'] == '27':
        a1 = a['object_content'] #要抽取得字段
        a2 = a['_id']

        try:
              f = codecs.open(os.path.join(path,a2.__str__()+'.txt'),'w','utf-8')#python 写入路径不可有&、怎么处理
             # print f
        except:traceback.print_exc()
        if a1 == None :#or a1 == '':#忽略为空的文本
              continue
        f.write(a1)
        f.close()

end = time.clock()
print (end-start,'s') '''

start = time.clock()
#path = r'E:\changhong\dataextract525'
path = r'E:\changhong\dataextract802\27_newwordpre'#存到本地的路径
client = MongoClient('10.9.201.190', 27017)
db = client.community #连接的数据库

#{'publishDate':{'$gt':'2016-07-01 00:00:00'},'content':{'$ne':None}  怎么就不行呢
for a in db.article_info_collect.find({'publishDate':{'$gt':'2016-07-20 00:00:00'},'content':{'$ne':None}}):#,
      # a1 = a['content']
      # a2 = a['entityName']


    a1 = a['content'] #要抽取得字段
    a2 = a['_id']
    # print a
    # break
    try:
          f = codecs.open(os.path.join(path,a2.__str__()+'.txt'),'w','utf-8')#python 写入路径不可有&、怎么处理
         # print f
    except:traceback.print_exc()
    if a1 == None :#or a1 == '':#忽略为空的文本
          continue
    f.write(a1)
    f.close()

end = time.clock()
print (end-start,'s')

