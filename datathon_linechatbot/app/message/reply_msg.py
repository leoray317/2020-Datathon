from app import handler, line_bot_api

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    ImageSendMessage
)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
        
    if event.message.text == "否, 下次再傳送":
        line_bot_api.reply_message( 
            event.reply_token,
            TextSendMessage(text="謝謝您, 隨時歡迎更新位置"))

    elif event.message.text == "History of flooding area":
        line_bot_api.reply_message( 
            event.reply_token,
            ImageSendMessage(original_content_url="https://i.imgur.com/DFkVFPU.png", preview_image_url="https://i.imgur.com/DFkVFPU.png"))
    elif event.message.text == "Damage level":
        line_bot_api.reply_message( 
            event.reply_token,
            ImageSendMessage(original_content_url="https://i.imgur.com/MNms0NS.png", preview_image_url="https://i.imgur.com/MNms0NS.png"))
    elif event.message.text == "Disaster supply heat map":
        line_bot_api.reply_message( 
            event.reply_token,
            ImageSendMessage(original_content_url="https://i.imgur.com/wY9Zssj.png", preview_image_url="https://i.imgur.com/wY9Zssj.png"))