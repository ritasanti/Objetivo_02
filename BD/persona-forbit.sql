-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: persona
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `estado`
--

DROP TABLE IF EXISTS `estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado` (
  `id` int NOT NULL DEFAULT '1',
  `descrip` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `estado_chk_1` CHECK ((`id` in (1,2)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado`
--

LOCK TABLES `estado` WRITE;
/*!40000 ALTER TABLE `estado` DISABLE KEYS */;
INSERT INTO `estado` VALUES (1,'ACTIVO'),(2,'INACTIVO');
/*!40000 ALTER TABLE `estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `id` int NOT NULL AUTO_INCREMENT,
  `apellido` varchar(100) DEFAULT NULL,
  `nombres` varchar(100) DEFAULT NULL,
  `dni` varchar(8) DEFAULT NULL,
  `domicilio` varchar(100) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `id_estado` int DEFAULT NULL,
  `fecHora_registro` date DEFAULT NULL,
  `fecHora_modificacion` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_estado` (`id_estado`),
  CONSTRAINT `persona_ibfk_1` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,'Soria','Emanuel','45789342','Av.Moreno 661-Capital','3856620965',2,'2024-09-10',NULL),(2,'Vittor','Roque','40123654','Av.Roca(S)54-Capital','3855359930',1,'2024-09-10',NULL),(3,'Silvera','Andres','40123654','Av.Belgrano 67-Rio Hondo','44987213',1,'2024-09-10',NULL),(4,'Regueiro','Mario','41023654','Gorriti 67-Capital','3815478981',2,'2024-09-10',NULL),(7,'Palermo','Martin','40928578','Patagonia 23','385986464',1,'2024-09-17',NULL),(8,'FORMICA','MAURO','35123478','Pje 330(s)','3817549621',2,'2024-09-19',NULL),(9,'FORMICA','MARTIN','35123474','Pje 330(N)','3817549610',1,'2024-09-20',NULL),(11,'Riccardo','Carlos','40754209','Pje 440','4225137',1,'2024-09-19',NULL),(12,'Paoletti','Domingo','40754209','Pje 447','4225138',2,'2024-09-19',NULL);
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'persona'
--
/*!50003 DROP PROCEDURE IF EXISTS `SP_ConsultarPersona` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `SP_ConsultarPersona`()
begin
select apellido,nombres,dni,domicilio,telefono,fechora_registro
from persona
where id_estado = 1;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `SP_REGISTROPERSONA` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `SP_REGISTROPERSONA`(
IN P_APELLIDO VARCHAR(100),
IN P_NOMBRES VARCHAR(100),
IN P_DNI VARCHAR(8),
IN P_DOMICILIO VARCHAR(100),
IN P_TELEFONO VARCHAR(15),
IN P_ID_ESTADO INT,
IN P_FECHORA_REGISTRO DATE)
BEGIN
INSERT INTO PERSONA(APELLIDO,NOMBRES,DNI,DOMICILIO,TELEFONO,ID_ESTADO,FECHORA_REGISTRO)
VALUES(P_APELLIDO,P_NOMBRES,P_DNI,P_DOMICILIO,P_TELEFONO,P_ID_ESTADO,P_FECHORA_REGISTRO);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-23 20:29:51
