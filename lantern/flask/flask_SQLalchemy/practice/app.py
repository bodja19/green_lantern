from flask import  Flask
from flask_SQLalchemy import SQLAlchemy
import os
from Config import Config

class Config:
    PG_USER = "cursor"
    PG_PASSWORD = "very_secret_password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "cursor"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False




db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('Database exists')
    else:
        print(f'Database does not exists{db.engine.url}')
        create_database(db.engine,url)
        print('Data base created')