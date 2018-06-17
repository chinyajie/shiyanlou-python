from flask import Blueprint, render_template
from .admin import send_message

live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
    return render_template('live/index.html')

@live.route('/systemmessage', methods=['GET', 'POST'])
def message():
    send_message()

