"""This module contains classes order and its method"""
import uuid
from datetime import datetime
food_orders = []


class Order:
    def __init__(self, order_id, item_name, price, order_date, user_name,
                 status):
        self.order_id = order_id
        self.item_name = item_name
        self.price = price
        self.order_date = order_date
        self.user_name = user_name

    @classmethod
    def existing_order(cls, item_name, price, order_date, user_name):
        """A method to check if the same order already exists """
        for order in food_orders:
            if order['item_name'] == item_name and order['price'] == \
                    price and order['order_date'] == order_date and \
                    order['user_name'] == user_name:
                return True
        return False

    @classmethod
    def valid_date(cls, order_date):
        """Check if the given date is less than the current date"""
        try:
            order_date = datetime.strptime(order_date, '%Y-%m-%d').date()
        except ValueError:
            return "Invalid Date Format"
        if order_date <= order_date.today():
            return False
        return True

    @classmethod
    def make_order(cls, item_name, price, order_date, user_name):
        """A method for making a order"""
        cls.data = {}
        if cls.existing_order(item_name, price, order_date, user_name):
            return "Order Already Exists"
        else:
            if not cls.valid_date(order_date):
                return "Invalid Date"
            else:
                cls.data['order_id'] = uuid.uuid1()
                cls.data['item_name'] = item_name
                cls.data['price'] = price
                cls.data["order_date"] = order_date
                cls.data["status"] = 'Pending'
                cls.data["user_name"] = user_name
                food_orders.append(cls.data)
                return "Order Made Successfully"

    @classmethod
    def get_all_orders(cls):
        """ Return all the food_orders"""
        return food_orders
