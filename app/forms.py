from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired("Please enter your full name")])
    email = StringField('Email', validators=[DataRequired("Please enter your e-mail address"), Email("Please enter a valid e-mail address")])
    subject = StringField('Subject', validators=[DataRequired("Please enter the subject for your message")])
    message = TextAreaField('Message', validators=[DataRequired("Please enter the message you would like to send")])
    submit = SubmitField('Send')
