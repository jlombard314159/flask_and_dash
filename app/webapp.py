from flask import (Blueprint, render_template, make_response)

server_bp = Blueprint('main', __name__)

def get_sid_cookie():

    # SID = request.cookies.get('SID')
    SID = '12413'

    if SID:
        return SID
    else:
        return None

# def store_sid(SID:str):
#     session[]

@server_bp.route('/generate_SID')
def index():
    SID = get_sid_cookie()

    resp = make_response('<p> wee </p>')
    resp.set_cookie(SID)

    return resp

