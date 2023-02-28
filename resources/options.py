from flask_smorest import abort,Blueprint
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from resources.schemas import PlainOptionSchema,QuestionSchema, OptionSchema
from models import QuestionModel,OptionsModel
blp = Blueprint("options" , __name__ , description="Operation on options of questions")
from db import db
@blp.route("/question/<string:question_id>/option")
class Option(MethodView):
    @blp.arguments(PlainOptionSchema)
    @blp.response(200 , PlainOptionSchema)
    def post(self,option_data , question_id): #create an option in a question
        option = OptionsModel(question_id = question_id , **option_data)
        db.session.add(option)
        db.session.commit()
        return option

    @blp.response(200, OptionSchema(many=True))
    def get(self, question_id):
        question = QuestionModel.query.get_or_404(question_id)
        return question.options.all()

@blp.route('/question/<string:question_id>/options/<string:id>')
class OptionList(MethodView):
    @blp.response(200,PlainOptionSchema(many=True))
    def get(self,question_id,id):
        question = QuestionModel.query.get_or_404(question_id)
        return question.query.all()

@blp.route('/options/<string:id>')
class UpdateOption(MethodView):
    @blp.arguments(PlainOptionSchema)
    @blp.response(200, PlainOptionSchema)
    def put(self, option_data, id):
        option = OptionsModel.query.get_or_404(id)
        option.option = option_data['option']
        db.session.add(option)
        db.session.commit()
        return option
    def delete(self, id):
        option = OptionsModel.query.get_or_404(id)
        db.session.delete(option)
        db.session.commit()
        return {'message':'deleted successfully'}