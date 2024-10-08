import os
from flask import Flask
from config import Config
from extensions import db, bcrypt, jwt
from flask_cors import CORS
from dotenv import load_dotenv
from sqlalchemy.sql import text


load_dotenv()

app = Flask(__name__)
CORS(app)
# Configure Flask app
app.config.from_object(Config)

connection_string = os.environ.get("LOCAL_CONNECTION_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# imports for the blueprints
# TODO: UNcomment quins code
from routes.auth import auth_bp

from routes.file_upload import file_upload_bp
from routes.Persona import Persona_bp
from routes.Age import age_bp
from routes.Education import education_bp
from routes.CommunicationStyle import CommunicationStyle_bp

# Register blueprints (routes)
app.register_blueprint(auth_bp, url_prefix="/")
app.register_blueprint(file_upload_bp, url_prefix="/")
app.register_blueprint(Persona_bp, url_prefix="/persona")
app.register_blueprint(age_bp, url_prefix="/age")
app.register_blueprint(education_bp, url_prefix="/education")
app.register_blueprint(CommunicationStyle_bp, url_prefix="/communication")

# Create the database tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
    try:
        with app.app_context():
            # Use text() to explicitly declare your SQL command
            result = db.session.execute(text("SELECT 1")).fetchall()
            # db.drop_all()
            # db.create_all()
            print("Connection successful:", result)
    except Exception as e:
        print("Error connecting to the database:", e)
