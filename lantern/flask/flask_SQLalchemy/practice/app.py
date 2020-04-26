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

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, drop_database, database_exists

from config import Config
from populate_data import get_users


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)



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

        print(f"Database does not exists {db.engine.url}")
        create_database(db.engine.url)
        print('Data base created')

with app.app_context():
    users = get_users()
    for user in users:
        db.session.add(User(**user))
    db.session.commit()
    print('Data written in data_base succesfuly')

