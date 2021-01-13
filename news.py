import json
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import datetime
import time


# json to csv
def jtoc():
    df = pd.read_json('data/news_json/網路輿情發文來源資料集_2020年06月.json')
    df.to_csv('data/網路輿情發文來源資料集_2020年06月.csv', mode='a',index=0,encoding='utf-8-sig')
    print(df)

jtoc()