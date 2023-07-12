from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Expense(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    expense_list = db.Column(db.JSON, nullable=False)