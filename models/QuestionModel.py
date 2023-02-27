from db import db
class QuestionModel(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey("surveys.id"),unique=False, nullable=False)
    description = db.Column(db.String ,unique=False ,nullable=False)
    answer = db.Column(db.String , unique=False)
    survey = db.relationship("SurveyModel" , back_populates="questions")
    options = db.relationship("OptionsModel" , back_populates = "questions")