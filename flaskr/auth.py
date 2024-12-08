from flask import Flask  , Blueprint  ,redirect ,render_template   , url_for , jsonify , flash ,session
from datetime import timedelta 
from authlib.integrations.flask_client import OAuth
ouath = OAuth(auth)
app.permanent_session_lifetime = timedelta(days=5)
auth = Blueprint('auth',__name__,static_folder='static' , template_folder='templates/auth')

@auth.route('/login')
def login():

	return render_template('auth.html')
#session.permanent=True
@auth.route('/register')
def register():
	return render_template('register.html')