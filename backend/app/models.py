from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Expense(db.Model):
    __tablename__ = 'expenses'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    expense_list = db.Column(db.JSON, nullable=False)