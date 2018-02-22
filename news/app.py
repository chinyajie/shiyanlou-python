from flask import abort, redirect, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/news'
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)

'''
文章表
id：文章的ID，主键约束（db.Integer）
title: 文章名称（db.String(80)）
created_time: 文章创建时间（db.DateTime）
category_id: 文章的分类，外键约束（db.Integer, db.ForeignKey(...)）
content: 文章的内容（db.Text）

类别表包含下面的数据：
id：类别的ID，主键约束（db.Integer）
name：类别的名称（db.String(80)）
'''


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.String(80)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category',
                               backref=db.backref('articles', lazy='dynamic'))

    def __repr__(self):
        return '<Article %s>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __repr__(self):
        return '<Category %s>' % self.name



class Files(object):
    directory = os.path.join(os.path.abspath(os.path.dirname(__name__)), '..', 'files')

    def __init__(self):
        self._files = self._read_all_files()

    def _read_all_files(self):
        result = {}
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            with open(file_path) as f:
                result[filename[:-5]] = json.load(f)
        return result

    def get_title_list(self):
        return [item['title'] for item in self._files.values()]

    def get_file_by_name(self, filename):
        return self._files.get(filename)


files = Files()


@app.route('/')
def index():
    pass


@app.route('/files/<filename>')
def file(filename):
    pass


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()