from flask import Flask, render_template, url_for, Blueprint, request, flash, redirect, g, session
from app import app, db
from .models import User, Article, Comment, Status
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@app.route('/')
@app.route('/index')
@app.route('/posts')
def index():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("index.html", articles=articles)


@app.route('/posts/<int:id>', methods=['POST', 'GET'])
def article_details(id):
    article_d = Article.query.get(id)
    # comments = Comment.query.order_by(Comment.date).all()
    comments = Comment.query.filter(Comment.article_id == id)
    if request.method == "POST":
        text = request.form['text']
        user_id = current_user.id
        article_id = id

        comment = Comment(text=text, user_id=user_id, article_id=article_id)

        try:
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "При добавлении статьи произошла ошибка"
    else:
        return render_template("article.html", article_d=article_d, comments=comments)


@app.route('/posts/<int:id>/del')
def post_del(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return "При удалении статьи произошла ошибка"


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get_or_404(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "При редактировании статьи произошла ошибка"
    else:
        return render_template("update-article.html", article=article)


@app.route('/create-article', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        user_id = current_user.id

        article = Article(title=title, intro=intro, text=text, user_id=user_id)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "При добавлении статьи произошла ошибка"
    else:
        return render_template("to-create.html")


@app.route('/people')
def people():
    people = User.query.all()
    return render_template("people.html", people=people)

@app.route('/people/<int:id>')
def person(id):
    person = User.query.get(id)
    states = Status.query.order_by(Status.date.desc()).all()
    return render_template("person.html", person=person, states=states)


@app.route('/to-create-status', methods=['POST', 'GET'])
def create_status():
    if request.method == "POST":
        text = request.form['text']
        user_id = current_user.id

        status = Status(text=text, user_id=user_id)

        db.session.add(status)
        db.session.commit()
        return redirect(url_for("index"))

    else:
        return render_template("to-create-status.html")
