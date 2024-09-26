from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', 
                           current_time=datetime.utcnow(),
                           name='Keshav')

if __name__ == '__main__':
    app.run(debug=True)
