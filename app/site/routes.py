from flask import Blueprint, render_template
import requests
from flask_login import current_user, login_required

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def index():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@site.route('/budget')
@login_required
def budget():
        return render_template('budget.html')