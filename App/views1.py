from flask import Blueprint, render_template, request, redirect, make_response, url_for, session

from App.forms import RegisterForm
from App.models import *
from App.ext import db
from App.verifycode import vc, VerifyCode

views1 = Blueprint('views1', __name__)


# 主页
@views1.route('/')
def home():
    articles = Article.query.all()
    latest_articles = db.session.query(Article, Category).filter(Article.cid == Category.cid).order_by(-Article.create_time).all()
    print(latest_articles[0][0].aid)
    return render_template('index.html', **locals())


# 文章列表
@views1.route('/list/')
def list_article():
    # 获取默认分类中所有文章数据
    category = Category.query.first()
    cid = category.cid
    articles = db.session.query(Article, Category).filter(Article.cid == Category.cid, Category.cid == cid).all()
    categories = Category.query.all()
    tags = Tag.query.all()
    article_num = len(articles)
    # 最近的文章
    latest_articles = Article.query.order_by(-Article.create_time).all()[:3]
    return render_template('blog.html', **locals())


#注册
@views1.route('/register/', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        confirm = form.confirm.data
        email = form.email.data
        phone = form.phone.data
        if password == confirm:
            user = User(username=username, password=password, email=email, phone=phone)
            db.session.add(user)
            db.session.commit()
            return redirect('/login/')
    return render_template('register.html', **locals())


# 登入
@views1.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username, User.password == password)
        if user:
            # 写cookie
            response = redirect('/')
            response.set_cookie('username', username, max_age=3600*24)
            return redirect('/')
        else:
            return redirect('/login/')
    return render_template('login.html')


# 登出
@views1.route('/logout/', methods=['GET', 'POST'])
def logout():
    response = make_response('退出登录')
    response.delete_cookie('username')
    return response


@views1.route('/post/')
@views1.route('/post/<int:aid>')
def post(aid=0):
    contents = Article.query.all()
    # 右侧边栏分类
    categories = Category.query.all()
    # 右侧边栏标签
    tags = Tag.query.all()
    # 最近的三篇文章
    latest_articles = Article.query.order_by(-Article.create_time).all()[:3]
    # 根据
    comments = db.session.query(User, Comments).filter(User.uid == Comments.uid).all()
    return render_template('post.html', **locals())
