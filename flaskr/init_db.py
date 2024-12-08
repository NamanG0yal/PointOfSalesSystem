import os
import psycopg2 
from psycopg2.extras import RealDictCursor
import click 
from flask import current_app ,g 
from datetime import datetime
def get_db_connection():
        conn = psycopg2.connect(
                host="localhost",
                database="zapay",
                user='naman',
                password='naman')
        return conn
conn = get_db_connection()
cur  = conn.cursor()
cur.execute('DROP TABLE IF EXISTS InventoryItem')
cur.execute('CREATE TABLE InventoryItem ('
                                 'Item_SKU VARCHAR(100) NOT NULL UNIQUE ,'
                                 'Item_Name varchar (150) NOT NULL UNIQUE,'
                                 'Item_Description varchar (500) NOT NULL,'
                                 'Item_Price integer NOT NULL CONSTRAINT positive_price   CHECK (Item_Price >  0 ),'
                                 'Item_Qty integer NOT NULL);'
			         )
cur.execute('CREATE TABLE Customer ('
                                 'c_ID  SERIAL PRIMARY KEY ,'

                                 'c_name varchar(100) NOT NULL,'
                                 'c_email varchar(100) NOT NULL,'
                                 'c_contact bigint NOT NULL UNIQUE);'
                                 )
cur.execute('CREATE TABLE Staff ('
                                 's_ID serial PRIMARY KEY,'
                                 's_name  varchar(100) NOT NULL,'
                                 's_email varchar(100) NOT NULL ,'
                                 's_isAdmin varchar(13) NOT NULL,'
                                 's_contact varchar(10) NOT NULL UNIQUE,'
                                 'pass varchar(199) NOT NULL CHECK(LENGTH(pass) >= 8) );'
                                 )
cur.execute('CREATE TABLE Transaction ('
                                 't_ID bigserial PRIMARY KEY,'
                                 't_date bigint,'
                                 't_amount bigint,'
                                 't_category integer ,'
                                 'c_ID SERIAL UNIQUE ,'
                                 'FOREIGN KEY(c_ID) REFERENCES Customer(c_ID));'
                                 )
cur.execute('INSERT INTO InventoryItem (Item_SKU, Item_Name, Item_Description, Item_Price , Item_Qty)'
            'VALUES (%s, %s, %s, %s , %s )',
            ('Toothbrush',
             'ChizelBristleS',
             'Electric toothbrush for the new generation ',
             10,
             5000)
            )
cur.execute('INSERT INTO Customer (c_ID  , c_name ,c_email , c_contact)'
        'VALUES (%s, %s, %s, %s )',
        (100000000 , 
         'Naman Goyal',
         'namagyal2@gmail.com',
         9871912939213)
        )
cur.execute('INSERT INTO Staff (s_ID , s_name , s_email , s_isAdmin , s_contact , pass)'
        'VALUES (%s, %s, %s, %s  , %s , %s )',
        (100000000,
         'Suchi',
         'Suchi@zapay.org',
         'Yes',
         '9871993533',
         'qwerty_zaxeru')
        )
cur.execute('INSERT INTO Transaction (t_ID , t_date , t_amount , t_category  , c_ID )'
        'VALUES (%s, %s, %s, %s  , %s)',
        (100000000 ,
         20241205,
         1000000,
         2,
         100000000)
        )
conn.commit()

cur.close()
conn.close()
