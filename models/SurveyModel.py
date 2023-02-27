from db import  db

class SurveyModel(db.Model):
    __tablename__ = "surveys"
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String , unique=True , nullable=False)
    description = db.Column(db.String ,unique=True ,nullable=False)
    questions = db.relationship("QuestionModel", back_populates="survey" )