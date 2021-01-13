from app.model.user_model import User
from app.model.flooding_model import Flooding
from app.utils.flood_api import flooding_town
from app import line_bot_api, app, db
from linebot.models import (
    TextSendMessage
)

a= [{
    "StationNo": "C0AD00",
    "CityCode": "65",
    "TownCode": "6800600",
    "Time": "2020-09-12T20:20:00",
    "M10": 0,
    "H1": 0,
    "H3": 97,
    "H6": 207.5,
    "H12": 207.5,
    "H24": 207.5,
    "WarningLevel": 1,
    "AffectedArea": "三芝區-後厝里,古庄里,埔頭里,圓山里,新庄里,福德里,橫山里,興華里,錫板里,店子里,埔坪里,八賢里,中正路"
  }]

@app.route("/check", methods=["GET", "POST"])
def check_flooding_users():
    flooding_towns = flooding_town()
    
    for town in flooding_towns:
        town_code = town['TownCode']
        users = User.query.filter_by(town=town_code).all()
        tmp_user_id_list = list()
        for user in users:
            tmp_user_id_list.append(user.user_id)
        
        send_text = "🚨請注意您所居住的地區 {} 有淹水警報 !\n\n\n累積雨量狀況:\n1小時累計雨量(mm) 👉👉  {}\n\n3小時累計雨量(mm) 👉👉  {}\n\n6小時累計雨量(mm) 👉👉  {}\n\n12小時累計雨量(mm) 👉👉  {}\n\n24小時累計雨量(mm) 👉👉  {}\n\n警戒級別 👉👉  {}\n\n"\
            .format(town["AffectedArea"][:3], town["H1"],town["H3"],town["H6"],town["H12"],town["H24"],town["WarningLevel"])

        line_bot_api.multicast(tmp_user_id_list, TextSendMessage(text=send_text))
        
        db.session.add_all([Flooding(user_id=user_id) for user_id in tmp_user_id_list])
        db.session.commit() 
    return "Done"


if __name__ == "__main__":
    print(check_flooding_users())
