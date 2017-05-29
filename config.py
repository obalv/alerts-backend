import os

basedir=os.path.abspath(os.path.dirname(__name__))

class Config:
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG=True
	SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'dev.sqlite')
	SQLALCHEMY_TRACK_MODIFICATIONS=False

class TestingConfig(Config):
	TESTING=True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'workshop.sqlite')

config={
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionConfig,
	'default':DevelopmentConfig
}