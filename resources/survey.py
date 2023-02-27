from flask_smorest import abort,Blueprint
from flask.views import MethodView
from resources.schemas import PlainSurveySchema,SurveySchema
from models import SurveyModel,QuestionModel
from db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("survey",__name__,description="Operations on survey")
@blp.route("/survey/<string:id>")
class Survey(MethodView):
    @blp.response(200, SurveySchema)
    def get(self,id):
        return SurveyModel.query.get_or_404(id)

    @blp.arguments(PlainSurveySchema)
    @blp.response(200, SurveySchema)
    def put(self, survey_data , id):
        survey = SurveyModel.query.get_or_404(id)
        if 'title' in survey_data:
            survey.title = survey_data['title']
        if 'description' in survey_data:
            survey.description = survey_data['description']
        db.session.add(survey)
        db.session.commit()
        return survey

    def delete(self,id):
        survey = SurveyModel.query.get_or_404(id)
        db.session.delete(survey)
        db.session.commit()

@blp.route('/survey')
class SurveyList(MethodView):
    @blp.response(200, SurveySchema(many=True))
    def get(self):
        return SurveyModel.query.all()
    @blp.arguments(SurveySchema)
    @blp.response(201,SurveySchema)
    def post(self,survey_data):
        question_list = None
        if 'questions' in survey_data:
            question_list = survey_data.pop('questions')

        survey = SurveyModel(**survey_data)
        try:
            db.session.add(survey)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500 , message= str(e))
        if question_list:
            for question in question_list:
                question_object = QuestionModel(survey_id = survey.id , **question)
                db.session.add(question_object)
                db.session.commit()
        return survey


