APT=sudo apt install -y
PYTHON=python3
PIP=pip3



py_deps: requirements.txt
	$(PIP) install -r requirements.txt


test_db:
	sudo mysql -u root -e 'create database sql_inCharge;' 
	sudo sh ./database_config.sh >> ~/.my.cnf
	sudo mysql -u root sql_inCharge < back-end/create_inCharge_Database.sql
	sudo mysql -u root sql_inCharge < back-end/inCharge_Data_Insertion.sql
	sudo mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '42DataBase42'"
	

deps:
	$(APT) mysql-server python3-pip
	$(MAKE) py_deps
	


certificate_gen:
	openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365




