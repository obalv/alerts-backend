from app import db

class AlertRecord(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.Text)
	color=db.Column(db.Text)
	number=db.Column(db.Integer,default=0)

	def to_json(self):
		json_recor={
			'name':self.name,
			'number':self.number
		}
		return json_recor

	@staticmethod
	def from_json(number_state):
		i=0
		while i<8:
			select_new_record=number_state[i]
			select_old_record=AlertRecord.query.filter_by(name=select_new_record['name'])
			select_old_blue_record=select_old_record.filter_by(color='blue').first()
			select_old_yellow_record=select_old_record.filter_by(color='yellow').first()
			select_old_orange_record=select_old_record.filter_by(color='orange').first()
			select_old_red_record=select_old_record.filter_by(color='red').first()
			select_old_blue_record.number=select_new_record['blue']
			select_old_yellow_record.number=select_new_record['yellow']
			select_old_orange_record.number=select_new_record['orange']
			select_old_red_record.number=select_new_record['red']
			db.session.add_all([select_old_blue_record,select_old_yellow_record,
			                    select_old_orange_record,select_old_red_record])
			db.session.commit()
			i+=1