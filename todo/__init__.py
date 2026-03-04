from flask import Flask
from todo.views.routes import register_routes

app = Flask(__name__)
register_routes(app)