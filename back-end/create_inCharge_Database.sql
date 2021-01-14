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
	`Customer_No` int(11) NOT NULL,						-- Primary Key
	`First_Name` varchar(20) NOT NULL,
    `Last_Name` varchar(20) NOT NULL,
    `Password` varchar(60) NOT NULL,
    `Points` int(11) DEFAULT NULL,
    `Birth_Date` date NOT NULL,
    `City` varchar(20) DEFAULT NULL,
    `Street_Name` varchar(20) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Family_Members` varchar(20) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
    
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `customer`
--
-- MAYBE DUMP DATA HERE

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
CREATE TABLE `administrator` (
	`Administrator_No` int(11) NOT NULL,					-- Primary Key
	`First_Name` varchar(20) NOT NULL,
    `Last_Name` varchar(20) NOT NULL,
    `Password` varchar(60) NOT NULL,
    `Birth_Date` date NOT NULL,
    `Working_Company` varchar(50) NOT NULL,
    `City` varchar(20) DEFAULT NULL,
    `Street_Name` varchar(20) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Family_Members` varchar(20) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `administrator`
--
-- MAYBE DUMP DATA HERE

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
	`Boss_No` int(11) NOT NULL,							-- Primary Key
	`First_Name` varchar(20) NOT NULL,
    `Last_Name` varchar(20) NOT NULL,
    `Password` varchar (60) NOT NULL,
    `Birth_Date` date NOT NULL,
    `City` varchar(20) DEFAULT NULL,
    `Street_Name` varchar(20) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Family_Members` varchar(20) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Boss`
--
-- MAYBE DUMP DATA HERE

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
	`Car_No` bigint(21) NOT NULL,						-- Primary Key
    `Car_Owner_ID` int(11) NOT NULL,					-- Foreign Key
    `Manufacturer_ID` varchar(50) NOT NULL,				-- Foreign Key
	`Brand` varchar(20) NOT NULL,
    `Model` varchar(20) NOT NULL,
    `Capacitance` decimal(7,2) NOT NULL,
    `Year` int(11) DEFAULT NULL,
    `Price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Car`
--
-- MAYBE DUMP DATA HERE


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `manufacturer`
--
CREATE TABLE `manufacturer` (
	`Manufacturer_Name` varchar(50) NOT NULL,			-- Primary Key
	`City` varchar(20) DEFAULT NULL,
    `Street_Name` varchar(20) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Car_Manufacturer`
--
-- MAYBE DUMP DATA HERE


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `transaction`
--
CREATE TABLE `transaction` (
	`Transaction_No` int(11) NOT NULL,					-- Primary Key
    `Customer_ID` int(11) NOT NULL,						-- Foreign Key
    `Station_ID` int(11) NOT NULL,						-- Foreign Key
	`Type` varchar(20) NOT NULL,
    `Points` int(11) NOT NULL,
    `Date` date NOT NULL,
    `Time` time NOT NULL,
    `Amount` decimal(7,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Transaction`
--
-- MAYBE DUMP DATA HERE


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `charging_station`
--
CREATE TABLE `charging_station` (
	`Station_No` int(11) NOT NULL,						-- Primary Key
    `Distributor_ID` varchar(50) NOT NULL,				-- Foreign Key
	`City` varchar(20) NOT NULL,
	`Street` varchar(20) NOT NULL,
    `Charging_Rate` decimal(7,2) NOT NULL,
    `Cost_per_KW` decimal(7,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Charging_Station`
--
-- MAYBE DUMP DATA HERE


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `electricity_distributor`
--
CREATE TABLE `distributor` (
	`Distributor_Name` varchar(50) NOT NULL,			-- Primary Key
    `Producer_ID` varchar(50) NOT NULL,					-- Foreign Key
    `KW_Price` decimal(7,2) NOT NULL,
	`City` varchar(20) DEFAULT NULL,
	`Street_Name` varchar(20) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Electricity_Distributor`
--
-- MAYBE DUMP DATA HERE


-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

--
-- Table structure for table `electricity_producer`
--
CREATE TABLE `producer` (
	`Producer_Name` varchar(50) NOT NULL,				-- Primary Key
	`City` varchar(20) DEFAULT NULL,
	`Street_Name` varchar(20) DEFAULT NULL,
    `Street_Number` int(11) DEFAULT NULL,
    `Postal_Code` int(11) DEFAULT NULL,
    `Email` varchar(50) DEFAULT NULL,
    `Phone` bigint(21) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
--
-- Dumping data for table `Electricity_Producer`
--
-- MAYBE DUMP DATA HERE

-- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- Primary Keys -- -- -- -- -- -- -- -- -- --
--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
	ADD PRIMARY KEY (`Customer_No`);

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
	ADD PRIMARY KEY (`Car_No`);

--
-- Indexes for table `manufacturer`
--
ALTER TABLE `manufacturer`
	ADD PRIMARY KEY (`Manufacturer_Name`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
	ADD PRIMARY KEY (`Transaction_No`);

--
-- Indexes for table `charging_station`
--
ALTER TABLE `charging_station`
	ADD PRIMARY KEY (`Station_No`);

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
-- Constraints for table `car` 
--
ALTER TABLE `car`
    ADD CONSTRAINT `FK_Car_Owner_ID` FOREIGN KEY
    (`Car_Owner_ID`) REFERENCES `customer` (`Customer_No`) 
    ON DELETE CASCADE,
    ADD CONSTRAINT `FK_Manufacturer_ID` FOREIGN KEY
    (`Manufacturer_ID`) REFERENCES `manufacturer` (`Manufacturer_Name`) 
    ON DELETE CASCADE;
    
--
-- Constraints for table `transaction` 
--
ALTER TABLE `transaction`
    ADD CONSTRAINT `FK_Customer_ID` FOREIGN KEY
    (`Customer_ID`) REFERENCES `customer` (`Customer_No`) 
    ON DELETE CASCADE,
    ADD CONSTRAINT `FK_Station_ID` FOREIGN KEY
    (`Station_ID`) REFERENCES `charging_station` (`Station_No`) 
    ON DELETE CASCADE;
    
--
-- Constraints for table `charging_station` 
--
ALTER TABLE `charging_station`
    ADD CONSTRAINT `FK_Distributor_ID` FOREIGN KEY
    (`Distributor_ID`) REFERENCES `distributor` (`Distributor_Name`) 
    ON DELETE CASCADE;
    
--
-- Constraints for table `distributor` 
--
ALTER TABLE `distributor`
    ADD CONSTRAINT `FK_Producer_ID` FOREIGN KEY
    (`Producer_ID`) REFERENCES `producer` (`Producer_Name`) 
    ON DELETE CASCADE;

-- ------------------------------------------------------------------    
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
