from extensions import db

class Persona(db.Model):
    __tablename__ = "persona"

    persona_id = db.Column(db.Integer, primary_key=True)
    persona_name = db.Column(db.String(50), nullable=False)
    age_range_id = db.Column(
        db.Integer, db.ForeignKey("age_range.age_range_id"), nullable=False
    )
    gender = db.Column(db.String(50), nullable=False)
    education_id = db.Column(
        db.Integer, db.ForeignKey("education.education_id"), nullable=False
    )
    thinking_style = db.Column(db.String(50), nullable=False)
    communication_style_id = db.Column(
        db.Integer, db.ForeignKey("communication_style.communication_style_id")
    )

    short_term_goal = db.Column(db.String(50))
    long_term_goal = db.Column(db.String(50))

    # Relationships
    age_range = db.relationship("Age")
    education = db.relationship("Education")
    communication_style = db.relationship("CommunicationStyle")

    def __repr__(self):
        return f"<Persona {self.persona_name}>"
    
    def to_dict(self):
        return {
            "persona_id": self.persona_id,
            "persona_name": self.persona_name,
            "age_range_id": self.age_range_id,
            "gender" : self.gender,
            "education_id": self.education_id,
            "thinking_style": self.thinking_style,
            "communication_style_id": self.communication_style_id,
            "short_term_goal": self.short_term_goal,
            "long_term_goal":self.long_term_goal,
        }
