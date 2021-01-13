from app import handler, line_bot_api
from app.message import quick_reply_msg

from linebot.models.events import JoinEvent, FollowEvent

from linebot.models import (
    TextSendMessage, TextMessage, QuickReply, QuickReplyButton, MessageAction, LocationAction
)

@handler.add(FollowEvent)
def handle_join(event):    
    
    profile=line_bot_api.get_profile(event.source.user_id)
    opening_text = f"👋👋👋👋 {profile.display_name} 您好\n\
為了您有更好的系統體驗, 是否傳送您目前的居住位置呢 \
    " 
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=opening_text,
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=MessageAction(label="否, 下次再傳送", text="否, 下次再傳送")),                    
                    QuickReplyButton(action=LocationAction(label="是的, 我很願意有更好的體驗"))
                ],
            )
        )
    )
  

    