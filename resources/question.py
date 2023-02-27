from flask_smorest import abort,Blueprint
from flask.views import MethodView
from resources.schemas import QuestionSchema , PlainQuestionSchema
from models import QuestionModel
from db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint('questions' , __name__ , description="Operations on survey questions")
@blp.route("/survey/<string:survey_id>/question")
class Questions(MethodView):
    @blp.arguments(PlainQuestionSchema)
    @blp.response(201, QuestionSchema)
    def post(self,question_data , survey_id):
        try:
            question = QuestionModel(survey_id = survey_id , **question_data)
            db.session.add(question)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message = str(e))
        return question

    @blp.response(200 , QuestionSchema(many=True))
    def get(self,survey_id):
        return QuestionModel.query.all()

@blp.route("/survey/<string:survey_id>/question/<string:id>")
class QuestionList(MethodView):
    @blp.arguments(QuestionSchema)
    @blp.response(202, QuestionSchema)
    def put(self, question_data ,survey_id ,id):
        question = QuestionModel.query.get(id)
        if question:
            question.id = id
            question.description = question_data['description']
            question.answer = question_data['answer']
        else:
            question = QuestionModel(id = id, survey_id = survey_id,**question_data)
        try:
            db.session.add(question)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500 , message = str(e))
        return question
@blp.route("/question/<string:id>")
class QuestionDelete(MethodView):
    def delete(self,id):
        quesiotn = QuestionModel.query.get_or_404(id)
        db.session.delete(quesiotn)
        db.session.commit()
        return {'message' : 'question deleted successfully'}