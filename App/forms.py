from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

from App.models import User


class RegisterForm(Form):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired('密码不能为空')])
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message='两次密码不一致')])
    email = EmailField('邮箱', validators=[Email('邮箱格式错误')])
    phone = StringField('联系电话', validators=[Length(min=11, max=11, message='电话格式错误')])

    # 固定写法，
    def validate_username(self, field):
        user = User.query.filter(User.username == field.data).first()
        if user:
            raise ValidationError('用户名重名')
        return field
