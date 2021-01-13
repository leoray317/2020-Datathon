from app import line_bot_api, handler

from linebot.models import(
    MessageEvent, TextSendMessage, VideoMessage
)

@handler.add(MessageEvent, message=VideoMessage)
def handler_video_message(event):
    """[summary]

    Args:
        event ([type]): [line bot event-> pass img]        
    Func 1.
        get img msg and reply msg    
    Func 2.
        upload iamge to AWS S3 client
    Func 3. (optional)
        udpate image detail(uploader id, image_path) to db         
    """
    # Step 1. Get message_id
    message_content = line_bot_api.get_message_content(event.message.id)
    file_name = f"{event.message.id }.mp4"

    # write iamge by message content (from user sent)
    with open(file_name, "wb") as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
     
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text=f"Video saved ! {file_name}"),            
        ],
    )