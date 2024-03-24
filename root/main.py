from flask import Flask, render_template, redirect
from root.forms.registratform import RegistrForm
from root.forms.profileform import ChangeProfileForm
from root.forms.enterform import EnterForm
from root.forms.redact_form import RedactForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
persons = {}


@app.route('/home/<person>')
def home_page(person):
    global persons
    return render_template('home.html', title='Главная страница', person=persons[person])


@app.route("/profile/<person>")
def profile(person):
    global persons
    return render_template('profile.html', title='Профиль', profile=persons[person][3])


@app.route("/note/<person>/<choosen_note>")
def note(person, choosen_note):
    global persons
    return render_template('note.html', title="Просмотр записи", note=persons[person][2][choosen_note])


@app.route("/profile_change/<person>")
def change(person):
    global persons
    form = ChangeProfileForm()
    if form.validate_on_submit() and form.submit:
        persons[person][3] = [form.name.data, form.surname.data, form.email.data,
                              form.password.data, form.gender.data, form.phone_number.data, form.age.data]
        # apply_data(persons[person]), передаю тебе штуки, чтобы занес в базу данных
        return redirect(f'/home/{person}')
    if form.back:
        return redirect(f'/home/{person}')
    return render_template('change_prof.html', title="Смена данных пользователя", person=persons[person])


@app.route("/redact_note/<person>/<note>")
def redact(person, note):
    global persons
    form = RedactForm()
    if form.validate_on_submit() and form.submit:
        persons[person][3] = [form.name.data, form.info.data, form.date.data]
        # apply_data(persons[person]), передаю тебе штуки, чтобы занес в базу данных
        return redirect(f'/home/{person}')
    if form.back:
        return redirect(f'/home/{person}')
    return render_template('redact_note.html', title="Редактирование записи", person=person, note=note)


@app.route('/registration', methods=['GET', 'POST'])  # регистрация
def registration():
    global persons
    form = RegistrForm()
    if form.validate_on_submit():  # and Check_registr([form.login.data, form.email.data, form.password.data]):, я передаю данные, ты проверяешь свободны ли они
        persons[form.login.data] = [form.password.data, form.email.data, {}, []]  # Сохраняем данные пользователя в таком порядке: пароль, почта, записи, штуки для профиля
        # apply_data(persons[form.login.data]), передаю тебе штуки, чтобы занес в базу данных
        return redirect('/enter')
    return render_template('registration.html', form=form, title='Регистрация')


@app.route('/enter', methods=['GET', 'POST'])  # вход
def login():
    global persons
    form = EnterForm()
    if form.validate_on_submit():  # and Check_enter([form.login.data, form.password.data]):, я передаю данные, ты проверяешь соотвествие и наличие их
        return redirect(f'/home/{persons[form.login.data]}')
    return render_template('enter.html', form=form, title='Вход')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
