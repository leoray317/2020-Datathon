from app import db
from datetime import datetime

class Log(db.Model):
    __tablename__ = "Log"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(50))
    message_type = db.Column(db.String(50))
    message = db.Column(db.String(999))
    create_time= db.Column(db.DateTime, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, user_id, message_type, message=None):
        self.user_id = user_id
        self.message_type = message_type
        self.message = message