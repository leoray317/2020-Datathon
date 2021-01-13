import json
from datetime import datetime

def event2json(event) -> dict:
    return json.loads(str(event))

def datetime_now() -> datetime:
    return datetime.now()

def timestamp_converter(timestamp) -> str(datetime):
    """[summary]
    Args:
        timestamp ([int]): 
            input timestamp is milliseconds
            get rid of it and transger to string datetime
    """
    timestamp: int =int(str(timestamp)[:-3])
    str_datetime: str = datetime.strftime(datetime.fromtimestamp(timestamp), "%Y-%m-%dT%H:%M:%S")
    return str_datetime

def logs_handler(logs, line_bot_api):
    from app.service.user_service import create_user
    from app.service.log_service import insert_log
    
    """[summary]

    Args:
        line logs, line_bot_api
        message types:
            text, sticker, audio, location, image, video
    function:
        distinguish the type of logs and produce to kafka 
        with different topics            
    """
    logs = event2json(logs)["events"][0]    
    if logs["type"] == "follow":        
        user_id = logs["source"]["userId"]
        profile=line_bot_api.get_profile(user_id)
        create_user(profile, user_id)               

    elif logs["type"] == "message":
        insert_log(logs)
          
    else:
        pass

    
    