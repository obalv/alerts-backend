from flask import jsonify,request,make_response,render_template
from flask_restful import Resource
from app import restful
from .models import AlertRecord
from app.api_1_0 import alert_frontend

@alert_frontend.route('/')
def alert_index():
	response=make_response(render_template('index.html'))
	return response

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
		json_record = request.get_json(force=True)
		AlertRecord.from_json(json_record['data'])
		return jsonify(json_record)

restful.add_resource(AlertNumber,'/')