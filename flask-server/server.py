from flask import Flask
from config import Config
from extensions import db, bcrypt, jwt
from routes.auth import auth_bp
from routes.file_upload import file_upload_bp


app = Flask(__name__)

# Configure Flask app
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Register blueprints (routes)
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(file_upload_bp, url_prefix='/')

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/mem')
def mem():
    return {"mem": ["memb1","mem2"]}


if __name__ == "__main__":
    app.run(debug=True)