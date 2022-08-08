from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    post = TextAreaField('Say something',
                         validators=[DataRequired(), Length(min=1, max=140)],
                         render_kw={"placeholder": "Type your message here"})
    submit = SubmitField('Send message')
