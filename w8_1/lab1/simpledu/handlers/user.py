from flask import Blueprint, render_template
from simpledu.models import db, Course, User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<user_name>')
def user(user_name):
    return render_template("user.html", user=User.query.filter_by(username=user_name).first_or_404())