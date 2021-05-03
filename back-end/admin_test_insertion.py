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

# insert administrator in database
def insert_administrator(Administrator_No, Password, First_Name, Last_Name, Birth_Year, Birth_Month, Birth_Day, Working_Company, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Family_Members = None, Email = None, Phone = None):
    query = "INSERT INTO administrator VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    Birth_Date = datetime.date(Birth_Year, Birth_Month, Birth_Day)
    salt = create_salt()
    hash = hash_password(Password, salt)
    data = (Administrator_No, hash, salt, First_Name, Last_Name, Birth_Date, Working_Company, City, Street_Name, Street_Number, Postal_Code, Family_Members, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

# delete administrator from database given his Administrator_No
def delete_administrator(Administrator_No):
    query = "DELETE FROM administrator WHERE Administrator_No = %s;"
    data = (Administrator_No,)
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

delete_administrator('DEDDIE_admin1')
delete_administrator('DEDDIE_admin2')
delete_administrator('Protergia_admin1')
delete_administrator('Protergia_admin2')
delete_administrator('WATT+VOLT_admin1')
delete_administrator('WATT+VOLT_admin2')
delete_administrator('Volterra_AE_admin1')
delete_administrator('ELPEDISON_admin1')
delete_administrator('Volton_admin1')
delete_administrator('Volton_admin1')
delete_administrator('ZeniΘ_admin1')
delete_administrator('PROMETHEUS_GAS_admin1')

insert_administrator('DEDDIE_admin1','deddie_admin_1_pass','Iwannis','Papapetrou',1987,1,23,'DEDDIE','Athens','Rodou',43,12567,'Two','papapetrou@gmail.com',6910101010)
insert_administrator('DEDDIE_admin2','deddie_admin_2_pass','Nikolaos','Vasileiou',1988,9,11,'DEDDIE','Athens','Karaiskaki',55,43112,'Three','vasilakisnick@gmail.com',6903939394)
insert_administrator('Protergia_admin1','protergia_admin_1_pass','Kwnstantinos','Georgiou',1990,7,29,'Protergia','Athens','Kokovenou',27,11543,'Two','kwstakwsta@gmail.com',6902029292)
insert_administrator('Protergia_admin2','protergia_admin_2_pass','Vasileios','Amorgakis',1988,2,28,'Protergia','Athens','Peristeriou',2,11236,'One','amorgakisvas@gmail.com',6957574848)
insert_administrator('WATT+VOLT_admin1','watt+volt_admin_1_pass','Nikoleta','Apostolopoulou',1989,7,21,'WATT+VOLT','Athens','Leontos',8,16532,None,'nikoletaapo@gmail.com',6902030405)
insert_administrator('WATT+VOLT_admin2','watt+volt_admin_2_pass','Eleni','Hatzitheodorou',1982,11,8,'WATT+VOLT','Athens','Mpoumpoulinas',11,19876,'Three','elenihatzi@gmail.com',6992939495)
insert_administrator('Volterra_AE_admin1','volterra_admin_1_pass','Periklis','Kostantakis',1985,3,8,'Volterra AE','Athens','Kifisou',16,11726,'Four','periklaksi@gmail.com',6981828384)
insert_administrator('ELPEDISON_admin1','elpedison_admin_1_pass','Georgios','Miralidis',1983,3,19,'ELPEDISON','Athens','Leukaditou',73,17364,'Two','miralidisgeorge@gmail.com',6987868584)
insert_administrator('Volton_admin1','volton_admin_1_pass','Evaggelia','Theodorou',1986,5,18,'Volton','Athens','Sofokleous',56,19876,None,'evatheo@gmail.com',6971727374)
insert_administrator('ZeniΘ_admin1','zenith_admin_1_pass','Paraskeui','Vaskoura',1993,4,17,'ZeniΘ','Thessaloniki','Irodotou',12,11264,'Three','paraskeuoulavask@gmail.com',6942535251)
insert_administrator('PROMETHEUS_GAS_admin1','prometheus_admin_1_pass','Panagiotis','Kokoveos',1994,6,26,'PROMETHEUS GAS','Athens','Aristotelous',25,19337,'Three','pankoko@gmail.com',6926262524)
