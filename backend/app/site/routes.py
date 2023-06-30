from flask import Blueprint, render_template, request, session

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
        other_expense = request.form.get('other')
        
        



        session['housing_expense'] = housing_expense
    return render_template('budget.html')