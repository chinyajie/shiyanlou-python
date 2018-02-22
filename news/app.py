from flask import abort, redirect, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import json
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/news'
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)
mongo = MongoClient('127.0.0.1', 27017).news

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


class File(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category',
                               backref=db.backref('file', lazy='dynamic'))

    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def __repr__(self):
        return '<Article %s>' % self.title

    def _read_all_files(self):
        result = {}
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            with open(file_path) as f:
                result[filename[:-5]] = json.load(f)
        return result


    def add_tag(self, tag_name):
        file = mongo.files.find_one({'file_id': self.id})
        if file:
            tags = file['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            mongo.files.update_one({'file_id': self.id}, {'$set': {'tags': tags}})
        else:
            tags = [tag_name]
            mongo.files.insert_one({'file_id': self.id, 'tags': tags})
        return tags

    def remove_tag(self, tag_name):
        file = mongo.files.find_one({'file_id': self.id})
        if file:
            tags = file['tags']
            if tag_name in tags:
                tags.remove(tag_name)
                mongo.files.update_one({'file_id': self.id}, {'$set': {'tags': tags}})
            return tags
        return []

    @property
    def tags(self):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            print(file_item)
            return file_item['tags']
        else:
            return []


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File') #enen

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %s>' % self.name


#
# class Files(object):
#     directory = os.path.join(os.path.abspath(os.path.dirname(__name__)), '..', 'files')
#

#
#
# files = Files()


@app.route('/')
def index():
    article_list = File.query.all()
    return render_template("index.html", article_list=article_list)


@app.route('/files/<int:file_id>')
def file(file_id):
    return render_template("file.html", article=File.query.get_or_404(file_id))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()