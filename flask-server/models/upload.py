from extensions import db
from datetime import datetime

class Upload(db.Model):
    __tablename__ = "uploads"

    upload_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    upload_text = db.Column(db.Text)  # equivalent to NVARCHAR(MAX
    upload_url = db.Column(db.String(255))  
    created_at = db.Column(db.DateTime, default=datetime.now)  


    def __repr__(self):
        return f"<Uploads {self.upload_text}>"
    
    def to_dict(self):
        return {
            "upload_id": self.upload_id,
            "upload_text": self.upload_text,
            "upload_url": self.upload_url,
            "created_at": self.created_at,
        }