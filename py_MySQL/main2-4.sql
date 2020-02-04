-- MySQL dump 10.13  Distrib 8.0.19, for Linux (x86_64)
--
-- Host: localhost    Database: main
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `main`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `main` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `main`;

--
-- Table structure for table `companiesBasic`
--

DROP TABLE IF EXISTS `companiesBasic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companiesBasic` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `website` varchar(500) NOT NULL,
  `scope` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companiesBasic`
--

LOCK TABLES `companiesBasic` WRITE;
/*!40000 ALTER TABLE `companiesBasic` DISABLE KEYS */;
INSERT INTO `companiesBasic` VALUES (1,'Cloudinary','Cloudinary','Cloudinary'),(2,'Algorand','http://www.algorand.com/','Algorand Node - https://github.com/algorand/go-algorand; Algorand JavaScript SDK - https://github.com/algorand/js-algorand-sdk; Algorand Java SDK - https://github.com/algorand/java-algorand-sdk; Algorand Golang SDK - https://github.com/algorand/go-algorand-sdk; Algorand Ledger App - https://github.com/algorand/ledger-app-algorand; Algorand TestNet'),(3,'Bitdefender','https://www.bitdefender.com/','*.bitdefender.com; *.bitdefender.net; Bitdefender Total Security 2019; Bitdefender GravityZone Business Security'),(4,'Zilliqa','https://zilliqa.com/','https://github.com/Zilliqa/Zilliqa; https://github.com/Zilliqa/scilla; https://github.com/Zilliqa/savant-ide; https://savant-ide.zilliqa.com; https://github.com/Zilliqa/Zilliqa-JavaScript-Library); Moonlet-core JS library (https://github.com/cryptolandtech/moonlet-core/releases/tag/v0.0.1); Moonlet wallet Chrome extension (https://github.com/cryptolandtech/moonlet/releases); https://github.com/Zilliqa/nucleus-wallet); https://dev-wallet.zilliqa.com/; https://learnscilla.com/;'),(5,'Caffeine','https://www.caffeine.tv/','https://www.caffeine.tv/; https://api.caffeine.tv/; https://payments.caffeine.tv; https://realtime.caffeine.tv/; https://preview.caffeine.tv/; https://images.caffeine.tv/; https://static.caffeine.tv/; https://build.caffeine.tv/; caffeine.exe; caffeine-helper.x86.exe; caffeine-helper.x64.exe; Caffeine iOS; *.rtcdn.caffeine.tv'),(6,'Cloudinary','https://cloudinary.com/documentation','https://cloudinary.com/console; https://api.cloudinary.com; https://res.cloudinary.com; widget.cloudinary.com');
/*!40000 ALTER TABLE `companiesBasic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `id` int NOT NULL,
  `ip` varchar(40) NOT NULL,
  `time` varchar(50) NOT NULL,
  `browser` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logginAttempts`
--

DROP TABLE IF EXISTS `logginAttempts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logginAttempts` (
  `username` varchar(50) NOT NULL,
  `atempts` int NOT NULL,
  `numOfBans` int NOT NULL,
  `time1` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ip` varchar(30) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logginAttempts`
--

LOCK TABLES `logginAttempts` WRITE;
/*!40000 ALTER TABLE `logginAttempts` DISABLE KEYS */;
INSERT INTO `logginAttempts` VALUES ('12',1,0,'2020-02-04 19:05:02','10.1.120.54',1),('12',2,1,'2020-02-04 19:05:06','10.1.120.54',2);
/*!40000 ALTER TABLE `logginAttempts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logins1`
--

DROP TABLE IF EXISTS `logins1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logins1` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `ip` varchar(30) NOT NULL,
  `time1` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logins1`
--

LOCK TABLES `logins1` WRITE;
/*!40000 ALTER TABLE `logins1` DISABLE KEYS */;
INSERT INTO `logins1` VALUES (1,'admin','10.1.160.167','2020-02-04 05:54:11'),(2,'admin','10.1.160.167','2020-02-04 05:54:11'),(3,'admin','10.1.160.167','2020-02-04 05:54:11'),(4,'admin','10.1.120.54','2020-02-04 05:54:11'),(5,'admin','10.1.120.54','2020-02-04 05:56:44'),(6,'admin','10.1.120.54','2020-02-04 06:24:01'),(7,'booty','10.1.120.54','2020-02-04 06:25:04'),(8,'admin','10.1.120.54','2020-02-04 18:31:20'),(9,'admin','10.1.120.54','2020-02-04 19:09:28'),(10,'admin','10.1.120.54','2020-02-04 19:57:20'),(11,'admin','10.1.120.54','2020-02-04 21:16:27');
/*!40000 ALTER TABLE `logins1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t1`
--

DROP TABLE IF EXISTS `t1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t1` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t1`
--

LOCK TABLES `t1` WRITE;
/*!40000 ALTER TABLE `t1` DISABLE KEYS */;
/*!40000 ALTER TABLE `t1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','$2y$10$1smLX1efqIQJ/LbDGy/tp.KyAX3hwtVZEm1UxzSyXJZZJuwKRrdrq','2020-02-04 05:56:41'),(2,'booty','$2y$10$JbScN.gKrnumYQYFh2hAiOYWhilQiOqgIfwfDlzzvrtxoPYDdvRia','2020-02-04 06:23:40');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-04 16:54:28
