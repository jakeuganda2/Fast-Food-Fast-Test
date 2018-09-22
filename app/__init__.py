from flask import Flask, jsonify
from config import configuration

app = Flask(__name__)


def create_app(configuration_name):
    '''Creates the app and registers Blue prints'''
    app.config.from_object(configuration[configuration_name])
    from app.order.views import ORDER_APP
    app.register_blueprint(ORDER_APP)
    return app
