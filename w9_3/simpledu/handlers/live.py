from flask import Blueprint, render_template ,redirect, url_for, redirect, url_for, flash
from simpledu.decorators import admin_required
from simpledu.models import Course
from simpledu.forms import CourseForm, MessageForm
import json
from .ws import redis 

live = Blueprint('live', __name__, url_prefix='/live')


@live.route('/')
def index():
    return render_template('live/index.html')

@live.route('/systemmessage', methods=['GET', 'POST'])
def systemmessage():
    form = MessageForm()
    if form.validate_on_submit():
        redis.publish('chat', json.dumps(dict(
            username='System',
            text=form.text.data
        )))
        flash('系统消息发送成功', 'success')
        return redirect(url_for('live.systemmessage'))
    return render_template('admin/message.html', form=form)
