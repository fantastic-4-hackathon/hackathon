from extensions import db

class Education(db.Model):
    __tablename__ = "education"

    education_id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<Education {self.level}>"
    
    def to_dict(self):
        return {
            "education_id": self.education_id,
            "level": self.level,
        }