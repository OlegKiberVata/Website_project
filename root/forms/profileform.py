from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class ChangeProfileForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField("Фамилия", validators=[DataRequired()])
    gender = StringField('Пол', validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    phone_number = StringField("Номер телефона")
    submit = SubmitField('Сохранить')
