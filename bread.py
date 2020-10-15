from flask import Flask, render_template, redirect, request, url_for, flash
from breadforms import loginform, registerform
from database import adduser, verifylogin, verifyemail
from datetime import datetime
import time
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'qwerty'

@app.route('/')
def main():
#redirect to home page!
    return render_template('index.html') 



@app.route('/profiles')
def profiling():
#redirect to aboutus page!
    return render_template('profile.html') 


@app.route('/about')
def abouting():
#redirect to aboutus page!
    return render_template('aboutus.html') 


@app.route('/service')
def servicing():
#redirect to aboutus page!
    return render_template('service.html') 

@app.route('/contact')
def contacting():
#redirect to contacttus page!
    return render_template('contactus.html') 

@app.route('/index')
def indexing():
#redirect to index page!
    return render_template('index.html') 

@app.route('/log')
def loging():
#redirect to login page!
    form = loginform()
    return render_template('submit.html',form=form)


#main page with login
@app.route('/home/', methods = ['GET','POST'])
def home():

    form = loginform()

    if request.method == 'POST':
        if request.form['action'] == 'Login' and form.validate_on_submit():
                email    = form.email.data.lower()
                password = form.password.data
                #validate password and email
                if verifylogin(email,password):
                    #flash('Login Success','flashok')
                    return redirect(url_for('user'))
                else:
                    flash('Email and/or password is not found','error')
      
        elif request.form['action'] == 'Register':
        	return redirect(url_for('register'))
        else:
            flash('Required field(s) are not entered','flasherror')
    return render_template('submit.html', form=form)

@app.route('/user/', methods = ['GET','POST'])
def user():
   return render_template('profile.html')  

#registration page
@app.route('/register/', methods = ['GET','POST'])
def register():
    form = registerform()
      
    if request.method == 'POST':
        if request.form['action'] == 'Register':
            email = form.email.data.lower()

            if form.validate_on_submit() == False:
                flash_errors(form)
                return render_template('register.html',form=form)
            elif verifyemail(email) == False:
                flash('Email has already been used','error')
                return render_template('register.html',form=form)  
            else:
                #collect data from form to submit to database	   
                newuser = {
		        "name" : {
		            "first" : form.firstname.data,
	                    "last" : form.lastname.data
		          },
		        "email" : form.email.data.lower(),
		        "phone" : form.phone.data,
                        "password": form.password.data,
		        "address" : {
			    "street" : form.address.data,
			    "city" : form.address.data,
			    "state" : form.state.data,
			    "zip" : form.zipcode.data,
		          },
                        "date": datetime.now()
		        }
                #insert into database collection		 
                adduser(newuser)
                flash('Registration Complete!','flashok')
                return redirect(url_for('home'))
        elif request.form['action'] == 'Login':
            return redirect(url_for('home')) 
    elif request.method == 'GET': 
        return render_template('register.html',form=form)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error),'error')

if __name__ == "__main__":
    app.config.update(
      DEBUG = True,
      CSRF_ENABLED = True,
      SECRET_KEY = 'adsfhjkaldhfhehh38718y2h2')
    app.run(host='104.131.27.56',port=5023)



