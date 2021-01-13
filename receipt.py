'''
將攔位名稱進行斷字，並篩出指定防災用品字串。存入csv

'''


import json
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import datetime
import time
import jieba

# 全形轉半形
def strQ2B(ustring):
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全形空格直接轉換
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # 全形字元（除空格）根據關係轉化
                inside_code -= 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return ''.join(ss)

# 引入jieba字典
jieba.set_dictionary('jieba_data/user_dict.txt.big')
jieba.load_userdict('jieba_data/user_receipt.txt')

# 引入停用字
with open(file='jieba_data/simple_stop_words.txt', mode='r', encoding='utf-8') as file:
    stop_words = file.read().split('\n')

# 精確模式分詞 (cut_all=False)
def cut(data):
    seg_stop_result_list = []
    seg_result = jieba.cut(data, cut_all=False)
    for term in seg_result:
        if term not in stop_words and term != ' ':
            seg_stop_result_list.append(term)
    return seg_stop_result_list

# 字典轉list
def user_dict_list():
    user_dict_list=[]
    with open('jieba_data/user_receipt.txt','r',encoding='utf-8') as f:
        for line in f:
            user_dict_list.append(line.strip('\n'))
    return user_dict_list

# 存入csv
def df_col(inv_id, item_no, product_name, unit_price, quantity, amonut, inv_time, login_time, company_name, seller_address, unknow, gender, age):
    data = [inv_id, item_no, product_name, unit_price, quantity, amonut, inv_time, login_time, company_name, seller_address, unknow, gender, age]
    df1 = pd.DataFrame(columns=['inv_id','item_no','product_name','unit_price','quantity','amonut','inv_time','login_time','company_name','seller_address','unknow','gender','age'])
    df1.loc[len(df1)] = data
    print(df1)
    #df1.to_csv('data/receipt_all.csv', mode='a',index=0, header=0,encoding='utf-8-sig')
    return

# 遍歷df title是否符合自建自典
df = pd.read_csv('data/invoice_qmonster.csv',header=None,encoding='utf8', chunksize=100)
#df.columns=['inv_id','item_no','product_name','unit_price','quantity','amonut','inv_time','login_time','company_name','seller_address','unknow','gender','age']
#df.columns=['inv_id','item_no','product_name','unit_price','quantity','amonut','seller_address','inv_time','login_time','gender','age','1','2','3','4','5','6','7']
#df_f = pd.DataFrame(columns=columns)

for chunk in df:
    chunk.columns=['inv_id','item_no','product_name','unit_price','quantity','amonut','inv_time','login_time','company_name','seller_address','unknow','gender','age']
    for index,row in chunk.astype(str).iterrows():
        cut_list = [i for i in cut(row['product_name']) if i in user_dict_list()]
        if cut_list :
            inv_id = row['inv_id']
            item_no = row['item_no']
            product_name = row['product_name']
            unit_price = row['unit_price']
            quantity = row['quantity']
            amonut = row['amonut']
            inv_time = row['inv_time']
            login_time = row['login_time']
            company_name = row['company_name']
            seller_address = row['seller_address']
            unknow = row['unknow']
            gender = row['gender']
            age = row['age']
    
            df_col(inv_id, item_no, product_name, unit_price, quantity, amonut, inv_time, login_time, company_name, seller_address, unknow, gender, age)

