from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired


class RedactForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    info = StringField("Данные", validators=[DataRequired()])
    date = DateTimeField('Дата напоминания', validators=[DataRequired()])
    back = SubmitField('Назад')
    submit = SubmitField('Сохранить')
