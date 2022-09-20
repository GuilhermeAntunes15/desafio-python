from flask import Flask, Blueprint, request, Response
from api.views import health
from api import crud
from datetime import datetime

def create_app():
    api = Blueprint('api', __name__)
    app = Flask(__name__)

    crd = crud.Crud()

    # define api routes
    api.add_url_rule('/status', 'health', view_func=health, methods=['GET'])

    api.add_url_rule('/despesas', 'list', view_func=crd.list, methods=['GET'])

    # api.add_url_rule('/despesas', 'insert', view_func=crd.insert, methods=['POST'])

    app.register_blueprint(api, url_prefix='/api')

    @app.route('/api/despesas', methods=['POST'])
    def add_task():
        try:
            request_data = request.get_json()
            crd.insert(request_data["valor"], request_data["data"], request_data["descricao"], request_data["tipo_pagamento"], request_data["categoria"])
            return {
                    'data': None, 
                    "success": True
                    }
        except:
            return {
                    'data': None, 
                    "success": False
                    }
    return app