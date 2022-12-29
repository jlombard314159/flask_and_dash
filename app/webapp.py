from flask import (Blueprint, render_template)

server_bp = Blueprint('main', __name__)


@server_bp.route('/')
def index():
    return '<p> wee </p>'

