from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from App.views1 import views1
from App.ext import db

from App.models import *


# 注册app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxx'
# 导入设置
app.config.from_pyfile('settings.py')
# 注册views1的蓝图
app.register_blueprint(views1)
# 数据库初始化
db.init_app(app)
# 生成迁移对象
migrate = Migrate(db=db, app=app)
# 使用flask_script
manager = Manager(app)
# 添加迁移命令，第一步init，第二步migrate，第三部upgrade
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
