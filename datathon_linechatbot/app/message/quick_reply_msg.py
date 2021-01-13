from linebot.models import (
    TextSendMessage, QuickReplyButton, MessageAction, QuickReply
)

text_message = TextSendMessage(
    text='Hello, world',
    quick_reply=QuickReply(items=[
        QuickReplyButton(action=MessageAction(label="label", text="text"))
        ]
    )
)

