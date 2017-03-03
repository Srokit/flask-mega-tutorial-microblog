from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length
from .models import User


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nn, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nn = original_nn

    def validate(self):
        if not Form.validate(self):
            # Form failed builtin form checks
            return False
        if self.nickname.data == self.original_nn:
            # If the user just didn't change their nickname
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user is not None:
            # The chosen uniquename is already in DB
            self.nickname.errors.append('This nickname is already in use ' +
                                        'another.')
            return False
        # The new nickname was not found in DB
        return True


class PostForm(Form):
    body = StringField('body', validators=[DataRequired(),
                                           Length(min=0, max=140)])


class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])
