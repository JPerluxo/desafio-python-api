from flask import Flask, Blueprint
from api.views import health

from api.despesas import Listardespesas, Cadastrardespesa

def create_app():
    api = Blueprint('api', __name__)
    app = Flask(__name__)

    # define api routes
    api.add_url_rule('/status', 'health', view_func=health, methods=['GET'])

    api.add_url_rule('/despesas', 'Listardespesas', view_func=Listardespesas, methods=['GET'])
    api.add_url_rule('/despesas', 'Cadastrardespesa', view_func=Cadastrardespesa, methods=['POST'])
    

    app.register_blueprint(api, url_prefix='/api')
    return app