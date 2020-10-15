# login form class using WTForms. 
from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, IntegerField, FormField, SelectField
#from wtforms.fields.html5 import EmailField

class loginform(Form):
    
    email    = StringField('Email',[validators.DataRequired(),validators.Email()], default="example@bread.com")
    password = PasswordField('Password',[validators.DataRequired()])

class registerform(Form):

    firstname = StringField('First Name',[validators.DataRequired()])
    lastname = StringField('Last Name',[validators.DataRequired()])
    email = StringField('Email',[validators.DataRequired(),validators.Email()])
    password = PasswordField('New Password',[validators.DataRequired(),validators.EqualTo('confirm',message='Passwords must match')])
    confirm = PasswordField('Repeat Password',[validators.DataRequired()])
    address = TextAreaField('Mailing Address', [validators.DataRequired()])
    city = StringField('City', [validators.DataRequired()])
    state = SelectField('State',choices=[('Pennsylvaina','PA'),('Maryland','MD')])
    zipcode = IntegerField('Zip Code',[validators.DataRequired()]) 
    phone = IntegerField('Telephone', [validators.DataRequired()])



