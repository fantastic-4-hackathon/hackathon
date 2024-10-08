from extensions import db

class Age(db.Model):
    __tablename__ = "age_range"

    age_range_id = db.Column(db.Integer, primary_key=True)
    age_range_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<AgeRange {self.age_range_name}>"
    
    def to_dict(self):
        return {
            "age_range_id": self.age_range_id,
            "age_range_name": self.age_range_name,
            "description": self.description,
        }