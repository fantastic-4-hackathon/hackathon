from extensions import db

class Contacts(db.Model):
    __tablename__ = "contacts"

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(150), nullable=False)  
    customer_lastname = db.Column(db.String(150), nullable=False) 
    phone_number = db.Column(db.String(150), nullable=False)



    def __repr__(self):
        return f"<Contacts {self.level}>"
    
    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "customer_lastname": self.customer_lastname ,
            "phone_number": self.phone_number ,
        }