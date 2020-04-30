from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, drop_database, database_exists
# import os
from Config import Config
from populate_data import get_users, get_goods, get_stores

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(), nullable=False)

class Product(db.Model):
    __tablename__ = "goods"

    product_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Store(db.Model):
    __tablename__ = "stores"

    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False, primary_key=True)





app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('database_exists')
    else:
        print(f"Database does not exists {db.engine.url}")
        create_database(db.engine.url)
        print("Database created")

with app.app_context():
    users = get_users()
    for user in users:
        db.session.add(User(**user))
    db.session.commit()
    print('Database users writen base successfully')

with app.app_context():
    goods = get_goods()
    for product in goods:
        db.session.add(Product(**product))
    db.session.commit()
    print('Database goods writen base successfully')

with app.app_context():
    stores = get_stores()
    for store in stores:
        db.session.add(Store(**store))
    db.session.commit()
    print('Database store writen base successfully')












#
