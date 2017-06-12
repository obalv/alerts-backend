from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import config

db=SQLAlchemy()
restful=Api(prefix='/api_1_0')

def create_app(config_name):
	app=Flask(__name__)
	app.config.from_object(config[config_name])

	db.init_app(app)
	restful.init_app(app)

	from .api_1_0 import alert_frontend
	app.register_blueprint(alert_frontend)
	return app