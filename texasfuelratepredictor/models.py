from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from texasfuelratepredictor import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') 
    password = db.Column(db.String(60), nullable=False)
    order = db.relationship('Quote', backref='client', lazy=True)
    background = db.relationship('ClientInformation', backref='register', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    # magic method
    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"

class ClientInformation(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    address1 = db.Column(db.String(100), nullable=False)
    address2 = db.Column(db.String(100))
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    client = db.Column(db.Integer, db.ForeignKey('user.email'), nullable=False)

     # magic method
    def __repr__(self):
        return f"ClientInformation('{self.fullname}','{self.address1}', '{self.address2}', '{self.city}','{self.state}', '{self.zipcode}')"


class Quote(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    gallon = db.Column(db.Integer)
    address= db.Column(db.String(100), unique=True, nullable=False, default='')
    datedelivery = db.Column(db.Date, nullable=False) 
    datepost = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    suggested_price = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    client_em = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)



    # magic method
    def __repr__(self):
        return f"Quote('{self.gallon}','{self.address}', '{self.datedelivery}', '{self.total_price}','{self.client_name}')"
