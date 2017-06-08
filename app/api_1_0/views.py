from flask import jsonify,request
from flask_restful import Resource
from app import restful
from .models import AlertRecord

class AlertNumber(Resource):
	def get(self):
		record_blue=AlertRecord.query.filter_by(color='blue').all()
		record_yellow= AlertRecord.query.filter_by(color='yellow').all()
		record_orange= AlertRecord.query.filter_by(color='orange').all()
		record_red= AlertRecord.query.filter_by(color='red').all()
		return jsonify(
			{
				'blue':[b.to_json() for b in record_blue],
				'yellow':[y.to_json() for y in record_yellow],
				'orange':[o.to_json() for o in record_orange],
				'red':[r.to_json() for r in record_red]
			}
		)
	def post(self):
		AlertRecord.from_json(request.json().data)
		return jsonify({
			'status':'ok',
			'msg':'ok'
		})

restful.add_resource(AlertNumber,'/')