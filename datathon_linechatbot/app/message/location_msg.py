from app import handler, line_bot_api

from linebot.models.events import (
    LocationMessage
)
from linebot.models import(
    MessageEvent, TextSendMessage
)

@handler.add(MessageEvent, message=LocationMessage)
def location_handler(event):    
    from app.service.user_service import udpate_location
    res = udpate_location(event)
    print(res)
    line_bot_api.reply_message( 
        event.reply_token,
        TextSendMessage(text="已更新您的位置 !"))
    
    


