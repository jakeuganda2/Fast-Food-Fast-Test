import uuid
from flask.views import MethodView
from flask import jsonify, request, make_response
from app.models import Order


class OrderAPI(MethodView):

    def get(self, order_id):
        if order_id:
            order_id = uuid.UUID(order_id)
            orders = Order.get_all_orders()
            for order in orders:
                if order_id == order['order_id']:
                    return jsonify(order), 200
            return jsonify({'message': "Order Not Found "}), 404
        else:
            orders = Order.get_all_orders()
            if orders == []:
                response = {
                    "message": "No Orders Available"}
                return make_response(jsonify(response)), 200
            return jsonify(orders), 200

    def post(self):
        data = request.json
        item_name = data["item_name"]
        price = data["price"]
        order_date = data["order_date"]
        user_name = data["user_name"]
        new_order = Order.make_order(item_name, price, order_date, user_name)
        if new_order == "Order Made Successfully":
            return jsonify({'message': new_order}), 201
        return jsonify({'message': new_order}), 409

    def put(self, order_id):
        if order_id:
            order_id = uuid.UUID(order_id)
            orders = Order.get_all_orders()
            for order in orders:
                if order_id == order['order_id']:
                    order['status'] = 'Completed'
                    return jsonify({'message': "Order Completed"}), 200
            return jsonify({'message': "Order Not Found "}), 404
