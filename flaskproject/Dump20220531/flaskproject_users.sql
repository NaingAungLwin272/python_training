-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: flaskproject
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` text NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `profile` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `type` varchar(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (14,'naingnaing','addfwwqq@gmail.com','Naing27201','09784613543','Bago','2001-02-27','','0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,'0'),(15,'ak47332','ak47443@gmail.com','Naing27201','959254379675','Rakine','2022-05-18','','0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,'0'),(16,'naing','naingnaing@gmail.com','Naing27201','959254379675','dadfasdfa','2022-05-25','','0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,'1'),(21,'naingnaing','naingnaingn@gmail.com','Naing27201','95925437332','Yangon','1995-01-31','','0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,'0'),(22,'mth','mth@gmail.com','Naing27201','959254379675','asdfsadfasdsfasdf','2022-05-12','','0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,'1'),(23,'naingnaingaung','naingnaingaung@gmail.com','Naing27201','097655434553','adsdfasdfadf','2022-05-25','<FileStorage: \'2022-04-20.png\' (\'image/png\')>','0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,'1'),(24,'naingnaingaungaung','naingnaingaungaung@gmail.com','Naing27201','959254379675','asdfasdfasdfasd','2022-05-11','<FileStorage: \'2022-04-20.png\' (\'image/png\')>','0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,'1'),(25,'naing','adceeeds@gmail.com','Naing27201','097655434553','Yangon','2022-05-25','<FileStorage: \'2022-04-19 (1).png\' (\'image/png\')>','2022-05-23 22:17:05','2022-05-23 22:17:05',NULL,'1'),(26,'naing','asdfasewwwqq@gmail.com','Naing27201','23424421111','saddfasdfasdfasdf','2022-05-17','<FileStorage: \'2022-04-20.png\' (\'image/png\')>','2022-05-25 22:30:53','2022-05-25 22:30:53',NULL,'1'),(27,'naing','awwwewq@gmail.com','Naing27201','234244','saddfasdfasdfasdf','2022-05-19','<FileStorage: \'Logo RE1(green).png\' (\'image/png\')>','2022-05-25 22:48:42','2022-05-25 22:48:42',NULL,'0'),(28,'adsfsqweeffadda','adsfsqweeffadda@gmail.com','Naing27201','959254379675','asdfasdfasdfasd','2022-05-11','<FileStorage: \'Logo RE1(b).png\' (\'image/png\')>','2022-05-26 00:59:28','2022-05-26 00:59:28',NULL,'0'),(29,'naingaung27201','naingaunglwin27201@gmail.com','Naing27201','09784613543','Yangon','2002-02-26','<FileStorage: \'2022-04-20 (7).png\' (\'image/png\')>','2022-05-26 10:43:10','2022-05-26 10:43:10',NULL,'0'),(30,'naing','awweweee@gmail.com','Naing27201','959254379675','asdfasdfasdfadfa','2022-05-17','<FileStorage: \'2022-04-19.png\' (\'image/png\')>','2022-05-26 23:19:23','2022-05-26 23:19:23',NULL,'1'),(32,'naing','asdfasdfasddfwwwewrw@gmail.com','Naing27201','0955524411','dfadfadffaa','2022-05-12','<FileStorage: \'2022-04-20.png\' (\'image/png\')>','2022-05-28 13:59:20','2022-05-28 13:59:20',NULL,'0'),(33,'wewerqrer22@gmail.com','aweedddewwsa@gmail.com','Niang27201','959254379675','Bago','2022-05-25','<FileStorage: \'2022-04-19.png\' (\'image/png\')>','2022-05-28 15:30:18','2022-05-28 15:30:18',NULL,'0');
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

-- Dump completed on 2022-05-31  9:57:30
