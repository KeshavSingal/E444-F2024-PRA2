from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'

bootstrap = Bootstrap(app)
moment = Moment(app)

# Define the form for name and email
class UserForm(FlaskForm):
    fullname = StringField('What is your full name?', validators=[DataRequired()])
    email = StringField('Enter your UofT email:', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()

    if form.validate_on_submit():
        session['fullname'] = form.fullname.data
        session['email'] = form.email.data

        # Check if the email contains 'utoronto'
        if 'utoronto' not in form.email.data:
            flash('Please enter a valid UofT email address.')
        else:
            flash(f'Hello, {form.fullname.data}! Welcome to PRA2 Docker! Your UofT email is {form.email.data}')

        return redirect(url_for('home'))

    return render_template('index.html', form=form, name=session.get('fullname'), email=session.get('email'), current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)
