from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'

# Initialize Bootstrap and Moment for styling and time functionality
bootstrap = Bootstrap(app)
moment = Moment(app)

# Define a form for user input
class UserForm(FlaskForm):
    fullname = StringField('What is your full name?', validators=[DataRequired()])
    email = StringField('Enter your UofT email:', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    
    if form.validate_on_submit():
        # Save name and email in the session
        session['fullname'] = form.fullname.data
        session['email'] = form.email.data
        
        # Check if the email is a valid UofT email
        if 'utoronto' not in form.email.data:
            flash('Please enter a valid UofT email address (must contain "utoronto").')
        else:
            flash(f'Hello, {form.fullname.data}! Your UofT email is {form.email.data}')
        
        return redirect(url_for('home'))

    return render_template('index.html', form=form, 
                           name=session.get('fullname'), 
                           email=session.get('email'), 
                           current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)
