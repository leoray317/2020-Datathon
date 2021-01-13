import json
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import datetime
import time

# 淹水警戒爬蟲

def water():
    path = 'data/water.csv'
    city_name=['桃園市','台南市','台中市','新北市','高雄市','台北市','嘉義市','新竹市','基隆市','澎湖縣','花蓮縣','台東縣','屏東縣','嘉義縣','雲林縣','南投縣','彰化縣','苗栗縣','新竹縣','宜蘭縣','金門縣','連江縣']
    city_id=['68','67','66','65','64','63','10020','10018','10017','10016','10015','10014','10013','10010','10009','10008','10007','10005','10004','10002','09020','09007']
    columns=['city', 'Name', 'CityID',  'TownID', 'Flood', 'Lv1_12H', 'Lv1_1H', 'Lv1_24H', 'Lv1_3H', 'Lv1_6H', 'Lv2_12H', 'Lv2_1H', 'Lv2_24H', 'Lv2_3H', 'Lv2_6H', 'Murgang', 'SlopeLand']
    df=pd.DataFrame(columns=columns)
    df.to_csv(path,encoding='utf-8-sig',index=0)

    # 爬取各city的淹水狀況
    for i in range(len(city_name)):
        url = "https://dmap.ncdr.nat.gov.tw/Umbraco/Api/AjaxApi/GetWarningDataByCityId?cityId="+city_id[i]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
        res = requests.get(url, headers=headers)
        
        df = pd.DataFrame(json.loads(res.text)['DisasterData'])

        # 插入地區欄位，並將欄位移至最前面
        df['city'] = city_name[i]
        cols = df.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        df=df[cols]
        
        # 輸出
        df.to_csv(path, mode='a',index=0, header=0)
        print(df)

if __name__ == "__main__":
    water()