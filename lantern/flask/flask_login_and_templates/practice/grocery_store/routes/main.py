from flask import Blueprint, render_template
from grocery_store.database import db
from flask_login import current_user
from grocery_store.models import Good

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html', user=current_user.name, email=current_user.email)

@main.route('/goods')
def goods_page():
    return render_template('goods-page.html', good=Good.query.all)
