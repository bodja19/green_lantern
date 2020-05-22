from flask import Blueprint, render_template
from grocery_store.database import db
from flask_login import current_user, login_required
from grocery_store.models import Good, Order, OrderLine, User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',  user=current_user.name, email=current_user.email)

@main.route('//goods_page')
def goods_page():
    rows = Good.query.all()
    return render_template('goods-page.html', rows=rows)

@main.route('//orders')
def order_page():
    user = current_user.user_id








    return render_template('orders.html', workuser=workuser)
