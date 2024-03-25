from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Optional


class RedactForm(FlaskForm):
    info = StringField("Данные", validators=[DataRequired()])
    date = DateTimeField('Дата напоминания', validators=[Optional()])
    submit = SubmitField('Сохранить')
