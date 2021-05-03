import os
import hashlib
import mysql.connector


# hash plaintext password with salt and return value
def hash_password(password, salt):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key

# return random 32 byte value to be used as salt for user
def create_salt():
    salt = os.urandom(32)
    return salt

def insert_customer(Username, Car_Brand, Car_Model, Password, First_Name, Last_Name, Birth_Date, Points = 0, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Family_Members = None, Email = None, Phone = None):
    query = "SELECT car_No FROM car WHERE brand = %s AND model = %s;"
    data = (Car_Brand, Car_Model)
    cursor.execute(query, data)
    Car_ID = cursor.fetchall()
    if (Car_ID != []):
        Car_ID = Car_ID[0][0]
        query = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        salt = create_salt()
        hash = hash_password(Password, salt)
        data = (Username, Car_ID, hash, salt, First_Name, Last_Name, Points, Birth_Date, City, Street_Name, Street_Number, Postal_Code, Family_Members, Email, Phone)
        cursor.execute(query, data)
        mydb.commit()
        return True
    else:
        return False

# delete customer from database given his Username
def delete_customer(Username):
    query = "DELETE FROM customer WHERE Username = %s;"
    data = (Username,)
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

delete_customer('michalakos')
delete_customer('pangiann')
delete_customer('Pantelis_G')
delete_customer('geosotos')
delete_customer('vintere')
delete_customer('vasoulis')
delete_customer('17spyros42')
delete_customer('trigonopsaroulis')
delete_customer('froutotrela')
delete_customer('nikolakisXD')
delete_customer('kosmolagnos')
delete_customer('dragonball')

insert_customer('michalakos', 'Tesla', 'Model 3', 'JLKFjdlsa#*uy', 'Michalis', 'Vasilakos', '1999-10-01', 0, 'Athens', 'Ath.Diakou', 1, 19324, None, 'michalis@gmail.com', 6969341254)
insert_customer('pangiann', 'Tesla', 'Model 3', 'fjdaslO*UEowf0)', 'Panagiotis', 'Giannoulis', '1999-07-03', 0, 'Athens', 'Karaiskaki', 12, 11432, None, 'panagiotis@gmail.com', 6987654387)
insert_customer('Pantelis_G', 'Tesla', 'Model 3', 'kfsaJ)(*UFEosaf*&*&(', 'Pantelis', 'Gavalas', '1999-06-13', 0, 'Athens', 'Mpoumpoulinas', 45, 12054, None, 'pantelis@gmail.com', 6929349087)
insert_customer('geosotos', 'Tesla', 'Model S', 'fajsl*OUfoH()E*gfsfa', 'Giwrgos', 'Swthriou', '1999-11-19', 0, 'Athens', 'Miaouli', 76, 65812, None, 'giwrgos@gmail.com', 6987320912)
insert_customer('vintere', 'Volvo', 'XC 60 T8', '809FJd0wejfg8ajgrew09rjfga', 'Karina', 'Emporou', '2000-02-22', 0, 'Athens', 'Papaflessa', 121, 23189, None, 'mastoras@ntua.gr', 6987654309)
insert_customer('vasoulis', 'Audi', 'A3 40 e-tron', 'saysaysaysaythepassword', 'Vasilis', 'Ntounis', '2001-08-12', 0, 'Athens', 'K.Kanari', 101, 12432, None, 'kastoras@ntua.gr', 6990906745)
insert_customer('17spyros42', 'Opel', 'Corsa-e', 'SAGAPO_S-A-G-A-P-O', 'Spyros', 'Kaskolewn', '1970-08-09', 0, 'Athens', 'Filikis Etairias', 98, 12321, None, 'pastoras@ntua.gr', 6921324343)
insert_customer('trigonopsaroulis', 'Porsche', 'Taycan', 'ajsfgloisf4#$)QFj0)FJfdsaf', 'Stathon', 'Aspgomali', '1982-04-28', 0, 'Athens', 'Skoufa', 17, 12321, None, 'bob@hotmail.com', 6989894323)
insert_customer('froutotrela', 'Honda', 'e', '98nfvsan9*HJgagadf', 'Mpampinos', 'Kaskoleas', '1987-05-17', 0, 'Athens', 'Tsakalwf', 42, 12121, None, 'dod@hotmail.com', 6978433289)
insert_customer('nikolakisXD', 'Volkswagen', 'e-Golf', 'jfdas0jj0Jfd0qwjfgWJF098WJGFWE', 'Nikolas', 'Tsimpoukas', '1995-04-30', 0, 'Athens', 'Ksanthou', 45, 12653, None, 'joj@hotmail.com', 6932128943)
insert_customer('kosmolagnos', 'BMW', 'X5', 'paosdkjforhw249dfaw', 'Kosmas', 'Mperdos', '1975-04-14', 0, 'Athens', 'Mpotsari', 12, 12431, None, 'kosmas@gmail.com', 6969696969)
insert_customer('dragonball', 'Peugeot', '3008', 'LIG890eatrJO8ERPF*0gfd', 'Christos', 'Drakopoulos', '1972-11-04', 0, 'Athens', 'Kolokotroni', 112, 10431, None, 'drakopoulos@gmail.com', 6991756969)





