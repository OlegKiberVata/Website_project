from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    email = StringField("Почта", validators=[DataRequired()])
    password = StringField('Придумайте пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')
