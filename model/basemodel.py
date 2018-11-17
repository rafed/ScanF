from app import db 

class BaseModel():
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}