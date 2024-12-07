import os
import psycopg2
from datetime import datetime
from flask import Flask
from flask import     redirect,url_for  , render_template , request , jsonify   ,flash

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
    

    
   


    return render_template("inventory/inventory.html")



@app.route('/add_item'  , methods=['POST'])
def add_item():
    conn = get_db_connection()
    cur = conn.cursor()
    sku  = request.form["sku"]
    item_name = request.form['item_name']
    description = request.form['description']
    price = float(request.form['price'])
    quantity  = int(request.form['quantity'])
    
  
    cur.execute('INSERT INTO InventoryItem (Item_SKU, Item_Name, Item_Description, Item_Price , Item_Qty)'
        'VALUES (%s, %s, %s, %s  , %s  )',
        (f'{sku}',
        f'{item_name}',
        f'{description} ',
        price,
        quantity)
            )
    conn.commit()
    cur.close()
    conn.close()
    flash('Item Added Successfully')
    return redirect(url_for('Inventory'))