from flask import json
from test_data import*
from test_base import TestBase


class TestOrder(TestBase):

    def test_order_creation(self):
        """Test API can create a order (POST request)"""
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_order1))
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order Made Successfully', str(response.data))

    def test_order_creation_given_past_order(self):
        """Test if a order can be created with a past order"""
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(past_order_date))
        self.assertIn("Invalid Date", str(response.data))

    def test_duplicate_order_creation(self):
        self.client.post('api/v1/orders/',
                         content_type='application/json',
                         data=json.dumps(duplicate_order))
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(duplicate_order))
        self.assertIn("Order Already Exists", str(response.data))

    def test_get_all_orders(self):
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_order2))
        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/orders/')
        self.assertEqual(response.status_code, 200)

    def test_get_order_by_id(self):
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_order3))
        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/orders/')
        self.assertEqual(response.status_code, 200)
        results = json.loads(response.data.decode())
        for order in results:
            result = self.client.get('api/v1/orders/{}'
                                     .format(order['order_id']))
            self.assertEqual(result.status_code, 200)
            self.assertIn(order['order_id'], str(result.data))
