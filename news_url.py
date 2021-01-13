'''
爬取個新聞的內文，並將有關災情的文字存入csv

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


# 設定繁體字典位置 & 加上擴充字典位置
jieba.set_dictionary('jieba_data/user_dict.txt.big')
jieba.load_userdict('jieba_data/user_dict.txt')
jieba.load_userdict('jieba_data/user_dict_location.txt')


#停用字
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


# 自建自典
def user_dict_list():
    user_dict_list=[]
    with open('jieba_data/user_dict.txt','r',encoding='utf-8') as f:
        for line in f:
            user_dict_list.append(line.strip('\n'))
    return user_dict_list


def user_dict_location_list():
    user_dict_location_list=[]
    with open('jieba_data/user_dict_location.txt','r',encoding='utf-8') as f:
        for line in f:
            user_dict_location_list.append(line.strip('\n'))
    return user_dict_location_list


# 公視新聞網
def ftvnews_news(url):
    try :
        headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url= url
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.select('#contentarea')[0].text.replace("\n","")
    except IndexError as er:
        print('error',er)
        content = 'content'
    return content


# 民視新聞
def news_pts(url):
    try :
        headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url= url
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.select('.post-article')[0].text.replace("\n","")
    except IndexError as er:
        print('error',er)
        content = 'content'
    return content

# 中時新聞網
def chinatimes(url):
    try :
        headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url= url
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.select('.article-body')[0].text.replace("\n","")
    except IndexError as er:
        print('error',er)
        content = 'content'
    return content

# 三立新聞網
def setn(url):
    try :
        headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url= url
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.select('#Content1')[0].text.replace("\n","")
    except IndexError as er:
        print('error',er)
        content = 'content'
    return content

# 華視新聞網
def cts(url):
    try :
        headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url= url
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        content = soup.select('.artical-content')[0].text.replace("\n","")
    except IndexError as er:
        print('error',er)
        content = 'content'
    return content

# 自由時報電子報
def ltn(url):
    try :
        headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url= url
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        content = soup.select('.whitecon')[0].text.replace("\n","")
    except IndexError as er:
        print('error',er)
        content = 'content'
    return content

# LINE TODAY
def line(url):
    try :
        headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url= url
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        content = soup.select('.articleContent')[0].text.replace("\n","")
    except IndexError as er:
        print('error',er)
        content = 'content'
    return content

# yahoo
def yahoo(url):
    try :
        headers={'User+Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        url= url
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        content = soup.select('#mrt-node-Col1-3-ContentCanvas')[0].text.replace("\n","")
    except IndexError as er:
        print('error',er)
        content = 'content'
    return content



# 插入dataframe
def df_col(time,media,area,text):
    columns=['time','media','area','text']
    df_f = pd.DataFrame(columns=columns)
    data = [time,media,area,text]
    df_f.loc[len(df_f)] = data
    print(time,area)
    df_f.to_csv('data/news_url_data4.csv', mode='a',index=0, header=0,encoding='utf-8-sig')
    return



# 遍歷dataframe的title並斷詞，是否符合自建自典，有就進入url內抓內文
df = pd.read_csv('data/網路輿情發文來源資料集_2020年04月.csv')
for index,row in df.iterrows():
    if [i for i in cut(row['title']) if i in user_dict_list()]:
        if row['media'] == '公視新聞網':
            text = news_pts(row['url'])
            print(row['url'])
            area = [j for j in cut(text) if j in user_dict_location_list()]
            if area:
                area = sorted(set(area),key = area.index)
            else:
                area = 'no_area'
            df_col(row['datetime_publish'],row['media'], area, text)
        elif row['media'] == '民視新聞':
            text = ftvnews_news(row['url'])
            print(row['url'])
            area = [j for j in cut(text) if j in user_dict_location_list()]
            if area:
                area = sorted(set(area),key = area.index)
            else:
                area = 'no_area'
            df_col(row['datetime_publish'],row['media'], area, text)
        elif row['media'] == '中時新聞網':
            text = chinatimes(row['url'])
            print(row['url'])
            area = [j for j in cut(text) if j in user_dict_location_list()]
            if area:
                area = sorted(set(area),key = area.index)
            else:
                area = 'no_area'
            df_col(row['datetime_publish'],row['media'], area, text)
        elif row['media'] == '三立新聞網':
            text = setn(row['url'])
            print(row['url'])
            area = [j for j in cut(text) if j in user_dict_location_list()]
            if area:
                area = sorted(set(area),key = area.index)
            else:
                area = 'no_area'
            df_col(row['datetime_publish'],row['media'], area, text)
        elif row['media'] == '華視新聞網':
            text = cts(row['url'])
            print(row['url'])
            area = [j for j in cut(text) if j in user_dict_location_list()]
            if area:
                area = sorted(set(area),key = area.index)
            else:
                area = 'no_area'
            df_col(row['datetime_publish'],row['media'], area, text)
        elif row['media'] == '自由時報電子報':
            text = ltn(row['url'])
            print(row['url'])
            area = [j for j in cut(text) if j in user_dict_location_list()]
            if area:
                area = sorted(set(area),key = area.index)
            else:
                area = 'no_area'
            df_col(row['datetime_publish'],row['media'], area, text)
        elif row['media'] == 'LINE TODAY':
            text = line(row['url'])
            print("linetoday",row['url'])
            area = [j for j in cut(text) if j in user_dict_location_list()]
            if area:
                area = sorted(set(area),key = area.index)
            else:
                area = 'no_area'
            df_col(row['datetime_publish'],row['media'], area, text)
        elif row['media'] == '奇摩新聞':
            text = yahoo(row['url'])
            print(row['url'])
            area = [j for j in cut(text) if j in user_dict_location_list()]
            if area:
                area = sorted(set(area),key = area.index)
            else:
                area = 'no_area'
            df_col(row['datetime_publish'],row['media'], area, text)
