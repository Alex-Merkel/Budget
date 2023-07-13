from flask import Blueprint, render_template, request, session, redirect, url_for, current_app
import requests

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def index():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/budget', methods=['GET', 'POST'])
def budget():
    if request.method == 'POST':
        housing_expense = request.form.get('housing')
        transportation_expense = request.form.get('transportation')
        groceries_expense = request.form.get('groceries')
        utilities_expense = request.form.get('utilities')
        healthcare_expense = request.form.get('healthcare')
        debt_payments_expense = request.form.get('debt_payments')
        emergency_fund_expense = request.form.get('emergency_fund')
        retirement_expense = request.form.get('retirement')
        vacation_expense = request.form.get('vacation')
        entertainment_expense = request.form.get('entertainment')
        dining_out_expense = request.form.get('dining_out')
        hobbies_expense = request.form.get('hobbies')


        expense_data = {
            'housing': housing_expense,
            'transportation': transportation_expense,
            'groceries': groceries_expense,
            'utilities': utilities_expense,
            'healthcare': healthcare_expense,
            'debt_payments': debt_payments_expense,
            'emergency_fund': emergency_fund_expense,
            'retirement': retirement_expense,
            'vacation': vacation_expense,
            'entertainment': entertainment_expense,
            'dining_out': dining_out_expense,
            'hobbies': hobbies_expense
        }
        
        api_url = f"{current_app.config['DATABASE_URI']}/api/expenses"
        response = requests.post(api_url, json=expense_data)

        if response.status_code == 200:
            return redirect(url_for('site.budget'))
        else:
            return render_template('error.html', error_message='Failed to save expense data')

    return render_template('budget.html')