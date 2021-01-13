from app import db
from datetime import datetime

class Flooding(db.Model):
    __tablename__ = "Flooding"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.String(100))
    create_time= db.Column(db.DateTime, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id) -> None:
        self.user_id = user_id
        
