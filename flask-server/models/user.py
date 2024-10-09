from extensions import db


# User Model
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_Ecode = db.Column(db.String(150), unique=True, nullable=False)
    user_name = db.Column(db.String(150), nullable=False)
    user_lastname = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<Uploads {self.user_Ecode}>"

    def to_dict(self):
        return {
            "user_Ecode": self.user_Ecode,
            "user_name": self.user_name,
            "user_lastname": self.user_lastname,
            "password_hash": self.password_hash,
        }
