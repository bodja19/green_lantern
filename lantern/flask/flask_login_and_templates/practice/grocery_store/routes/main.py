from flask import Blueprint, render_template
from grocery_store.database import db
from flask_login import current_user, login_required
from grocery_store.models import Good, Order, OrderLine, Store
from datetime import datetime
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
    if len(manager_store) == 0:
        return render_template('profile.html', user=current_user.name, email=current_user.email)
    return render_template('profile.html', user=current_user.name, email=current_user.email, stores=manager_store)


@main.route('//goods_page')
def goods_page():
    rows = Good.query.all()
    return render_template('goods-page.html', rows=rows)


@main.route('//orders')
@login_required
def order_page():
    key = []
    order = []
    for number_order in Order.query.filter_by(user_id=current_user.user_id).all():                     #дістаю ід кожного замовлення
        suma_order = 0
        order_time = datetime.strftime(number_order.created_time, '%G-%b-%d %I:%M %p')
        listorder = {'numberOrder': number_order.order_id,
                     'time': order_time,
                     'name': '',
                     'price': '',
                     'suma': ''}
        key.append(listorder)
        for orderline in OrderLine.query.filter(number_order.order_id == OrderLine.order_id).all():
            good = Good.query.filter(orderline.good_id == Good.good_id).first()
            listorder = {'name': good.name,
                         'price': good.price}
            key.append(listorder)
            suma_order += good.price
        listorder = {'suma': suma_order}
        key.append(listorder)
        order.append(suma_order)
    all_sume = sum(order)
    print('aaaaaaaaaaaaaaaa')
    print(all_sume, 'aaaaaaaaaaaaaaa')

    # listorder = {'all_sume': all_sume}
    # key.append(listorder)
    # print(all_sume)
    return render_template('orders.html', goods=key, all_sume=all_sume)










