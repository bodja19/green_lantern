from flask import Blueprint, render_template
from grocery_store.database import db
from flask_login import current_user, login_required
from grocery_store.models import Good, Order, OrderLine, Store

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    stores = Store.query.filter_by(manager_id=current_user.user_id).all()
    manager_store = []
    for store in stores:
        manager_store.append(store)

    return render_template('profile.html', user=current_user.name, email=current_user.email, stores=manager_store)


@main.route('//goods_page')
def goods_page():
    rows = Good.query.all()
    return render_template('goods-page.html', rows=rows)


@main.route('//orders')
@login_required
def order_page():
    orders = Order.query.filter_by(user_id=current_user.user_id).all()
    key = []

    for number_order in orders:                     #дістаю ід кожного замовлення
        listorder = {'numberOrder': number_order.order_id,
                     'time': number_order.created_time,
                     'name': '',
                     'price': ''}
        key.append(listorder)
        for orderline in OrderLine.query.filter(number_order.order_id == OrderLine.order_id).all():
            good = Good.query.filter(orderline.good_id == Good.good_id).first()
            goodname = good.name
            goodprice = good.price
            print(good.name)
            print(orderline.good_id)
            listorder = {'name': goodname,
                         'price': goodprice}
            # listorder = goodname, goodprice
            key.append(listorder)
    print('Отут буде key')
    print(key)
    print('list')
    print(listorder)
    goods = []
    # for good in listorders:
    #     good = Good
    return render_template('orders.html', goods=key)






