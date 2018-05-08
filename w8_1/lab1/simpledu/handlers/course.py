from flask import Blueprint, render_template

course = Blueprint('course', __name__, url_prefix='/courses')
