from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Optional


class CreateForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    info = StringField("Данные", validators=[DataRequired()])
    date = DateTimeField('Дата напоминания', validators=[Optional()])
    submit = SubmitField('Сохранить')
