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
    return render_template('profile.html', user=current_user.name, email=current_user.email)


@main.route('//goods_page')
def goods_page():
    rows = Good.query.all()
    return render_template('goods-page.html', rows=rows)


@main.route('//orders')
@login_required
def order_page():
    goods = Good.query.all()
    orders = Order.query.filter_by(user_id=current_user.user_id).all()
    orders_lin = OrderLine.query.all()
    key = []
    for number_order in orders:                     #дістаю ід кожного замовлення
        print(number_order.user_id, number_order.order_id)
        orders_line = OrderLine.query.get(order_id=number_order.number_order)

        #orders_line = OrderLine.query.get()
        print(orders_line)
    return render_template('orders.html', datas=orders, goods=goods)

    # for god_id in good:
    #     Good(good_id=god_id)
    # return render_template('orders.html', goods=goods)

    # user_order = Order.query.filter_by(user_id=current_user.user_id).all()
    #
    # for number_order in user_order:
    #     order_line = [OrderLine.query(OrderLine.good_id).filter_by(order_id=number_order.order_id).all()]
    #     for line in order_line:
    #         good = [Good.query(Good.good_id).filter_by(good_id=line).first()]
    #     good.append(good)
    # goods = Good.query.filter_by(good_id=good).all()
    # return render_template('orders.html', goods=goods)


    # users = User.query.all()
    # goods = Good.query.all()
    # stores = Store.query.all()
    # import pdb;
    # pdb.set_trace()
    # pass
    # # for user in users:
    # #     number_of_orders = randint(1, 5)
    # #     for _ in range(number_of_orders):
    # #         number_of_goods = randint(1, 10)
    # #
    # #         order = Order()
    # #         order_lines = [OrderLine(good=good) for good in sample(goods, number_of_goods)]
    # #         order.order_lines = order_lines
    # #         order.user = user
    # #         order.store = choice(stores)
    # #         db.session.add(order)
    # # db.session.commit()
    # return render_template('orders.html', workuser=workuser)
