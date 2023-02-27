from db import db

class OptionsModel(db.Model):
     __tablename__ = 'options'
     id = db.Column(db.Integer , primary_key = True)
     option = db.Column(db.String)
     question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
     questions = db.relationship("QuestionModel" , back_populates = "options")