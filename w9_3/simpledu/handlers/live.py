from flask import Blueprint, render_template ,redirect, url_for
 

live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
    return render_template('live/index.html')

@live.route('/systemmessage', methods=['GET', 'POST'])
def message():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return redirect(url_for('admin.send_message'))

