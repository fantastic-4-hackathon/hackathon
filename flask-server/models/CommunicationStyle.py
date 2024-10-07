from extensions import db

class CommunicationStyle(db.Model):
    __tablename__ = "communication_style"

    communication_style_id = db.Column(db.Integer, primary_key=True)
    communication_channel = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<CommunicationStyle {self.communication_channel}>"
    
    def to_dict(self):
        return {
            "communication_style_id": self.communication_style_id,
            "communication_channel": self.communication_channel,
        }