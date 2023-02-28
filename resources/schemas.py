from marshmallow import fields,Schema

class PlainSurveySchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
class PlainQuestionSchema(Schema):
    id = fields.String(dump_only=True)
    description = fields.String(required=True)
    answer = fields.String()
class PlainOptionSchema(Schema):
    id = fields.Integer(dump_only=True)
    option = fields.String(required=True)
class QuestionSchema(PlainQuestionSchema):
    #survey_id = fields.Integer(required=True)
    #survey = fields.Nested(PlainSurveySchema(), dump_only=True)
    options = fields.List(fields.Nested(PlainOptionSchema()))
class SurveySchema(PlainSurveySchema):
    questions = fields.List(fields.Nested(QuestionSchema()))

class OptionSchema(PlainOptionSchema):
    options = fields.List(fields.Nested(PlainOptionSchema()))