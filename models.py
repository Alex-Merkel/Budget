from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String, nullable=True, default='')
    g_auth_verify = db.Column(db.Boolean, default=False)
    token = db.Column(db.String, default='', unique=True)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return self.token
    



class Expense(db.Model):
    __tablename__ = 'expenses'
    user_id = db.Column(db.String, primary_key=True)
    expense_list = db.Column(db.JSON, nullable=False)
    needs = db.Column(db.JSON, nullable=False)
    savings = db.Column(db.JSON, nullable=False)
    wants = db.Column(db.JSON, nullable=False)
    income = db.Column(db.Float, default=0.00, nullable=False)
    total_expenses = db.Column(db.Float, default=0.00, nullable=False)
    surplus_deficit = db.Column(db.Float, default=0.00, nullable=False)
    user_token = db.Column(db.String, db.ForeignKey('users.token'), nullable=False)

    def __init__(self, expense_list, needs, savings, wants, income, total_expenses, surplus_deficit, user_token, user_id=''):
        self.user_id = self.set_id()
        self.expense_list = expense_list
        self.needs = needs
        self.savings = savings
        self.wants = wants
        self.income = income
        self.total_expenses = total_expenses
        self.surplus_deficit = surplus_deficit
        self.user_token = user_token


    def __repr__(self):
        return 'The budget data has been added to the database.'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    

class ExpenseSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'expense_list', 'needs', 'savings', 'wants', 'income', 'total_expenses', 'surplus_deficit']

expense_schema = ExpenseSchema()
    