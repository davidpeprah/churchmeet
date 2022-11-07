-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: churchmeet
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `friends`
--

DROP TABLE IF EXISTS `friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friends` (
  `friends_id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(16) DEFAULT NULL,
  `friend` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`friends_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friends`
--

LOCK TABLES `friends` WRITE;
/*!40000 ALTER TABLE `friends` DISABLE KEYS */;
INSERT INTO `friends` VALUES (2,'Sarah','david'),(3,'parhin','david'),(16,'david','Sarah'),(17,'david','david'),(18,'adwoa','adwoa'),(19,'david','parhin'),(21,'adwoa','Sarah'),(22,'adwoa','parhin'),(25,'adwoa','david'),(27,'david','adwoa'),(28,'abena','abena'),(29,'yaw','yaw'),(30,'ama','ama'),(31,'akua','akua'),(32,'Kofi','Kofi'),(33,'afia','afia'),(34,'yaa','yaa'),(35,'Kwasi','Kwasi'),(36,'kwaku','kwaku'),(37,'kwame','kwame'),(38,'kwabena','kwabena');
/*!40000 ALTER TABLE `friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `members` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  `password` varchar(16) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (1,'david','david','david@awesoft.org'),(2,'Sarah','sarah','sarah@awesoft.com'),(3,'parhin','password','parhin@awesoft.com'),(4,'adwoa','password','adwoa@awesoft.com'),(5,'abena','password','abena@yahoo.com'),(6,'yaw','passwod','yaw2@yahoo.com'),(7,'ama','password','ama3@yahoo.com'),(8,'akua','password','akua4@yahoo.com'),(9,'Kofi','password','kofi5@yahoo.com'),(10,'afia','password','afia6@yahoo.com'),(11,'yaa','password','yaa6@yahoo.com'),(12,'Kwasi','password','kwasi7@yahoo.com'),(13,'kwaku','password','kwaku8@yahoo.com'),(14,'kwame','password','kwame9@yahoo.com'),(15,'kwabena','password','kwabena10@yahoo.com');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `message_id` int unsigned NOT NULL AUTO_INCREMENT,
  `auth` varchar(16) DEFAULT NULL,
  `time` datetime(6) NOT NULL,
  `message` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (2,'david','2021-05-05 22:23:21.000000','Hello, World!'),(3,'david','2021-05-05 23:11:11.000000',' Give Thanks to God'),(4,'adwoa','2021-05-05 23:15:46.000000',' God is Good and His Mercies Endure forever...!!'),(5,'adwoa','2021-05-05 23:21:59.000000',' SING HIS PRAISE OH MY SOUL');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pmessages`
--

DROP TABLE IF EXISTS `pmessages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pmessages` (
  `pmessages` int unsigned NOT NULL AUTO_INCREMENT,
  `sender` varchar(10) NOT NULL,
  `receiver` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `message` varchar(500) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pmessages`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pmessages`
--

LOCK TABLES `pmessages` WRITE;
/*!40000 ALTER TABLE `pmessages` DISABLE KEYS */;
INSERT INTO `pmessages` VALUES (1,'david','sarah','2021-05-13','I love You','2021-05-14 03:41:29'),(2,'sarah','david','2021-05-13','I love You too','2021-05-14 03:49:36'),(3,'david','parhin','2021-05-13','Thanks for your sacrifices','2021-05-14 03:50:11'),(4,'david','Sarah','2021-05-24',' Missing you like crazy','2021-05-25 02:38:23'),(5,'david','Sarah','2021-05-24',' How is my Baby','2021-05-25 02:39:39'),(6,'david','parhin','2021-05-24',' How is the family doing?','2021-05-25 02:48:11'),(7,'Sarah','parhin','2021-05-24',' I\'m good by God\'s grace','2021-05-25 03:02:57'),(8,'Sarah','david','2021-05-24',' Doing good by Grace','2021-05-25 03:04:10'),(9,'david','Sarah','2021-05-24',' <strong>Love is Here!</strong>','2021-05-25 03:31:19'),(10,'david','Sarah','2021-05-25',' Hello World..!!','2021-05-26 02:01:44');
/*!40000 ALTER TABLE `pmessages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles` (
  `profile_id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(16) DEFAULT NULL,
  `text` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`profile_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-28 14:27:26
