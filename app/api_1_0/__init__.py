from flask import Blueprint

API_1_0 = Blueprint('api_1_0', __name__)

from .views import  *