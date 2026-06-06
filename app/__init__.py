from flask import Flask
from .extensions import mail
from .routes.home import home_bp
from .routes.services import services_bp
from .routes.portfolio import portfolio_bp
from .routes.contact import contact_bp
from .routes.consulting import consulting_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    mail.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(consulting_bp)

    return app
