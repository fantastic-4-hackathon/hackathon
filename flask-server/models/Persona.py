from extensions import db


class Age(db.Model):
    __tablename__ = "age_range"

    age_range_id = db.Column(db.Integer, primary_key=True)
    age_range_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<AgeRange {self.age_range_name}>"


class CommunicationStyle(db.Model):
    __tablename__ = "communication_style"

    communication_style_id = db.Column(db.Integer, primary_key=True)
    communication_channel = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<CommunicationStyle {self.communication_channel}>"


class Education(db.Model):
    __tablename__ = "education"

    education_id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<Education {self.level}>"


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
