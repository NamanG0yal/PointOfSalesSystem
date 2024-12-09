from flask import Flask  , Blueprint  ,redirect ,render_template   , url_for , jsonify , flash ,session , request
from datetime import timedelta 
import psycopg2
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash , check_password_hash
def get_db_connection():
        conn = psycopg2.connect(
                host="localhost",
                database="zapay",
                user='naman',
                password='naman')
        return conn
auth = Blueprint('auth',__name__,static_folder='static' , template_folder='templates/auth')
auth.permanent_session_lifetime = timedelta(days=10)

@auth.route('/dashboard' , methods=['POST' , "GET"])
def dashboard():
	if request.method == 'POST':
		conn = get_db_connection()
		cur  = conn.cursor()

	else:
		return render_template('dashboard')


@auth.route('/login' , methods=['POST' , 'GET'])
def login():
	if request.method == 'POST':
		email  = request.form['email']
		password = request.form['password']
		remember = request.form['remember']
		if remember == '1':
			session.permanent = True
		else:
			session.permanent = False

		conn = get_db_connection()
		cur  = conn.cursor()
		cur.execute("SELECT * FROM Staff WHERE s_email = %s",(email,))
		data = cur.fetchone()
		cur.close()
		conn.close()
		if email:
			stored_password  = data[5]
			if check_password_hash(stored_password , password):
				access_token = create_access_token(identity = email)
				return redirect(url_for('Inventory'))
			else:
				return 'Incorrect Password typed'

	if request.method == "GET":
		return render_template('auth.html')
#session.permanent=True
@auth.route('/register', methods=['GET'])
def register():


	return render_template('register.html')

@auth.route('/new_acc' , methods=['POST'])

def new_acc():
	conn = get_db_connection()
	cur = conn.cursor()

	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	session['username']  = username
	session['email'] = email
	contact = request.form['contact']
	pp  = generate_password_hash(password , method='pbkdf2:sha256', salt_length=12)
	is_admin = request.form['is_admin']
	cur.execute('INSERT INTO Staff (  s_name , s_email  , s_contact  ,pass)'
        'VALUES ( %s, %s, %s  , %s )',
        (
         f'{str(username)}',
         f'{str(email)}',
         f'{str(contact)}',
         f'{pp}')
        )
	conn.commit()
	cur.close()
	conn.close()
	print('account_succefully created' , 'info')
	return redirect(url_for('auth.login'))