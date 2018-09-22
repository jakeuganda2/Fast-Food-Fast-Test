"""This module register the order_APP Blue_print and adds url rules"""
from flask import Blueprint
from app.order.api import OrderAPI

ORDER_APP = Blueprint('ORDER_APP', __name__)

ORDER_VIEW = OrderAPI.as_view('order_api')
ORDER_APP.add_url_rule('/api/v1/orders/', defaults={'order_id': None},
                       view_func=ORDER_VIEW, methods=['GET', ])
ORDER_APP.add_url_rule('/api/v1/orders/',
                       view_func=ORDER_VIEW, methods=['POST', ])
ORDER_APP.add_url_rule('/api/v1/orders/<order_id>',
                       view_func=ORDER_VIEW, methods=['GET', ])
ORDER_APP.add_url_rule('/api/v1/orders/<order_id>',
                       view_func=ORDER_VIEW, methods=['PUT', ])
