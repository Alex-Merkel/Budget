from flask import Blueprint, render_template, request, jsonify
from helpers import token_required
from models import db, Expense, expense_schema
import uuid

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/checkexpenses', methods=['GET', 'POST'])
@token_required
def get_expenses(current_user_token):
    token = request.headers.get('x-access-token')
    print(token)
    expense = Expense.query.filter_by(user_token=token).first()

    if expense:
        response = {
            "message": "Expense data saved successfully.",
            "expense_list": expense.expense_list,
            "income": expense.income
        }
    else:
        response = "User and/or data not found"

    return jsonify(response), 200


@api.route('/createexpenses', methods=['GET', 'POST'])
@token_required
def create_expenses(current_user_token):
    # print('Helo')
    # print(current_user_token)
    # print(request.data)
    # print(request.headers)
    # expense = request.json
    # print(expense)

    
    expense_list = {
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
    income = 0
    user_token = current_user_token

    expense = Expense(
        user_id = str(uuid.uuid4()),
        expense_list = expense_list,
        income = income,
        user_token = user_token
    )
    
    # print(expense)

    db.session.add(expense)
    db.session.commit()

    response = "Data not created, please try again"

    


    return jsonify(response), 201


@api.route('/updateexpenses', methods=['GET', 'PUT'])
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


@api.route('/deleteexpenses', methods=['DELETE'])
def delete_expenses(current_user_token):
    expense = Expense.query.get(id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        response = expense_schema.dump(expense)
        return jsonify({'message': 'Expense list deleted'}), 200
    else:
        return jsonify({'message': 'Expense list not found'}), 404
