import mysql.connector

# insert contract/subscription in database
def insert_contract(Customer_ID, Supplier_ID):
    query = "SELECT Contract FROM distributor WHERE Distributor_Name = %s"
    data = (Supplier_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    if (result[0][0] == []):
        return False
    Price = result[0][0]
    query = "SELECT Username FROM customer WHERE Username = %s"
    data = (Customer_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    else:
        query = "SELECT * FROM subscription WHERE Customer_ID = %s;"
        data = (Customer_ID,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        if (result == []):
            query = "INSERT INTO subscription (Customer_ID, Supplier_ID, Price, Last_paid, Last_issued) VALUES (%s, %s, %s, %s, %s);"
            data = (Customer_ID, Supplier_ID, Price, None, None)
            cursor.execute(query, data)
            mydb.commit()
            return True
        else:
            return False

# delete contract/subscription from database
def delete_contract_unsafe(User_ID):
    query = "DELETE FROM subscription WHERE Customer_ID = %s;"
    data = (User_ID,)
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

delete_contract_unsafe('michalakos')
delete_contract_unsafe('pangiann')
delete_contract_unsafe('Pantelis_G')
delete_contract_unsafe('geosotos')
delete_contract_unsafe('vintere')
delete_contract_unsafe('vasoulis')
delete_contract_unsafe('17spyros42')
delete_contract_unsafe('trigonopsaroulis')
delete_contract_unsafe('froutotrela')
delete_contract_unsafe('nikolakisXD')
delete_contract_unsafe('kosmolagnos')
delete_contract_unsafe('dragonball')

insert_contract('michalakos', 'DEDDIE')
insert_contract('pangiann', 'ELPEDISON')
insert_contract('Pantelis_G', 'Volterra AE')
insert_contract('geosotos', 'Volton')
insert_contract('vintere', 'ZeniΘ')
insert_contract('vasoulis', 'WATT+VOLT')
insert_contract('17spyros42', 'Protergia')
insert_contract('trigonopsaroulis', 'DEDDIE')
insert_contract('froutotrela', 'PROMETHEUS GAS')
insert_contract('nikolakisXD', 'DEDDIE')
insert_contract('kosmolagnos', 'ELPEDISON')
insert_contract('dragonball', 'DEDDIE')
