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

# insert boss in database
def insert_boss(Boss_No, Password, First_Name, Last_Name, Birth_Year, Birth_Month, Birth_Day, Working_Company, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Family_Members = None, Email = None, Phone = None):
    query = "INSERT INTO boss VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    salt = create_salt()
    hash = hash_password(Password, salt)
    Birth_Date = datetime.date(Birth_Year, Birth_Month, Birth_Day)
    data = (Boss_No, hash, salt, First_Name, Last_Name, Birth_Date, Working_Company, City, Street_Name, Street_Number, Postal_Code, Family_Members, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

# delete boss from database given his Boss_No
def delete_boss(Boss_No):
    query = "DELETE FROM boss WHERE Boss_No = %s;"
    data = (Boss_No,)
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


delete_boss('DEDDIE_boss1')
delete_boss('DEDDIE_boss2')
delete_boss('Protergia_boss1')
delete_boss('Protergia_boss2')
delete_boss('WATT+VOLT_boss1')
delete_boss('WATT+VOLT_boss2')
delete_boss('Volterra_AE_boss1')
delete_boss('ELPEDISON_boss1')
delete_boss('Volton_boss1')
delete_boss('ZeniΘ_boss1')
delete_boss('PROMETHEUS_GAS_boss1')

insert_boss('DEDDIE_boss1','o-kwdikos-mou-123','Mixahl','Vasiliou',1976,8,29,'DEDDIE','Athens','Monodendri',1,12345,'Five','michvas@gmail.com',6942136589);
insert_boss('DEDDIE_boss2','geia_sou_mastora_12','Iwannis','Nikolaou',1956,2,15,'DEDDIE','Athens','Harilaou Trikoupi',5,17364,'Three','gianonikolaou@gmail.com',69362746352);
insert_boss('Protergia_boss1','password-password-1199','Petros','Georgiou',1963,7,19,'Protergia','Athens','Parou',8,21832,'Four','geopetr@gmail.com',69123456543);
insert_boss('Protergia_boss2','mhn_me_hackarete_plzzz','Vasileios','Iwannou',1971,8,3,'Protergia','Athens','Polunisidwn',12,12323,'Four','vasiwoannou@gmail.com',6900928374);
insert_boss('WATT+VOLT_boss1','den_kserw_ti_na_gra4w','Simeon','Karageorgiou',1968,11,21,'WATT+VOLT','Athens','Kritis',15,11123,'Five','simeontherealg@gmail.com',6900012372);
insert_boss('WATT+VOLT_boss2','me_lene_petro_1212','Petros','Fotopoulos',1959,3,21,'WATT+VOLT','Athens','Panagi Tsaldari',21,12334,'Five','fotopoulakos@gmail.com',6903748572);
insert_boss('Volterra_AE_boss1','geia-eimai-o-alexandros-00','Iwanna','Papanikolaou',1971,8,30,'Volterra AE','Athens','Melinas Merkouri',31,17645,'Four','papanikolaouuu@gamil.com',6901928374);
insert_boss('ELPEDISON_boss1','elpedison_4_ever','Vasiliki','Karanikoli',1979,9,17,'ELPEDISON','Athens','Themistokleous',12,18882,'Two','vasivasi@gmail.com',6912345678);
insert_boss('Volton_boss1','i-work-4-volton','Panagiotis','Papaswtiriou',1980,4,15,'Volton','Athens','Demirdesiou',18,16623,'Three','papaswtirakis@gmail.com',6909876543);
insert_boss('ZeniΘ_boss1','giannakis-gia-3-mesa!!!','Panagiotis','Giannakis',1981,11,13,'ZeniΘ','Athens','Kolokotroni',53,22148,'Four','iwontheeuropeancup@gmail.com',6934567890);
insert_boss('PROMETHEUS_GAS_boss1','who-is-the-bo$$','Georgios','Pestouridis',1978,5,28,'PROMETHEUS GAS','Athens','Eutuxias',46,12449,'Four','pastouridis@gmail.com',6909871234);
