import json
import random
import pandas as pd
import numpy as np
import datetime
import time
import os
from pandas.io.json import json_normalize

# 讀資料夾內json資料
store_name = 'okmart'
path = 'data/'+store_name+'/'
json_files = [i for i in os.listdir(path)]

#columns=['POIID','POIName','X','Y','Telno','FaxNo','Address','isDining','isParking','isLavatory','isATM','is7WiFi','isIce','isHotDog','isHealthStations','isIceCream',	'isOpenStore','isFruit','isCityCafe','isUnionPay','isOrganic','isCorn','isMakeup','isMuji','isMisterDonuts','SpecialStore_Kind','Store_URL','city_id','city_name']

for i in json_files:
    with open(path+i,encoding='utf-8') as json_file:
        x = json.load(json_file)
        result = json_normalize(x, 'stores', ['city_name'])
        result['store_name']='okmart'
        result.to_csv('data/'+store_name+'.csv',mode='a',encoding='cp950')
        print(result.head(3))

