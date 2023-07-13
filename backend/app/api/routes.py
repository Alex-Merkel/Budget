from flask import Blueprint, render_template, request, jsonify
from app.models import Expense
from app import db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/expenses', methods=['POST'])
def create_expenses():
    data = request.get_json()

    # Set default expense items (name of expense and value at 0)
    default_expenses = {
        'Housing': 0,
        'Transportation': 0,
        'Groceries': 0,
        'Utilities': 0,
        'Healthcare': 0,
        'Debt Payments': 0,
        'Emergency Fund': 0,
        'Retirement': 0,
        'Vacation': 0,
        'Entertainment': 0,
        'Dining Out': 0,
        'Hobbies': 0
    }

    expense_list = {**default_expenses, **data}

    expense = Expense(expense_list=expense_list)

    db.session.add(expense)
    db.session.commit()

    return jsonify(expense_list), 201

@api.route('/expenses', methods=['GET'])
def get_expenses():
    expense = Expense.query.first()
    if expense:
        expense_list = expense.expense_list
        return jsonify(expense_list), 200
    else:
        return jsonify({'message': 'Expense list not found'}), 404

@api.route('/expenses', methods=['PUT'])
def update_expenses():
    data = request.get_json()

    expense = Expense.query.first()
    if expense:
        expense.expense_list.update(data)
        db.session.commit()
        return jsonify(expense.expense_list), 200
    else:
        return jsonify({'message': 'Expense list not found'}), 404

@api.route('/expenses', methods=['DELETE'])
def delete_expenses():
    expense = Expense.query.first()
    if expense:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'message': 'Expense list deleted'}), 200
    else:
        return jsonify({'message': 'Expense list not found'}), 404
