from flask import Blueprint, render_template, request, jsonify
from helpers import token_required
from models import db, Expense, expense_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/checkexpenses', methods=['GET', 'POST'])
@token_required
def get_expenses(current_user_token):
    expense = Expense.query.filter_by(user_token=current_user_token.token).first()

    if expense:
        response = {
            "message": "Expense data saved successfully.",
            "expense_list": expense.expense_list,
            "needs": expense.needs,
            "savings": expense.savings,
            "wants": expense.wants,
            "income": expense.income,
            "total_expenses": expense.total_expenses,
            "surplus_deficit": expense.surplus_deficit
        }
    else:
        response = "User and/or data not found"

    return jsonify(response), 200


@api.route('/createexpenses', methods=['GET', 'POST'])
@token_required
def create_expenses(current_user_token):
    # Default expenses if no data in db for user
    expense_list = {
        'housing': 0.00,
        'transportation': 0.00,
        'groceries': 0.00,
        'utilities': 0.00,
        'healthcare': 0.00,
        'debt payments': 0.00,
        'emergency fund': 0.00,
        'retirement': 0.00,
        'vacation': 0.00,
        'entertainment': 0.00,
        'dining out': 0.00,
        'hobbies': 0.00
    }
    needs = [
        'housing',
        'transportation',
        'groceries',
        'utilities',
        'healthcare',
        'debt payments'
    ]
    savings = [
        'emergency fund',
        'retirement',
        'vacation'
    ]
    wants = [
        'entertainment',
        'dining out',
        'hobbies'
    ]
    income = 0.00
    total_expenses = 0.00
    surplus_deficit = 0.00
    user_token = current_user_token.token

    expense = Expense(
        expense_list = expense_list,
        needs = needs,
        savings = savings,
        wants = wants,
        income = income,
        total_expenses = total_expenses,
        surplus_deficit = surplus_deficit,
        user_token = user_token
    )
    
    db.session.add(expense)
    db.session.commit()

    response = "Data not created, please try again"


    return jsonify(response), 201


@api.route('/updateexpenses', methods=['GET', 'PUT'])
@token_required
def update_expenses(current_user_token):
    if not current_user_token:
        return jsonify({"message": "Token is missing or invalid."}), 401

    user_token = current_user_token.token

    expense = Expense.query.filter_by(user_token=user_token).first()

    if not expense:
        return jsonify({"message": "Expense list not found."}), 404
    
    expense_name = request.json.get('expense_name')
    expense_value = request.json.get('expense_value')

    if expense_name and expense_value:
        # Update the expense_list with the custom expense
        expense.expense_list[expense_name] = expense_value

    # Determine what category possible user added / custom expense needs to go to
    category = request.json.get('category')
    if category == 'needs':
        expense.needs.append(expense_name)
    elif category == 'savings':
        expense.savings.append(expense_name)
    elif category == 'wants':
        expense.wants.append(expense_name)    

    expense.expense_list = request.json['expense_list']
    expense.needs = request.json['needs']
    expense.savings = request.json['savings']
    expense.wants = request.json['wants']
    expense.income = request.json['income']
    expense.total_expenses = request.json['total_expenses']
    expense.surplus_deficit = request.json['surplus_deficit']
    expense.user_token = current_user_token.token

    db.session.commit()
    response = expense_schema.dump(expense)
    return jsonify(response)
