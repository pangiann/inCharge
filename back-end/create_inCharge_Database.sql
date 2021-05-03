DROP DATABASE IF EXISTS `sql_inCharge` ;
CREATE DATABASE `sql_inCharge` ;
USE `sql_inCharge` ;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO" ;
SET time_zone = "+02:00" ;

select @@FOREIGN_KEY_CHECKS ;
set FOREIGN_KEY_CHECKS = 1 ;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- --  Data Base  -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `customer`
--
CREATE TABLE `customer` (
	`Username` varchar(50) NOT NULL,				-- Primary Key
	`Car_ID` varchar(100) NOT NULL,					-- Foreign Key
    `Password` varbinary(50) NOT NULL,
    `Salt` varbinary(50) NOT NULL,
    `First_Name` varchar(20) NOT NULL,
    `Last_Name` varchar(20) NOT NULL,
    `Points` int(11) DEFAULT NULL,
    `Birth_Date` date NOT NULL,
    `City` varchar(20) DEFAULT NULL,
    `Street_Name` varchar(40) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Family_Members` varchar(20) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `customer`
-- dump data in inCharge_Data_Insertion


--
-- Trigger_1 `customer`
--
DELIMITER $$
CREATE TRIGGER `Customer_family_state` BEFORE INSERT ON `customer`
FOR EACH ROW BEGIN
		IF (NEW.Family_Members is NULL OR NEW.Family_Members = '')
        THEN
			SET NEW.Family_Members = 'Unknown';
	END IF;
END
$$
DELIMITER ;
--
-- Trigger_2 `customer`
--
DELIMITER $$
CREATE TRIGGER `Customer_points` BEFORE INSERT ON `customer`
FOR EACH ROW BEGIN
		IF (NEW.POINTS is NULL)
        THEN
			SET NEW.POINTS = 0;
	END IF;
END
$$
DELIMITER ;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `administrator`
--
CREATE TABLE `superadmin` (
	`Superadmin_ID` varchar(50) NOT NULL,						-- Primary Key
    `Password` varbinary(50) NOT NULL,
    `Salt` varbinary(50) NOT NULL,
		`First_Name` varchar(20) NOT NULL,
    `Last_Name` varchar(20) NOT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL,
		PRIMARY KEY (`Superadmin_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `administrator`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `administrator`
--
CREATE TABLE `administrator` (
	`Administrator_No` varchar(50) NOT NULL,						-- Primary Key
    `Password` varbinary(50) NOT NULL,
    `Salt` varbinary(50) NOT NULL,
	`First_Name` varchar(20) NOT NULL,
    `Last_Name` varchar(20) NOT NULL,
    `Birth_Date` date NOT NULL,
    `Working_Company` varchar(50) NOT NULL,			-- Foreign Key -> will be distributors PK
    `City` varchar(20) DEFAULT NULL,
    `Street_Name` varchar(40) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Family_Members` varchar(20) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `administrator`
-- dump data in inCharge_Data_Insertion

--
-- Trigger `administrator`
--
DELIMITER $$
CREATE TRIGGER `Administrator_family_state` BEFORE INSERT ON `administrator`
FOR EACH ROW BEGIN
		IF (NEW.Family_Members is NULL OR NEW.Family_Members = '')
        THEN
			SET NEW.Family_Members = 'Unknown';
	END IF;
END
$$
DELIMITER ;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `boss`
--
CREATE TABLE `boss` (
	`Boss_No` varchar(50) NOT NULL,							-- Primary Key
    `Password` varbinary(50) NOT NULL,
    `Salt` varbinary(50) NOT NULL,
	`First_Name` varchar(20) NOT NULL,
    `Last_Name` varchar(20) NOT NULL,
    `Birth_Date` date DEFAULT NULL,
    `Working_Company` varchar(50) NOT NULL,			-- Foreign Key -> will be distributors PK
    `City` varchar(20) DEFAULT NULL,
    `Street_Name` varchar(40) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Family_Members` varchar(20) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Boss`
-- dump data in inCharge_Data_Insertion

--
-- Trigger `boss`
--
DELIMITER $$
CREATE TRIGGER `Boss_family_state` BEFORE INSERT ON `boss`
FOR EACH ROW BEGIN
		IF (NEW.Family_Members is NULL OR NEW.Family_Members = '')
        THEN
			SET NEW.Family_Members = 'Unknown';
	END IF;
END
$$
DELIMITER ;


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `car`
--
CREATE TABLE `car` (
	`car_No` varchar(100) NOT NULL,						-- Primary Key
	`brand` varchar(20) NOT NULL,						-- Foreign Key
    `model` varchar(20) NOT NULL,
		`type` varchar(10) NOT NULL,
    `capacitance` decimal(7,2) NOT NULL,
    `release_year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Car`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `manufacturer`
--
CREATE TABLE `manufacturer` (
	`Brand_Name` varchar(50) NOT NULL,			-- Primary Key
	`City` varchar(20) DEFAULT NULL,
    `Street_Name` varchar(40) DEFAULT NULL,
    `Streen_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Car_Manufacturer`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `charging_session`
--
CREATE TABLE `charging_session` (
	`Session_No` int(11) NOT NULL AUTO_INCREMENT,		-- Primary Key
    `Customer_ID` varchar(50) NOT NULL,					-- Foreign Key
    `Point_ID` varchar(50) NOT NULL,					-- Foreign Key
		`Protocol` varchar(50) NOT NULL,
		`Type` varchar(20) NOT NULL,
    `Points` int(11) NOT NULL,
    `Date` date NOT NULL,
    `Start_Time` time NOT NULL,
    `End_Time` time NOT NULL,
    `Amount` decimal(7,2) NOT NULL,
    `Energy` decimal(9,2) NOT NULL,
    PRIMARY KEY (Session_No)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `charging_session`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `charging_station`
--
CREATE TABLE `charging_station` (
	`Station_No` varchar(50) NOT NULL,					-- Primary Key
	`City` varchar(20) NOT NULL,
	`Street` varchar(20) NOT NULL,
	`Number` int(11) NOT NULL,
    `Operator` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Charging_Station`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `charging_point`
--
CREATE TABLE `charging_point` (
	`Point_No` varchar(50) NOT NULL,						-- Primary Key
    `Distributor_ID` varchar(50) NOT NULL,					-- Foreign Key
    `Station_ID` varchar(50) NOT NULL,						-- Foreign Key
    `Charging_Rate` decimal(7,2) NOT NULL,			-- this is KWh per minute
    `Cost_per_KWh` decimal(7,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Charging_Station`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `electricity_distributor`
--
CREATE TABLE `distributor` (
	`Distributor_Name` varchar(50) NOT NULL,			-- Primary Key
    `Producer_ID` varchar(50) NOT NULL,					-- Foreign Key
    `KWh_Price` decimal(7,2) NOT NULL,
    `Contract` decimal(7,2) DEFAULT NULL,
	`City` varchar(20) DEFAULT NULL,
	`Street_Name` varchar(40) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Webpage` varchar(100) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Electricity_Distributor`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `subscription`
--
CREATE TABLE `subscription` (
	`Subscription_No` int(11) NOT NULL AUTO_INCREMENT,				-- Primary Key
    `Customer_ID` varchar(50) NOT NULL, 							-- Foreign Key
    `Supplier_ID` varchar(50) NOT NULL,								-- Foreign Key
    `Price` decimal(7,2) NOT NULL,
    `Last_paid` date DEFAULT NULL,
    `Last_issued` date DEFAULT NULL,
    PRIMARY KEY (`Subscription_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Subscription`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `electricity_producer`
--
CREATE TABLE `producer` (
	`Producer_Name` varchar(50) NOT NULL,				-- Primary Key
	`City` varchar(20) DEFAULT NULL,
	`Street_Name` varchar(40) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Electricity_Producer`
-- dump data in inCharge_Data_Insertion

-- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- Primary Keys -- -- -- -- -- -- -- -- -- --
--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
	ADD PRIMARY KEY (`Username`);

--
-- Indexes for table `administrator`
--
ALTER TABLE `administrator`
	ADD PRIMARY KEY (`Administrator_No`);

--
-- Indexes for table `boss`
--
ALTER TABLE `boss`
	ADD PRIMARY KEY (`Boss_No`);

--
-- Indexes for table `car`
--
ALTER TABLE `car`
	ADD PRIMARY KEY (`car_No`);

--
-- Indexes for table `manufacturer`
--
ALTER TABLE `manufacturer`
	ADD PRIMARY KEY (`Brand_Name`);

--
-- Indexes for table `charging_station`
--
ALTER TABLE `charging_station`
	ADD PRIMARY KEY (`Station_No`);

--
-- Indexes for table `charging_point`
--
ALTER TABLE `charging_point`
	ADD PRIMARY KEY (`Point_No`);

--
-- Indexes for table `electricity_distributor`
--
ALTER TABLE `distributor`
	ADD PRIMARY KEY (`Distributor_Name`);

--
-- Indexes for table `electricity_producer`
--
ALTER TABLE `producer`
	ADD PRIMARY KEY (`Producer_Name`);

-- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- Foreign Keys -- -- -- -- -- -- -- -- -- --

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
    ADD CONSTRAINT `FK_Car_Owner_ID` FOREIGN KEY
    (`Car_ID`) REFERENCES `car` (`Car_No`)
    ON DELETE CASCADE;

--
-- Constraints for table `administrator`
--
ALTER TABLE `administrator`
    ADD CONSTRAINT `FK_Working_Company_Admin` FOREIGN KEY
    (`Working_Company`) REFERENCES `distributor` (`Distributor_Name`)
    ON DELETE CASCADE;

--
-- Constraints for table `boss`
--
ALTER TABLE `boss`
    ADD CONSTRAINT `FK_Working_Company_Boss` FOREIGN KEY
    (`Working_Company`) REFERENCES `distributor` (`Distributor_Name`)
    ON DELETE CASCADE;

--
-- Constraints for table `car`
--
ALTER TABLE `car`
    ADD CONSTRAINT `FK_Brand` FOREIGN KEY
    (`brand`) REFERENCES `manufacturer` (`Brand_Name`)
    ON DELETE CASCADE;

--
-- Constraints for table `charging_session`
--
ALTER TABLE `charging_session`
    ADD CONSTRAINT `FK_Customer_ID` FOREIGN KEY
    (`Customer_ID`) REFERENCES `customer` (`Username`)
    ON DELETE CASCADE,
    ADD CONSTRAINT `FK_Point_ID` FOREIGN KEY
    (`Point_ID`) REFERENCES `charging_point` (`Point_No`)
    ON DELETE CASCADE;

--
-- Constraints for table `charging_point`
--
ALTER TABLE `charging_point`
    ADD CONSTRAINT `FK_Distributor_ID` FOREIGN KEY
    (`Distributor_ID`) REFERENCES `distributor` (`Distributor_Name`)
    ON DELETE CASCADE,
    ADD CONSTRAINT `FK_Station_ID` FOREIGN KEY
    (`Station_ID`) REFERENCES `charging_station` (`Station_No`)
    ON DELETE CASCADE;

--
-- Constraints for table `distributor`
--
ALTER TABLE `distributor`
    ADD CONSTRAINT `FK_Producer_ID` FOREIGN KEY
    (`Producer_ID`) REFERENCES `producer` (`Producer_Name`)
    ON DELETE CASCADE;

--
-- Constraionts for table `subscription`
--
ALTER TABLE `subscription`
	ADD CONSTRAINT `FK_Customer_IF` FOREIGN KEY
    (`Customer_ID`) REFERENCES `customer` (`Username`)
    ON DELETE CASCADE,
    ADD CONSTRAINT `FK_Supplier_ID` FOREIGN KEY
    (`Supplier_ID`) REFERENCES `distributor` (`Distributor_Name`)
    ON DELETE CASCADE;

-- ------------------------------------------------------------------
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
