from app import app, db
from models import User, PhoneNumber, Comment

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(phone='+37060000001', password='12345', is_confirmed=True, network='Telia')
    user2 = User(phone='+37060000002', password='12345', is_confirmed=True, network='Tele2')
    user3 = User(phone='+37060000005', password='12345', is_confirmed=True, network='Kitas')

    number1 = PhoneNumber(number='+37061234567', valid=True, check_count=3)
    number2 = PhoneNumber(number='+37069876543', valid=True, check_count=5)

    comment1 = Comment(content='Puikus numeris!', user=user1, phone_number=number1)
    comment2 = Comment(content='Čia mano senas numeris.', user=user2, phone_number=number1)
    comment3 = Comment(content='Tikrinau keletą kartų.', user=user1, phone_number=number2)
    comment4 = Comment(content='Komentaras.', user=user3, phone_number=number2)

    db.session.add_all([user1, user2, user3, number1, number2, comment1, comment2, comment3, comment4])
    db.session.commit()
