from flask import Flask, request, render_template, session, redirect, url_for
from sqlalchemy import desc
from utility import is_valid_phone
from models import db, User, PhoneNumber, Comment
import datetime

app = Flask(__name__)
app.secret_key = 'secretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///telefono_numeriai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')
        network = request.form.get('network')

        if phone.startswith('+370') and len(phone) == 12 and phone[4:].isdigit():
            user = User.query.filter_by(phone=phone).first()

            if user:
                if user.password == password:
                    session['user_id'] = user.id
                    return redirect(url_for('valid_number'))
                else:
                    message = 'Neteisingas slaptažodis.'
            else:
                new_user = User(phone=phone, password=password, is_confirmed=True, network=network)
                db.session.add(new_user)
                db.session.commit()
                session['user_id'] = new_user.id
                return redirect(url_for('valid_number'))
        else:
            message = 'Netinkamas telefono numerio formatas.'

    return render_template('login.html', message=message)


@app.route('/', methods=['GET', 'POST'])
def valid_number():
    result = None
    check_count = 0
    phone = None

    if request.method == 'POST':
        phone = request.form.get('phone')
        if is_valid_phone(phone):
            number = PhoneNumber.query.filter_by(number=phone).first()
            if number:
                number.check_count += 1
                db.session.commit()
            else:
                number = PhoneNumber(number=phone, valid=True, check_count=0)
                db.session.add(number)
                db.session.commit()
            check_count = number.check_count
            result = f"Tinkamas numerio formatas. {phone} jau tikrintas {check_count} kartą/-us."
        else:
            result = 'Netinkamas numerio formatas - turi prasidėti +370 ir po to 8 skaičiai.'

    return render_template('index.html', result=result, phone=phone, check_count=check_count)


@app.route('/numbers')
def numbers():
    numbers = PhoneNumber.query.filter_by(valid=True).order_by(desc(PhoneNumber.id)).all()
    return render_template('numbers.html', numbers=numbers)


@app.route('/number/<int:number_id>', methods=['GET', 'POST'])
def number_detail(number_id):
    number = PhoneNumber.query.get(number_id)
    user_id = session.get('user_id')
    user = User.query.get(user_id) if user_id else None

    if request.method == 'POST':
        content = request.form.get('content')

        if content and content.strip():
            comment = Comment(
                content=content.strip(),
                user_id=user_id,
                phone_number_id=number.id,
                timestamp=datetime.datetime.now()
            )
            db.session.add(comment)
            db.session.commit()
        else:
            return 'Komentaras negali būti tuščias.'

        return redirect(url_for('number_detail', number_id=number.id))

    comments = number.comments
    comments = sorted(comments, key=lambda c: c.timestamp, reverse=False)
    return render_template('number_detail.html', number=number, comments=comments, user=user)


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
