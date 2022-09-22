from flask import Flask, Blueprint
from api.views import health, add_task, list
from datetime import datetime

def create_app():
    api = Blueprint('api', __name__)
    app = Flask(__name__)

    # define api routes
    api.add_url_rule('/status', 'health', view_func=health, methods=['GET'])

    api.add_url_rule('/despesas', 'list', view_func=list, methods=['GET'])

    api.add_url_rule('/despesas', 'add_task', view_func=add_task, methods=['POST'])

    app.register_blueprint(api, url_prefix='/api')

    
    return app