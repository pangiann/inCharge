import os
import hashlib
import mysql.connector
import datetime


# hash plaintext password with salt and return value
def hash_password(password, salt):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key

# return random 32 byte value to be used as salt for user
def create_salt():
    salt = os.urandom(32)
    return salt

# insert superadmin in database
def insert_superadmin(Superadmin_ID, Password, First_Name, Last_Name, Email = None, Phone = None):
    query = "INSERT INTO superadmin VALUES (%s, %s, %s, %s, %s, %s, %s);"
    salt = create_salt()
    hash = hash_password(Password, salt)
    data = (Superadmin_ID, hash, salt, First_Name, Last_Name, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

# delete superadmin from database given his Boss_No
def delete_superadmin(Superadmin_ID):
    query = "DELETE FROM superadmin WHERE Superadmin_ID = %s;"
    data = (Superadmin_ID,)
    cursor.execute(query, data)
    mydb.commit()

mydb = mysql.connector.connect(
    user="root",
    password="42DataBase42",
    database="sql_inCharge",
    host="127.0.0.1",
    port="3306",
    auth_plugin='mysql_native_password',
    use_pure='True'
)
cursor = mydb.cursor()

delete_superadmin('admin')
insert_superadmin('admin','petrol4ever','Mitsos','Koulitakis')
