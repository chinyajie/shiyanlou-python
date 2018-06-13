from flask import Blueprint, render_template
from simpledu.models import Course, Chapter
from flask_login import login_required

course = Blueprint('live', __name__, url_prefix='/live')


@course.route('/')
def index():
    live = Live.query.order_by(Live.create_at.desc()).limit(1).first()
    return render_template('live/index.html', live=live)

