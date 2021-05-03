-- ------------ CUSTOMER ------------
-- AUTOMATED INSERTION (customer_test_insertion.py)

-- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ ADMINISTRATOR ------------
-- AUTOMATED INSERTION (admin_test_insertion.py)

-- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ BOSS ------------
-- AUTOMATED INSERTION (boss_test_insertion.py)

-- -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ MANUFACTURER ------------
INSERT INTO `manufacturer` VALUES ('Audi','Ingolstadt','AG Ettinger',70,85057,'imprint@audi.de',49841890);
INSERT INTO `manufacturer` VALUES ('BMW','Munich','Petuerling',130,80809,'classic@bmwgroup.com',498938217981);
INSERT INTO `manufacturer` VALUES ('Citroen','Saint-Ouen','Rueil-Malmaison',80,78093,'service_presse@citroen.com',08000939393);
INSERT INTO `manufacturer` VALUES ('Fiat','Torino','Corso Agnelli',200,10135,'centroarchiviostorico@fcagroup.com',390110031111);
INSERT INTO `manufacturer` VALUES ('Ford','Dearborn','Ford Motor Company',1,48126,NULL,18003923673);
INSERT INTO `manufacturer` VALUES ('Hyundai','Seoul','Seocho-gu',12,NULL,NULL,82234641114);
INSERT INTO `manufacturer` VALUES ('Jaguar','Birmingham','Jaguar Land Rover',1,NULL,NULL,03705000500);
INSERT INTO `manufacturer` VALUES ('Kia','Seoul','Peters Canyon',111,92606,NULL,9494684800);
INSERT INTO `manufacturer` VALUES ('Mercedes Benz','Stuttgart','Daimler AG',120,70546,'dialog@daimler.com',49711170);
INSERT INTO `manufacturer` VALUES ('Mitsubishi','Tokyo','Chiyoda-ku',100,8086,NULL,81332102121);
INSERT INTO `manufacturer` VALUES ('Nissan','Yokohama','Nishi-ku',220,8686,NULL,81455235523);
INSERT INTO `manufacturer` VALUES ('Opel','Rüsselsheim','Bahnhofsplatz',1,65423,'opel.post@opel.com',06142774057);
INSERT INTO `manufacturer` VALUES ('Peugeot','London','Route de Gisy',1,78140,NULL,330157593000);
INSERT INTO `manufacturer` VALUES ('Renault','Boulogne-Billancourt','Quai le Gallo',13,92513,NULL,330176840404);
INSERT INTO `manufacturer` VALUES ('Smart','Makati','Ayala Avenue',6799,1226,'Smartschools@smart.com.ph',025113100);
INSERT INTO `manufacturer` VALUES ('Tesla','Palo Alto CA','Deer Creek Road',3500,94304,NULL,02111984867);
INSERT INTO `manufacturer` VALUES ('Volkswagen','Wolfsburg','Berliner Ring',2,38440,'vw@volkswagen.de',49536190);
INSERT INTO `manufacturer` VALUES ('Mini','New Jersey','Chestnut Ridge Rd',300,38627,NULL,8662756464);
INSERT INTO `manufacturer` VALUES ('Honda','Minato','Minami-Aoyama',107,8556,NULL,810334231111);
INSERT INTO `manufacturer` VALUES ('Porsche','Stuttgart','Porscheplatz',1,70435,NULL,07119110);
INSERT INTO `manufacturer` VALUES ('MG','Cairo','Teseen',54,11835,NULL,20221281800);
INSERT INTO `manufacturer` VALUES ('Maxus','Shanghai','Jungong Road', 2500,200438,NULL,NULL);
INSERT INTO `manufacturer` VALUES ('Polestar','Göteborg','Assar Gabrielssons',9,41878,NULL,8008062504);
INSERT INTO `manufacturer` VALUES ('Seat','Martorell','Autovía',585,NULL,NULL,0500222222);
INSERT INTO `manufacturer` VALUES ('Skoda','Mladá Boleslav','Václava Klementa',869,29301,'infoline@skoda-auto.cz',00420800600000);
INSERT INTO `manufacturer` VALUES ('DS','Meyrin','Dharampal Satyapal',67,201309,'ds@dsgroup.com',01204032200);
INSERT INTO `manufacturer` VALUES ('Aiways','Shanghai',NULL,NULL,NULL,NULL,NULL);
INSERT INTO `manufacturer` VALUES ('Artega','Delbrümanufacturerck','Bösendamm',11,6283,'info(at)artega.de',004905250938310);
INSERT INTO `manufacturer` VALUES ('e.GO Mobile','Aachen',NULL,NULL,NULL,NULL,NULL);
INSERT INTO `manufacturer` VALUES ('Volvo','Gothenburg','AB Volvo SE',1,40508,NULL,4631660000);
INSERT INTO `manufacturer` VALUES ('Mazda','Fuchu','Shinchi',3,7308670,NULL,8008661998);
INSERT INTO `manufacturer` VALUES ('Chevrolet','Detroit','Colonel Sam Drive',1,19084,NULL,18002221020);

-- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ CAR ------------
INSERT INTO `car` VALUES ('89c2668c-0c50-4344-9386-93e4000f7673','Audi','e-tron 55','BEV', 86.5,2019);
INSERT INTO `car` VALUES ('89c2668c-0c50-4344-9386-93e4000f7674','Audi','e-tron 50','BEV', 65.0,2019);
INSERT INTO `car` VALUES ('89c2668c-0c50-4344-9386-93e4000f7675','Audi','A3 40 e-tron','PHEV',08.8,2020);
INSERT INTO `car` VALUES ('0742668c-bf59-4191-890e-2b0883508808','BMW','i3','BEV', 37.9,NULL);
INSERT INTO `car` VALUES ('0742668c-bf59-4191-890e-2b0883508809','BMW','X5','PHEV',21.0,2020);
INSERT INTO `car` VALUES ('3b3fc191-f4c3-45da-bc3b-21efbe1b264f','Citroen','C-Zero','BEV',14.5,NULL);
INSERT INTO `car` VALUES ('3b3fc191-f4c3-45da-bc3b-21efbe1b264g','Citroen','Berlingo Electric','BEV',22.5,NULL);
INSERT INTO `car` VALUES ('3291e5ba-862c-49fa-8437-71105743875e','Fiat','500e','BEV', 19.2,2014);
INSERT INTO `car` VALUES ('6cf9e9b6-28aa-44c7-b6c3-438d518ac12f','Ford','Focus electric','BEV', 33.5,2017);
INSERT INTO `car` VALUES ('6cf9e9b6-28aa-44c7-b6c3-438d518ac12g','Ford','Kuga','PHEV',14.4,2020);
-- --------- --------- --------- --------- --------- ---------
INSERT INTO `car` VALUES ('9771afb8-9e25-4ae6-a5b3-b2a5b9f363f0','Hyundai','Kona','BEV', 39.2,2018);
INSERT INTO `car` VALUES ('9771afb8-9e25-4ae6-a5b3-b2a5b9f363f1','Hyundai','Ioniq','BEV', 28.0,2016);
INSERT INTO `car` VALUES ('61fc79a2-04ca-418e-9333-caf5f67ba02f','Jaguar','i-Pace','BEV', 84.0,NULL);
INSERT INTO `car` VALUES ('3337d5f0-39de-4ded-831b-843dfec1ebbd','Kia','e-niro','BEV', 39.0,2018);
INSERT INTO `car` VALUES ('3337d5f0-39de-4ded-831b-843dfec1ebbe','Kia','Soul','BEV', 27.0,NULL);
INSERT INTO `car` VALUES ('3337d5f0-39de-4ded-831b-843dfec1ebbf','Kia','e-Soul','BEV', 39.0,2019);
INSERT INTO `car` VALUES ('3337d5f0-39de-4ded-831b-843dfec1ebbg','Kia','e-Niro','BEV', 64.0,2018);
INSERT INTO `car` VALUES ('3337d5f0-39de-4ded-831b-843dfec1ebbh','Kia','Ceed SW','PHEV',08.9,2020);
INSERT INTO `car` VALUES ('3337d5f0-39de-4ded-831b-843dfec1ebbi','Kia','XCeed','PHEV',08.9,2020);
INSERT INTO `car` VALUES ('3337d5f0-39de-4ded-831b-843dfec1ebbj','Kia','Niro','PHEV',08.9,2020);
-- --------- --------- --------- --------- --------- ---------
INSERT INTO `car` VALUES ('b2282fbe-f5d9-48d9-943f-a9b66ec51423','Mercedes Benz','EQC','BEV', 80.0,2019);
INSERT INTO `car` VALUES ('b2282fbe-f5d9-48d9-943f-a9b66ec51424','Mercedes Benz','B-Klasse','BEV', 28.0,NULL);
INSERT INTO `car` VALUES ('b2282fbe-f5d9-48d9-943f-a9b66ec51425','Mercedes Benz','A 250 e','PHEV',10.7,2020);
INSERT INTO `car` VALUES ('b2282fbe-f5d9-48d9-943f-a9b66ec51426','Mercedes Benz','GLC 300 de 4MATIC','PHEV', 13.5,2020);
INSERT INTO `car` VALUES ('b2282fbe-f5d9-48d9-943f-a9b66ec51427','Mercedes Benz','GLE','PHEV',31.2,2020);
INSERT INTO `car` VALUES ('3cf8cf51-60ac-4cac-9f25-131c21eda12e','Mitsubishi','i-Miev','BEV', 14.5,NULL);
INSERT INTO `car` VALUES ('3cf8cf51-60ac-4cac-9f25-131c21eda12f','Mitsubishi','Outlander PHEV','PHEV',11.0,2018);
INSERT INTO `car` VALUES ('dab5a47a-e8ce-4d34-9139-0701499205b1','Nissan','e-NV 200','BEV', 24.0,NULL);
INSERT INTO `car` VALUES ('dab5a47a-e8ce-4d34-9139-0701499205b2','Nissan','Leaf','BEV', 62.0,2019);
INSERT INTO `car` VALUES ('3500fb3e-bd2c-478e-ae5e-ac9ee490594b','Opel','Ampera e','BEV',60.0,2017);
-- --------- --------- --------- --------- --------- ---------
INSERT INTO `car` VALUES ('3500fb3e-bd2c-478e-ae5e-ac9ee490594c','Opel','Ampera e-Pionier','BEV',10.6,2012);
INSERT INTO `car` VALUES ('3500fb3e-bd2c-478e-ae5e-ac9ee490594d','Opel','Corsa-e','BEV',47.5,2020);
INSERT INTO `car` VALUES ('f458fe7d-f545-45f3-8c23-2ab8140b8b5d','Peugeot','I-on','BEV',14.5,NULL);
INSERT INTO `car` VALUES ('f458fe7d-f545-45f3-8c23-2ab8140b8b5e','Peugeot','e-208','BEV',47.5,2020);
INSERT INTO `car` VALUES ('f458fe7d-f545-45f3-8c23-2ab8140b8b5f','Peugeot','e-2008','BEV',47.5,2020);
INSERT INTO `car` VALUES ('f458fe7d-f545-45f3-8c23-2ab8140b8b5g','Peugeot','3008','PHEV',11.2,2020);
INSERT INTO `car` VALUES ('f458fe7d-f545-45f3-8c23-2ab8140b8b5h','Peugeot','Partner','BEV',22.5,NULL);
INSERT INTO `car` VALUES ('c0d8a60c-34b8-44fe-8af7-9eeb62eedb4b','Renault','Zoe','BEV',22.0,2013);
INSERT INTO `car` VALUES ('c0d8a60c-34b8-44fe-8af7-9eeb62eedb4c','Renault','Kangoo ZE','BEV',33.0,NULL);
INSERT INTO `car` VALUES ('c0d8a60c-34b8-44fe-8af7-9eeb62eedb4d','Renault','Twizy','BEV',06.1,NULL);
-- --------- --------- --------- --------- --------- ---------
INSERT INTO `car` VALUES ('c0d8a60c-34b8-44fe-8af7-9eeb62eedb4e','Renault','Captur E-Tech','PHEV',09.8,2020);
INSERT INTO `car` VALUES ('a462c115-33b4-438b-b590-bc4a33382d1c','Smart','fortwo ED','BEV',17.6,NULL);
INSERT INTO `car` VALUES ('a462c115-33b4-438b-b590-bc4a33382d1d','Smart','fortwo EQ','BEV',17.6,NULL);
INSERT INTO `car` VALUES ('a462c115-33b4-438b-b590-bc4a33382d1e','Smart','forfour EQ','BEV',17.6,NULL);
INSERT INTO `car` VALUES ('f37896c3-6bc5-45e1-b442-b9cbc38e3a7c','Tesla','Model 3','BEV',74.0,NULL);
INSERT INTO `car` VALUES ('f37896c3-6bc5-45e1-b442-b9cbc38e3a7d','Tesla','Model S','BEV',95.0,NULL);
INSERT INTO `car` VALUES ('f37896c3-6bc5-45e1-b442-b9cbc38e3a7e','Tesla','Model X','BEV',99.9,2017);
INSERT INTO `car` VALUES ('481793f5-c8b0-4dc9-b3d4-cc615085ac07','Volkswagen','e-Golf','BEV',31.5,2017);
INSERT INTO `car` VALUES ('481793f5-c8b0-4dc9-b3d4-cc615085ac08','Volkswagen','e-up','BEV',16.5,2013);
INSERT INTO `car` VALUES ('481793f5-c8b0-4dc9-b3d4-cc615085ac09','Volkswagen','ID.3','BEV',45.0,2020);
-- --------- --------- --------- --------- --------- ---------
INSERT INTO `car` VALUES ('481793f5-c8b0-4dc9-b3d4-cc615085ac10','Volkswagen','Golf GTE','PHEV',08.7,2017);
INSERT INTO `car` VALUES ('481793f5-c8b0-4dc9-b3d4-cc615085ac11','Volkswagen','Passat GTE','PHEV',13.1,2019);
INSERT INTO `car` VALUES ('6d9d9248-de4a-4b13-976b-4e9f6688b0b1','Mini','Countryman ALL4','PHEV',07.6,2019);
INSERT INTO `car` VALUES ('6d9d9248-de4a-4b13-976b-4e9f6688b0b2','Mini','Cooper SE','BEV',28.9,2020);
INSERT INTO `car` VALUES ('9ca5e092-76e2-4868-afc1-c06abeedf81b','Honda','e','BEV',32.0,2020);
INSERT INTO `car` VALUES ('68e11a25-d316-4d22-9444-45c7306c8ab7','Porsche','Taycan','BEV',83.7,2020);
INSERT INTO `car` VALUES ('5663b87a-d940-4bab-9846-d74c8c0ae260','MG','ZS EV','BEV',44.5,2020);
INSERT INTO `car` VALUES ('171a1e6d-8cbc-41a9-a8bb-e05b7ee98889','Maxus','EV80','BEV',56.0,2018);
INSERT INTO `car` VALUES ('391f000f-d9d1-4c13-b744-95f0b9c8a2e1','Polestar','2','BEV',72.5,2020);
INSERT INTO `car` VALUES ('91c527ff-aa74-4dbb-9091-36fb5ddd44b6','Seat','Mii Electric','BEV',32.3,2020);
-- --------- --------- --------- --------- --------- ---------
INSERT INTO `car` VALUES ('43763587-6999-406b-8843-28977e1b82c3','Skoda','CITIGOe iV','BEV',32.3,2020);
INSERT INTO `car` VALUES ('43763587-6999-406b-8843-28977e1b82c4','Skoda','Superb iV','PHEV',13.0,2020);
INSERT INTO `car` VALUES ('43763587-6999-406b-8843-28977e1b82c5','Skoda','Enyaq iV','BEV',58.0,2020);
INSERT INTO `car` VALUES ('37bfdacf-1aca-4eb7-8daa-8dc5b14c59e9','DS','3 Crossback E-Tense','BEV',46.0,2020);
INSERT INTO `car` VALUES ('37bfdacf-1aca-4eb7-8daa-8dc5b14c59e8','DS','7 Crossback','PHEV',13.2,2020);
INSERT INTO `car` VALUES ('a43d2607-eead-46c2-9fd5-2ebd3c49d895','Aiways','U5','BEV',63.0,2020);
INSERT INTO `car` VALUES ('97d0d03a-63c6-4f33-99d7-6e944f71d7c5','Artega','Karo','BEV',14.4,2020);
INSERT INTO `car` VALUES ('771bb157-23a2-4917-908c-810d241718d5','e.GO Mobile','Life 60','BEV',21.0,2019);
INSERT INTO `car` VALUES ('771bb157-23a2-4917-908c-810d241718d6','e.GO Mobile','Life 40','BEV',17.5,2019);
INSERT INTO `car` VALUES ('771bb157-23a2-4917-908c-810d241718d7','e.GO Mobile','Life 20','BEV',14.5,2019);
-- --------- --------- --------- --------- --------- ---------
INSERT INTO `car` VALUES ('2e55ea02-c829-4256-94fd-ffc971a1dd8e','Volvo','XC 60 T8','PHEV',10.4,2018);
INSERT INTO `car` VALUES ('9b829849-1219-48b8-964e-90ddc1a4fa85','Mazda','MX-30','BEV',32.0,2020);
INSERT INTO `car` VALUES ('cbca5847-9b23-47d9-80d3-24fa9a8ca21a','Chevrolet','Bolt','BEV',58.0,2017);
INSERT INTO `car` VALUES ('cbca5847-9b23-47d9-80d3-24fa9a8ca21b','Chevrolet','Spark EV','BEV',21.3,2013);

-- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ PRODUCER ------------
INSERT INTO `producer` VALUE ('Public Power Corporation','Athens','Halkokondili',30,10432,NULL,2105230301);

-- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ DISTRIBUTOR ------------
INSERT INTO `distributor` VALUES ('DEDDIE','Public Power Corporation',00.00,07.99,'Athens','Kallirois',5,11743,'infodeddie@deddie.gr','www.deddie.gr',2144050205);
INSERT INTO `distributor` VALUES ('Protergia','Public Power Corporation',00.0008,07.99,'Athens','Marinou Antipa',11,14121,NULL,'www.protergia.gr',2103448500);
INSERT INTO `distributor` VALUES ('WATT+VOLT','Public Power Corporation',00.0007,08.49,'Athens','Leoforos Kifisias',217,15124,'info@watt-volt.gr','www.watt-volt.gr',2130189199);
INSERT INTO `distributor` VALUES ('Volterra AE','Public Power Corporation',00.0009,08.99,'Athens','Halandriou',16,15125,'info@volterra.gr','www.volterra.gr',2130883000);
INSERT INTO `distributor` VALUES ('ELPEDISON','Public Power Corporation',00.0005,07.99,'Athens','Leoforos Kifisias',283,14562,'shop.kifissia@elpedison.gr','www.elpedison.gr',2169006999);
INSERT INTO `distributor` VALUES ('Volton','Public Power Corporation',00.0007,08.10,'Athens','Leoforos Siggrou',128,11745,'cs@volton.gr','www.volton.gr',2163001000);
INSERT INTO `distributor` VALUES ('ZeniΘ','Public Power Corporation',00.0008,09.99,'Thessaloniki','October 26th',54,54627,'info@zenith.gr','www.zenith.gr',2311223045);
INSERT INTO `distributor` VALUES ('PROMETHEUS GAS','Public Power Corporation',00.0008,08.49,'Athens','Leoforos Kifisias',209,15124,'info@prometheusgas.gr','www.prometheusgas.gr',2106141130);

-- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ CHARGING_SESSION ------------
-- AUTOMATED INSERTION

-- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ CHARGING_STATION ------------
INSERT INTO `charging_station` VALUES ('Station_1','Athens','Kifisias',12,'operator_1');
INSERT INTO `charging_station` VALUES ('Station_2','Athens','Marathonos',8,'operator_2');
INSERT INTO `charging_station` VALUES ('Station_3','Athens','Mesogeiwn',15,'operator_1');
INSERT INTO `charging_station` VALUES ('Station_4','Athens','Patisiwn',53,'operator_3');
INSERT INTO `charging_station` VALUES ('Station_5','Athens','Vouliagmenis',26,'operator_4');
INSERT INTO `charging_station` VALUES ('Station_6','Thessaloniki','3rd of September',44,'operator_4');
INSERT INTO `charging_station` VALUES ('Station_7','Thessaloniki','30th of October',42,'operator_4');
INSERT INTO `charging_station` VALUES ('Station_8','Thessaloniki','Tsimiski',19,'operator_5');
INSERT INTO `charging_station` VALUES ('Station_9','Athens','Athinwn',28,'operator_6');
INSERT INTO `charging_station` VALUES ('Station_10','Patra','Glaukou',19,'operator_7');
INSERT INTO `charging_station` VALUES ('Station_11','Patra','Dimitriou Gounari',27,'operator_1');
INSERT INTO `charging_station` VALUES ('Station_12','Trikala','Alexandras',7,'operator_2');
INSERT INTO `charging_station` VALUES ('Station_13','Kimi','Aliveriou',12,'operator_8');
INSERT INTO `charging_station` VALUES ('Station_14','Korinthos','Ethniki Odos Athinwn',160,'operator_7');
INSERT INTO `charging_station` VALUES ('Station_15','Hania','Karamanli',18,'operator_9');
INSERT INTO `charging_station` VALUES ('Station_16','Iraklio','Knosou',46,'operator_10');
INSERT INTO `charging_station` VALUES ('Station_17','Serres','Merarxias',63,'operator_10');
INSERT INTO `charging_station` VALUES ('Station_18','Athens','Kifisou',22,'operator_8');
INSERT INTO `charging_station` VALUES ('Station_19','Athens','Siggrou',11,'operator_6');
INSERT INTO `charging_station` VALUES ('Station_20','Tripoli','Leoforos OHE',14,'operator_11');
INSERT INTO `charging_station` VALUES ('Station_21','Karditsa','Dimokratias',16,'operator_11');
INSERT INTO `charging_station` VALUES ('Station_22','Iwannina','Iwanninwn',28,'operator_12');
INSERT INTO `charging_station` VALUES ('Station_23','Zakinthos','Dimokratias',84,'operator_13');
INSERT INTO `charging_station` VALUES ('Station_24','Rodos','Lindou',22,'operator_3');
INSERT INTO `charging_station` VALUES ('Station_25','Mitilini','Odissea Eliti',10,'operator_13');

-- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ CHARGING_POINT ------------
-- --------- Station 1 ----------
INSERT INTO `charging_point` VALUES ('Station_1_1','DEDDIE','Station_1',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_1_2','DEDDIE','Station_1',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_1_3','ELPEDISON','Station_1',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_1_4','Volterra AE','Station_1',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_1_5','Protergia','Station_1',0.1667,00.025);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 2 ----------
INSERT INTO `charging_point` VALUES ('Station_2_1','WATT+VOLT','Station_2',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_2_2','Volterra AE','Station_2',0.1667,00.025);
INSERT INTO `charging_point` VALUES ('Station_2_3','DEDDIE','Station_2',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_2_4','ZeniΘ','Station_2',0.1667,00.04);
INSERT INTO `charging_point` VALUES ('Station_2_5','Protergia','Station_2',0.2,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 3 ----------
INSERT INTO `charging_point` VALUES ('Station_3_1','DEDDIE','Station_3',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_3_2','DEDDIE','Station_3',0.2,00.028);
INSERT INTO `charging_point` VALUES ('Station_3_3','Volterra AE','Station_3',0.1667,00.032);
INSERT INTO `charging_point` VALUES ('Station_3_4','DEDDIE','Station_3',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_3_5','Protergia','Station_3',0.2,00.025);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 4 ----------
INSERT INTO `charging_point` VALUES ('Station_4_1','DEDDIE','Station_4',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_4_2','ELPEDISON','Station_4',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_4_3','WATT+VOLT','Station_4',0.1667,00.035);
INSERT INTO `charging_point` VALUES ('Station_4_4','Protergia','Station_4',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_4_5','WATT+VOLT','Station_4',0.1667,00.035);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 5 ----------
INSERT INTO `charging_point` VALUES ('Station_5_1','DEDDIE','Station_5',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_5_2','Volterra AE','Station_5',0.1667,00.04);
INSERT INTO `charging_point` VALUES ('Station_5_3','DEDDIE','Station_5',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_5_4','PROMETHEUS GAS','Station_5',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_5_5','Volton','Station_5',0.2,00.025);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 6 ----------
INSERT INTO `charging_point` VALUES ('Station_6_1','ZeniΘ','Station_6',0.2,00.02);
INSERT INTO `charging_point` VALUES ('Station_6_2','ELPEDISON','Station_6',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_6_3','WATT+VOLT','Station_6',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_6_4','DEDDIE','Station_6',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_6_5','WATT+VOLT','Station_6',0.1667,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 7 ----------
INSERT INTO `charging_point` VALUES ('Station_7_1','Protergia','Station_7',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_7_2','DEDDIE','Station_7',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_7_3','DEDDIE','Station_7',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_7_4','PROMETHEUS GAS','Station_7',0.1667,00.025);
INSERT INTO `charging_point` VALUES ('Station_7_5','ZeniΘ','Station_7',0.2,00.04);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 8 ----------
INSERT INTO `charging_point` VALUES ('Station_8_1','Volterra AE','Station_8',0.1667,00.0);
INSERT INTO `charging_point` VALUES ('Station_8_2','PROMETHEUS GAS','Station_8',0.2,00.0);
INSERT INTO `charging_point` VALUES ('Station_8_3','WATT+VOLT','Station_8',0.2,00.0);
INSERT INTO `charging_point` VALUES ('Station_8_4','ZeniΘ','Station_8',0.1667,00.0);
INSERT INTO `charging_point` VALUES ('Station_8_5','DEDDIE','Station_8',0.1667,00.0);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 9 ----------
INSERT INTO `charging_point` VALUES ('Station_9_1','DEDDIE','Station_9',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_9_2','PROMETHEUS GAS','Station_9',0.2,00.025);
INSERT INTO `charging_point` VALUES ('Station_9_3','Volton','Station_9',0.1667,00.02);
INSERT INTO `charging_point` VALUES ('Station_9_4','Protergia','Station_9',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_9_5','WATT+VOLT','Station_9',0.2,00.025);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 10 ----------
INSERT INTO `charging_point` VALUES ('Station_10_1','DEDDIE','Station_10',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_10_2','PROMETHEUS GAS','Station_10',0.2,00.04);
INSERT INTO `charging_point` VALUES ('Station_10_3','Volton','Station_10',0.2,00.04);
INSERT INTO `charging_point` VALUES ('Station_10_4','Volterra AE','Station_10',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_10_5','Volterra AE','Station_10',0.2,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 11 ----------
INSERT INTO `charging_point` VALUES ('Station_11_1','ELPEDISON','Station_11',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_11_2','DEDDIE','Station_11',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_11_3','Protergia','Station_11',0.2,00.04);
INSERT INTO `charging_point` VALUES ('Station_11_4','ELPEDISON','Station_11',0.1667,00.04);
INSERT INTO `charging_point` VALUES ('Station_11_5','WATT+VOLT','Station_11',0.2,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 12 ----------
INSERT INTO `charging_point` VALUES ('Station_12_1','Protergia','Station_12',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_12_2','PROMETHEUS GAS','Station_12',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_12_3','DEDDIE','Station_12',0.2,00.025);
INSERT INTO `charging_point` VALUES ('Station_12_4','Volterra AE','Station_12',0.2,00.02);
INSERT INTO `charging_point` VALUES ('Station_12_5','ELPEDISON','Station_12',0.2,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 13 ----------
INSERT INTO `charging_point` VALUES ('Station_13_1','ZeniΘ','Station_13',0.2,00.02);
INSERT INTO `charging_point` VALUES ('Station_13_2','WATT+VOLT','Station_13',0.1667,00.02);
INSERT INTO `charging_point` VALUES ('Station_13_3','ELPEDISON','Station_13',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_13_4','DEDDIE','Station_13',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_13_5','Volterra AE','Station_13',0.1667,00.04);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 14 ----------
INSERT INTO `charging_point` VALUES ('Station_14_1','Protergia','Station_14',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_14_2','PROMETHEUS GAS','Station_14',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_14_3','WATT+VOLT','Station_14',0.1667,00.04);
INSERT INTO `charging_point` VALUES ('Station_14_4','DEDDIE','Station_14',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_14_5','Volterra AE','Station_14',0.2,00.04);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 15 ----------
INSERT INTO `charging_point` VALUES ('Station_15_1','ELPEDISON','Station_15',0.2,00.02);
INSERT INTO `charging_point` VALUES ('Station_15_2','WATT+VOLT','Station_15',0.2,00.02);
INSERT INTO `charging_point` VALUES ('Station_15_3','ZeniΘ','Station_15',0.2,00.02);
INSERT INTO `charging_point` VALUES ('Station_15_4','Protergia','Station_15',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_15_5','ELPEDISON','Station_15',0.1667,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 16 ----------
INSERT INTO `charging_point` VALUES ('Station_16_1','Volterra AE','Station_16',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_16_2','DEDDIE','Station_16',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_16_3','WATT+VOLT','Station_16',0.2,00.04);
INSERT INTO `charging_point` VALUES ('Station_16_4','Volton','Station_16',0.2,00.04);
INSERT INTO `charging_point` VALUES ('Station_16_5','ELPEDISON','Station_16',0.1667,00.02);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 17 ----------
INSERT INTO `charging_point` VALUES ('Station_17_1','ELPEDISON','Station_17',0.2,00.025);
INSERT INTO `charging_point` VALUES ('Station_17_2','PROMETHEUS GAS','Station_17',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_17_3','Protergia','Station_17',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_17_4','Protergia','Station_17',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_17_5','DEDDIE','Station_17',0.2,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 18 ----------
INSERT INTO `charging_point` VALUES ('Station_18_1','ZeniΘ','Station_18',0.2,00.04);
INSERT INTO `charging_point` VALUES ('Station_18_2','Volton','Station_18',0.1667,00.04);
INSERT INTO `charging_point` VALUES ('Station_18_3','WATT+VOLT','Station_18',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_18_4','DEDDIE','Station_18',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_18_5','PROMETHEUS GAS','Station_18',0.2,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 19 ----------
INSERT INTO `charging_point` VALUES ('Station_19_1','ZeniΘ','Station_19',0.1667,00.04);
INSERT INTO `charging_point` VALUES ('Station_19_2','DEDDIE','Station_19',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_19_3','PROMETHEUS GAS','Station_19',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_19_4','ELPEDISON','Station_19',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_19_5','Volterra AE','Station_19',0.2,00.04);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 20 ----------
INSERT INTO `charging_point` VALUES ('Station_20_1','DEDDIE','Station_20',0.2,00.02);
INSERT INTO `charging_point` VALUES ('Station_20_2','WATT+VOLT','Station_20',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_20_3','WATT+VOLT','Station_20',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_20_4','Protergia','Station_20',0.2,00.035);
INSERT INTO `charging_point` VALUES ('Station_20_5','PROMETHEUS GAS','Station_20',0.2,00.04);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 21 ----------
INSERT INTO `charging_point` VALUES ('Station_21_1','DEDDIE','Station_21',0.1667,3);
INSERT INTO `charging_point` VALUES ('Station_21_2','Protergia','Station_21',0.2,3);
INSERT INTO `charging_point` VALUES ('Station_21_3','ZeniΘ','Station_21',0.1667,5);
INSERT INTO `charging_point` VALUES ('Station_21_4','Volton','Station_21',0.2,3);
INSERT INTO `charging_point` VALUES ('Station_21_5','PROMETHEUS GAS','Station_21',0.2,4);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 22 ----------
INSERT INTO `charging_point` VALUES ('Station_22_1','DEDDIE','Station_22',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_22_2','Volterra AE','Station_22',0.2,00.04);
INSERT INTO `charging_point` VALUES ('Station_22_3','WATT+VOLT','Station_22',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_22_4','ELPEDISON','Station_22',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_22_5','PROMETHEUS GAS','Station_22',0.1667,00.03);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 23 ----------
INSERT INTO `charging_point` VALUES ('Station_23_1','ZeniΘ','Station_23',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_23_2','DEDDIE','Station_23',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_23_3','Protergia','Station_23',0.2,00.035);
INSERT INTO `charging_point` VALUES ('Station_23_4','ELPEDISON','Station_23',0.1667,00.035);
INSERT INTO `charging_point` VALUES ('Station_23_5','Volton','Station_23',0.2,00.04);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 24 ----------
INSERT INTO `charging_point` VALUES ('Station_24_1','Volterra AE','Station_24',0.2,00.04);
INSERT INTO `charging_point` VALUES ('Station_24_2','DEDDIE','Station_24',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_24_3','WATT+VOLT','Station_24',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_24_4','PROMETHEUS GAS','Station_24',0.2,00.025);
INSERT INTO `charging_point` VALUES ('Station_24_5','ZeniΘ','Station_24',0.1667,00.04);
-- ------- ------- ------- ------- ------- -------
-- --------- Station 25 ----------
INSERT INTO `charging_point` VALUES ('Station_25_1','Protergia','Station_25',0.2,00.03);
INSERT INTO `charging_point` VALUES ('Station_25_2','ELPEDISON','Station_25',0.2,00.035);
INSERT INTO `charging_point` VALUES ('Station_25_3','WATT+VOLT','Station_25',0.1667,00.035);
INSERT INTO `charging_point` VALUES ('Station_25_4','DEDDIE','Station_25',0.1667,00.03);
INSERT INTO `charging_point` VALUES ('Station_25_5','Volton','Station_25',0.2,00.04);

-- -------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- ------------ SUBSCRIPTION ------------
-- AUTOMATED INSERTION

-- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
