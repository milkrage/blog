from flask import Flask
from .password.views import password


def create_app():
    app = Flask(__name__)
    app.register_blueprint(password)

    @app.route('/ping')
    def ping():
        return 'pong'

    return app
