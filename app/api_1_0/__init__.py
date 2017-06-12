from flask import Blueprint

alert_frontend = Blueprint('alert_forntend', __name__)

from .views import  *