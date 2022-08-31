from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField,  TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import  FileAllowed


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired(), FileAllowed(['jpeg' ,'png' ,'jpg'])])
    submit = SubmitField('Post')

