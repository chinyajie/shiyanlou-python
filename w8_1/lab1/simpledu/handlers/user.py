from flask import Blueprint, render_template
from simpledu.models import db, Course, User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('<string:user_name>')
def user(user_name):
    return render_template("user.html", user=User.query.get_or_404(username=user_name))