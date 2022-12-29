from app import create_app
from werkzeug import run_simple
server = create_app()

if __name__ == '__main__':

    run_simple('localhost',8050, server, use_debugger=True, use_reloader=True)

# from flask import Flask, redirect, session, request, make_response
# import dash
# from werkzeug import run_simple
# from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from dash_apps.src.dash_app_one import create_app1
# import random

# server = Flask(__name__)
# server.secret_key = 'superkey'

# my_app = create_app1(server, True) ##Works but not what we want
# @server.route('/')
# def home():

#     sid = request.cookies.get('sid')

#     if sid:
#         return '<p> Hello, world </p>'

#     return '<p> not ofund </p>'

# SID_Check = True

# @server.route('/mydashboard/')
# def return_dash():

#     response = make_response(my_app.index())
#     response.set_cookie('SID',random.randint(0,10))
#     return response

# # @server.route('/mydashboard')
# # def return_dash():
   
# #     my_app = create_app1(server, SID_Check)

# #     sid = request.cookies.get('sid')

# #     if sid:
# #         return '<p> hello, world </p>'

# #     else:
# #         resp = make_response(redirect('/'))
# #         resp.set_cookie('sid','weee')

# #     return my_app.index()
   
# # application = DispatcherMiddleware(server,{
# #     '/dash1': my_app.server
# # })
   
# if __name__ == '__main__':

#     run_simple('localhost',8050, server, use_debugger=True, use_reloader=True)