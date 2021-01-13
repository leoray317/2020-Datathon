import json
import random
import pandas as pd
import numpy as np
import datetime
import time
import os


# 合併便利商店於df6發票的檔案

df1 = pd.read_csv('data/data_7-11.csv',encoding='cp950')
df2 = pd.read_csv('data/data_familymart.csv',encoding='cp950')
df3 = pd.read_csv('data/data_hilife.csv',encoding='cp950')
df4 = pd.read_csv('data/data_okmart.csv',encoding='cp950')
df5 = pd.read_csv('data/fast_store_detail.csv',encoding='cp950')
df6 = pd.read_csv('data/receipt_all.csv',encoding='utf8', chunksize=1000)


for chunk in df6:
    chunk.columns=['inv_id','item_no','product_name','unit_price','quantity','amonut','inv_time','login_time','company_name','seller_address','unknow','gender','age']

    df1_merge = pd.merge(chunk, df1, on=['seller_address'])
    df2_merge = pd.merge(chunk, df2, on=['seller_address'])
    df3_merge = pd.merge(chunk, df3, on=['seller_address'])
    df4_merge = pd.merge(chunk, df4, on=['seller_address'])
    df5_merge = pd.merge(chunk, df5, on=['seller_address'])

    df_concat = pd.concat([df1_merge,df2_merge,df3_merge,df4_merge,df5_merge],axis=0)    
    #print(df_concat)
    print(chunk['product_name'],chunk['company_name'])
    df_concat.to_csv('data/store_merge_receipt_all.csv', mode='a',index=0, header=0,encoding='utf-8-sig')

