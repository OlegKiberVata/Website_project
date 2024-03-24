from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    info = StringField("Данные", validators=[DataRequired()])
    date = DateTimeField('Дата напоминания', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
