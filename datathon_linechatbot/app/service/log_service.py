from app.model.log_model import Log
from app import db

def insert_log(logs):
    user_id = logs["source"]["userId"]
    message_type = logs["message"]["type"]
    message = ""    
    if message_type=="text":
        try:
           message= logs["message"]["text"]
        except:
            return None
    new_log = Log(user_id=user_id, message_type=message_type, message=message)
    db.session.add(new_log)    
    db.session.commit()
    return "Inserted log"