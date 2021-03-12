from db import db
import time


class UserModel(db.Model):
    __tablename__ = "utenti"

    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(140))
    creation_date = db.Column(db.String(30))
    confirmed = db.Column(db.Boolean)
    password_change_date = db.Column(db.Integer)

    def __init__(self, id, mail, username, password):
        self.id = id
        self.mail = mail
        self.username = username
        self.password = password
        self.creation_date = time.time()
        self.confirmed = False
        self.password_change = time.time()

    @classmethod
    def find_by_id(cls, id):
        return UserModel.query.filter_by(id=id).first()

    @classmethod
    def find_by_mail(cls, mail):
        return UserModel.query.filter_by(mail=mail).first()

    @classmethod
    def find_all(self):
        return UserModel.query.filter_by()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def change_password(self, password):
        self.password = password
        self.password_change_date = time.time()

    def change_username(self, username):
        self.username = username
