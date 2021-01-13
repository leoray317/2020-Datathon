import requests


def flooding_town():    
    res = requests.get("http://fhy.wra.gov.tw/WraApi/v1/Rain/Warning?$top=100")
    res_json = res.json()    
    return res_json


if __name__ == "__main__":
    print(flooding_town())
