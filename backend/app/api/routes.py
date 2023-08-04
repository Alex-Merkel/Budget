from flask import Blueprint, render_template, request, jsonify
from helpers import token_required
from models import db, Expense, expense_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/expenses', methods=['GET', 'POST'])
@token_required
def get_or_create_expenses(current_user_token):
    data = request.get_json()
    expense_list = data.get('expenses') or {
        'housing': 0,
        'transportation': 0,
        'groceries': 0,
        'utilities': 0,
        'healthcare': 0,
        'debt_payments': 0,
        'emergency_fund': 0,
        'retirement': 0,
        'vacation': 0,
        'entertainment': 0,
        'dining_out': 0,
        'hobbies': 0
    }
    income = data.get('totalIncome') or 0
    user_token = current_user_token.token

    print(f'Watermelon: {current_user_token.token} ')

    expense = Expense.query.filter_by(token=user_token).first()

    if not expense:
        # If no entry is found, create a new row with default values
        expense = Expense(expense_list=expense_list, income=income, token=user_token)
        db.session.add(expense)
        db.session.commit()

    else:
        # If an entry is found, update the expense_list and income
        expense.expense_list = expense_list
        expense.income = income
        db.session.commit()

    # Response to return, you can modify this according to your needs
    response = {
        "message": "Expense data saved successfully.",
        "expense_list": expense.expense_list,
        "income": expense.income
    }

    return jsonify(response), 201

@api.route('/expenses', methods=['GET', 'PUT'])
@token_required
def update_expenses(current_user_token):
    if not current_user_token:
        return jsonify({"message": "Token is missing or invalid."}), 401

    user_id = current_user_token.user_id

    expense = Expense.query.get(user_id)

    if not expense:
        return jsonify({"message": "Expense list not found."}), 404

    expense.expense_list = request.json['expense_list']
    expense.income = request.json['income']
    expense.user_token = current_user_token.token

    db.session.commit()
    response = expense_schema.dump(expense)
    return jsonify(response)


@api.route('/expenses', methods=['DELETE'])
def delete_expenses(current_user_token):
    expense = Expense.query.get(id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        response = expense_schema.dump(expense)
        return jsonify({'message': 'Expense list deleted'}), 200
    else:
        return jsonify({'message': 'Expense list not found'}), 404
