import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///users.db')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'supersecretkey') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False