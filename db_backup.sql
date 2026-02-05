/*M!999999\- enable the sandbox mode */
-- MariaDB dump 10.19  Distrib 10.11.14-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: audit_support
-- ------------------------------------------------------
-- Server version       10.11.14-MariaDB-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `company_code` varchar(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `company_code` (`company_code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES
(1,'2026-01-25 05:16:41.701338','2026-01-25 05:16:41.701371','6290803003487','合同会社　イーライフ',1);
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `office`
--

DROP TABLE IF EXISTS `office`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `office` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `office_code` varchar(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `opened_on` date NOT NULL,
  `closed_on` date DEFAULT NULL,
  `company_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `office_code` (`office_code`),
  KEY `group_home_office_company_id_0cc86502_fk_group_home_company_id` (`company_id`),
  CONSTRAINT `group_home_office_company_id_0cc86502_fk_group_home_company_id` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `office`
--

LOCK TABLES `office` WRITE;
/*!40000 ALTER TABLE `office` DISABLE KEYS */;
INSERT INTO `office` VALUES
(1,'2026-01-25 05:20:25.303439','2026-01-25 05:20:25.303469','U0001','グループホーム　錬心館','2020-08-04',NULL,1),
(2,'2026-02-03 11:17:17.906295','2026-02-03 11:17:17.906331','U0002','清新館','2020-01-01',NULL,1);
/*!40000 ALTER TABLE `office` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resident`
--

DROP TABLE IF EXISTS `resident`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `resident` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `resident_code` varchar(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `birth_date` date NOT NULL,
  `care_level` int(11) DEFAULT 1,
  `room_number` varchar(20) DEFAULT '',
  `diagnosis` text DEFAULT NULL,
  `emergency_contact` text DEFAULT NULL,
  `notes` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resident_code` (`resident_code`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resident`
--

LOCK TABLES `resident` WRITE;
/*!40000 ALTER TABLE `resident` DISABLE KEYS */;
INSERT INTO `resident` VALUES
(1,'2026-01-25 05:22:41.884675','2026-01-25 05:22:41.884712','TEST01','テスト用イーライフ','2000-01-01',1,'',NULL,NULL,NULL),
(2,'2026-02-04 05:35:44.000000','2026-02-04 05:50:00.000000','1','和佐野 恭子','2026-02-03',1,'',NULL,NULL,NULL),
(3,'2026-02-04 05:35:46.000000','2026-02-04 05:50:01.000000','2','木本洋子','2026-02-04',1,'',NULL,NULL,NULL),
(4,'2026-02-04 05:35:48.000000','2026-02-04 05:50:03.000000','3','清永 祐以子','2026-02-04',1,'',NULL,NULL,NULL),
(5,'2026-02-04 05:35:50.000000','2026-02-04 05:50:04.000000','4','高須 幸恵','2026-02-04',1,'',NULL,NULL,NULL),
(6,'2026-02-04 05:35:52.000000','2026-02-04 05:50:05.000000','5','吉田 有佐','2026-02-04',1,'',NULL,NULL,NULL),
(7,'2026-02-04 05:35:53.000000','2026-02-04 05:50:06.000000','6','岩崎 奈々','2026-02-04',1,'',NULL,NULL,NULL),
(8,'2026-02-04 05:35:54.000000','2026-02-04 05:50:07.000000','7','河野 明日香','2026-02-04',1,'',NULL,NULL,NULL),
(9,'2026-02-04 05:35:55.000000','2026-02-04 05:50:08.000000','8','石松 勇樹','2026-02-04',2,'',NULL,NULL,NULL),
(10,'2026-02-04 05:35:56.000000','2026-02-04 05:50:09.000000','9','林 修平','2026-02-04',2,'',NULL,NULL,NULL),
(11,'2026-02-04 05:35:57.000000','2026-02-04 05:50:10.000000','10','辻 直樹','2026-02-04',2,'',NULL,NULL,NULL),
(12,'2026-02-04 05:35:59.000000','2026-02-04 05:50:10.000000','11','岡田 拓也','2026-02-04',2,'',NULL,NULL,NULL),
(13,'2026-02-04 05:36:01.000000','2026-02-04 05:50:12.000000','12','藤岡 俊幸','2026-02-04',2,'',NULL,NULL,NULL),
(14,'2026-02-04 05:36:03.000000','2026-02-04 05:50:13.000000','13','伊藤 毅','2026-02-04',2,'',NULL,NULL,NULL),
(15,'2026-02-04 05:36:05.000000','2026-02-04 05:50:14.000000','14','太田 勝治','2026-02-04',2,'',NULL,NULL,NULL),
(16,'2026-02-04 05:36:07.000000','2026-02-04 05:50:15.000000','15','瓜生 有孝','2026-02-04',2,'',NULL,NULL,NULL),
(17,'2026-02-04 05:36:08.000000','2026-02-04 05:50:16.000000','16','甲斐 慎之介','2026-02-04',2,'',NULL,NULL,NULL),
(18,'2027-02-04 05:36:09.000000','2026-02-04 05:50:17.000000','17','藤本 龍政','2026-02-04',2,'',NULL,NULL,NULL);
/*!40000 ALTER TABLE `resident` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resident_office`
--

DROP TABLE IF EXISTS `resident_office`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `resident_office` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `started_on` date DEFAULT NULL,
  `ended_on` date DEFAULT NULL,
  `office_id` bigint(20) NOT NULL,
  `resident_id` bigint(20) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `resident_office_office_id_7cc95968_fk_group_home_office_id` (`office_id`),
  KEY `resident_office_resident_id_258c7769` (`resident_id`),
  CONSTRAINT `resident_office_office_id_7cc95968_fk_group_home_office_id` FOREIGN KEY (`office_id`) REFERENCES `office` (`id`),
  CONSTRAINT `resident_office_resident_id_258c7769_fk_group_home_resident_id` FOREIGN KEY (`resident_id`) REFERENCES `resident` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resident_office`
--

LOCK TABLES `resident_office` WRITE;
/*!40000 ALTER TABLE `resident_office` DISABLE KEYS */;
INSERT INTO `resident_office` VALUES
(1,'2026-01-25 05:22:41.885520','2026-01-25 13:21:42.263055','2020-09-01',NULL,2,1,'2025-12-01',NULL),
(2,'2025-02-04 05:40:09.000000',NULL,NULL,NULL,2,2,NULL,NULL),
(3,'2025-02-04 05:40:14.000000',NULL,NULL,NULL,2,3,NULL,NULL),
(4,'2026-02-04 05:40:16.000000',NULL,NULL,NULL,2,4,NULL,NULL),
(5,'2026-02-04 05:40:17.000000',NULL,NULL,NULL,2,5,NULL,NULL),
(6,'2026-02-04 05:40:19.000000',NULL,NULL,NULL,2,6,NULL,NULL),
(7,'2026-02-04 05:40:20.000000',NULL,NULL,NULL,2,7,NULL,NULL),
(8,'2026-02-04 05:40:21.000000',NULL,NULL,NULL,1,8,NULL,NULL),
(9,'2026-02-04 05:40:22.000000',NULL,NULL,NULL,1,9,NULL,NULL),
(10,'2026-02-04 05:40:23.000000',NULL,NULL,NULL,1,10,NULL,NULL),
(11,'2026-02-04 05:40:24.000000',NULL,NULL,NULL,1,11,NULL,NULL),
(12,'2026-02-04 05:40:25.000000',NULL,NULL,NULL,1,11,NULL,NULL),
(13,'2026-02-04 05:40:26.000000',NULL,NULL,NULL,1,12,NULL,NULL),
(14,'2026-02-04 05:40:27.000000',NULL,NULL,NULL,1,13,NULL,NULL),
(15,'2026-02-04 05:40:28.000000',NULL,NULL,NULL,1,14,NULL,NULL),
(16,'2026-02-04 05:40:29.000000',NULL,NULL,NULL,1,16,NULL,NULL),
(17,'2026-02-04 05:40:30.000000',NULL,NULL,NULL,1,17,NULL,NULL);
/*!40000 ALTER TABLE `resident_office` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-04 11:50:18

