import dash
from flask import Flask
from flask.helpers import get_root_path
from app.dashapp1.complete_app import my_layout
from app.dashapp2.complete_app import my_layout as second_layout

class BaseConfig:
    SECRET_KEY = 'asdkljdl'


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashapps(server)
    register_blueprints(server)

    return server


def register_dashapps(app):

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp1 = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/dashboard/',
                         assets_folder='C:/Users/jlomb/Documents/PersonalProjects/dash_debugging/app/dashapp1/assets/',
                         meta_tags=[meta_viewport])

    dashapp2 = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/dashboard_two/',
                         assets_folder='C:/Users/jlomb/Documents/PersonalProjects/dash_debugging/app/dashapp2/assets/',
                         meta_tags=[meta_viewport])

    with app.app_context():
        dashapp1.title = 'Dashapp 1'
        dashapp1.layout = my_layout

        dashapp2.title = 'Dashapp 2'
        dashapp2.layout = second_layout
        # register_callbacks(dashapp1)


def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp)