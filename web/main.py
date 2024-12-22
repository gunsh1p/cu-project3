from flask import Flask
from flask_bootstrap import Bootstrap

from api import bp as api_bp
from route_creator import bp as route_bp
from dashapps import bp as dashes_bp, ad1
import config

bootstrap = Bootstrap()

def register_bps(app: Flask) -> None:
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(route_bp)
    app.register_blueprint(dashes_bp)

def add_dashes(app: Flask) -> Flask:
    app = ad1(app)
    return app

def create_app() -> Flask:
    app = Flask(__name__)

    bootstrap.init_app(app)

    register_bps(app)
    app = add_dashes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
