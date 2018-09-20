"""This module handles OrderAPI class and its methods"""
import uuid
from flask.views import MethodView
from flask import jsonify, request, make_response
from app.models import Order


class OrderAPI(MethodView):
    """This class based view handles Order related methods"""

    @classmethod
    def get(cls, order_id):
        """Method for  get orders"""
        if order_id:
            order_id = uuid.UUID(order_id)
            orders = Order.view_all_orders()
            for order in orders:
                if order_id == order['order_id']:
                    return jsonify(order), 200
                return jsonify({'message': "Order Not Found "}), 404
        else:
            orders = Order.view_all_orders()
            if orders == []:
                response = {
                    "message": "No Available Orders"}
                return make_response(jsonify(response)), 200
            return jsonify(orders), 200

    @classmethod
    def post(cls):
        '''Method for a post order'''
        data = request.json
        name = data["name"]
        price = data["price"]
        order_date = data["order_date"]
        new_order = Order.make_order(name, price, order_date)
        if new_order == "Order Made Successfully":
            return jsonify({'message': new_order}), 201
        return jsonify({'message': new_order}), 409
