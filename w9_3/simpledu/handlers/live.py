from flask import Blueprint, render_template

live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
    return render_template('live/index.html')


@live.route('/systemmessage')
def index():
    return render_template('admin/message.html')

