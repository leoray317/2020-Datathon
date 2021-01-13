from app import line_bot_api
from linebot.models import (
    RichMenuArea, RichMenu, RichMenuBounds, RichMenuSize,  
    MessageAction, URIAction, ImagemapAction

)

rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=2500, height=1686),
    selected=False,
    name="test20",
    chat_bar_text="Menu",
    areas=[
        RichMenuArea(
            bounds=RichMenuBounds(x=721, y=0, width=1038, height=576),
            action=MessageAction(label='History', text="History of flooding area")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=1767, y=0, width=733, height=690),
            action=MessageAction(label='Damage', text="Damage level")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=1097, width=869, height=589),
            action=URIAction(label='github', uri="https://github.com/arthurtibame")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=716, height=801),
            action=URIAction(label='Linkedin', uri="https://www.linkedin.com/in/shuli-lin-1679a9152/")
        ),

        RichMenuArea(
            bounds=RichMenuBounds(x=1653, y=1101, width=847, height=595),
            action=MessageAction(label='heat', text="Disaster supply heat map")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=736, y=594, width=1017, height=476),
            action=URIAction(label='Datathon', uri="https://2020datathon.wixsite.com/hack")
        )
    ]
)
rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# print(rich_menu_id)

with open("./app/static/image/final.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image(rich_menu_id,  "image/png", f)
line_bot_api.set_default_rich_menu(rich_menu_id)    
print("done!")  