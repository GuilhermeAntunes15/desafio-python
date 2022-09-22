from flask import json, jsonify, request, Response
from api import crud

def health():
    """
    Status da API
    """
    responseBody = {
        "status": "Service Running"
    }
    return jsonify(responseBody)


def add_task():
    try:
        crd = crud.Crud()
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
    
def list():
    try:
        crd = crud.Crud()
        dados = crd.list()
        return {
                'data': dados, 
                "success": True
                }
    except:
        return {
                'data': None, 
                "success": False
                }