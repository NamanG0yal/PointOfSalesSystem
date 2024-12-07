import os
import psycopg2
from datetime import datetime
from flask import Flask
from flask import     redirect,url_for  , render_template , request

def get_db_connection():

    conn = psycopg2.connect(
            host="localhost",
            database="zapay",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
    return conn
app = Flask(__name__)


    
@app.route('/inventory'   ,  methods=["POST"  ,  "GET" , "PUT" , "DELETE"  ,"PATCH"])
def Inventory():
    if request.method == "GET":


        return render_template("inventory/inventory.html")

