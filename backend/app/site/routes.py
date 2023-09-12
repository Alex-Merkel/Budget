from flask import Blueprint, render_template, request, session, redirect, url_for, current_app, jsonify
from models import db, User, Expense
import requests
from flask_login import current_user

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def index():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/budget')
def budget():
        return render_template('budget.html')