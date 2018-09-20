"""This module contains classes order and its method"""
import uuid
from datetime import datetime
food_orders = []



class Order:
    ''' A orders class'''

    def __init__(self, order_id, name, price, order_date):
        self.order_id = order_id
        self.name = name
        self.price = price
        self.order_date = order_date

    @classmethod
    def existing_order(cls, name, price, order_date):
        """A method to check if the same order already exists """
        for order in food_orders:
            if order['name'] == name and order['price'] == \
                    price and order['order_date'] == order_date:
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
    def make_order(cls, name, price, order_date):
        """A method for making a order"""
        cls.data = {}
        if cls.existing_order(name, price, order_date):
            return "Order Already Exists"
        else:
            if not cls.valid_date(order_date):
                return "Invalid Date"
            else:
                cls.data['order_id'] = uuid.uuid1()
                cls.data['name'] = name
                cls.data['price'] = price
                cls.data["order_date"] = order_date
                food_orders.append(cls.data)
                return "Order Made Successfully"

    @classmethod
    def view_all_orders(cls):
        """ Return all the food_orders"""
        return food_orders