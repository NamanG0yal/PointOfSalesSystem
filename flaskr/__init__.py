import os
import psycopg2
from datetime import datetime
from flask import Flask
from flask import     redirect,url_for  , render_template , request
app = Flask(__name__)
def get_db_connection():

    conn = psycopg2.connect(
            host="localhost",
            database="zapay",
            user='naman',
            password='naman')
    return conn




    
@app.route('/inventory'   ,  methods=["POST"  ,  "GET" , "PUT" , "DELETE"  ,"PATCH"])
def Inventory():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == "GET":


        return render_template("inventory/inventory.html")

    elif request.method == "POST":
        sku  = request.form['sku']
        name = request.form['item_name']
        desc = request.form['description']
        price = request.form['price']
        quantity  = request.form['quantity']
        cur.execute('INSERT INTO InventoryItem (Item_SKU, Item_Name, Item_Description, Item_Price , Item_Qty)'
            'VALUES (%s, %s, %s, %s  , %s  )',
            (f'{sku}',
             f'{name}',
             f'{desc} ',
             price,
             quantity)
            )
        cur.close()
        conn.close()
    return render_template("inventory/inventory.html")