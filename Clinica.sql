-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: Clinica
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.1

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
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mail` varchar(150) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idUser`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Andres','12345','example.mail.com','2023-02-21 13:02:01'),(2,'Carlos','2TqQPfV3JnjyLTq','example@mail.com','2023-03-07 13:02:05'),(3,'lalo25','124567','lalo25@gmail.com','2023-03-07 13:09:07'),(4,'Luis45','JBsLZRNNy3u5SVy','luis45@gmail.com','2023-03-07 15:20:30'),(5,'Jorge','YamMWFwtkjfma4Y','jorge89@hotmail.com','2023-03-07 16:32:56'),(6,'Salcedo','YamMWFwtkjfma4Y','salcedo1568@yahoo.es','2023-03-07 16:35:21'),(7,'Adonis','YamMWFwtkjfma4Y','adonis485@gmail.com','2023-03-07 16:38:34'),(8,'Jessica','SEeeCX2H9Z2MabN','jj57@gmail.com','2023-03-23 08:46:43'),(9,'Ricardo','123','Richard16@gmail.com','2023-05-09 16:10:30');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citas`
--

DROP TABLE IF EXISTS `citas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citas` (
  `idCita` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) DEFAULT NULL,
  `Ap_Paterno` varchar(50) DEFAULT NULL,
  `Ap_Materno` varchar(50) DEFAULT NULL,
  `Fecha_Cita` date DEFAULT NULL,
  `Hora_Cita` time DEFAULT NULL,
  `Medico` varchar(50) DEFAULT NULL,
  `Asunto` varchar(100) DEFAULT NULL,
  `Correo` varchar(100) DEFAULT NULL,
  `Telefono` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idCita`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citas`
--

LOCK TABLES `citas` WRITE;
/*!40000 ALTER TABLE `citas` DISABLE KEYS */;
INSERT INTO `citas` VALUES (1,'Luis Andres','Hernandez','Martinez','2023-05-23','15:25:00','Dr. Raul Castellanos Perez','Cirugia','fulanito@hotmail.com','9681452371'),(2,'Daniel','Andrade','Castellanos','2024-05-25','06:08:00','Dr. Raul Castellanos Perez','Cirugia Bariatrica','fulanito2@hotmail.com','9681452451'),(3,'Erick Saul','Garcia','Altamirano','2024-06-12','17:46:00','Dra. Jessica Jaqueline ','Circuncision','ericksaul@gmail.com','96458971232'),(4,'Jorge Alberto','De Aquino','Duran','2030-05-30','23:59:00','Dr. Alonso Hernandez Rodriguez','Colonoscopia','jorgedeaquino@gmail.com','9614587956'),(5,'Marco Antonio','Hernandez','Pimentel','2021-06-22','17:45:00','Dr. Benito Juarez Garcia','Oftalmologia','mahp@gmail.com','9615847239'),(6,'Jeancarlo Majerley','Arroyo','Lima','2023-08-23','16:22:00','Dr. Sergio Castañeda','Sesión de terapia de psicologica','jmp@gmail.com','9615894723');
/*!40000 ALTER TABLE `citas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicos`
--

DROP TABLE IF EXISTS `medicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicos` (
  `idMedicos` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `ap_paterno` varchar(50) DEFAULT NULL,
  `ap_materno` varchar(50) DEFAULT NULL,
  `nacionalidad` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `municipio` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `ced_prof` varchar(20) DEFAULT NULL,
  `especialidad` varchar(50) DEFAULT NULL,
  `folio` int NOT NULL,
  PRIMARY KEY (`idMedicos`),
  KEY `FK_medicos_pacientes` (`folio`),
  CONSTRAINT `FK_medicos_pacientes` FOREIGN KEY (`folio`) REFERENCES `pacientes` (`folio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicos`
--

LOCK TABLES `medicos` WRITE;
/*!40000 ALTER TABLE `medicos` DISABLE KEYS */;
/*!40000 ALTER TABLE `medicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pacientes`
--

DROP TABLE IF EXISTS `pacientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pacientes` (
  `folio` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `ap_paterno` varchar(50) DEFAULT NULL,
  `ap_materno` varchar(50) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `edad` int DEFAULT NULL,
  `genero` varchar(10) DEFAULT NULL,
  `estado_civil` varchar(20) DEFAULT NULL,
  `tratamiento` varchar(50) DEFAULT NULL,
  `num_familiares` int DEFAULT NULL,
  `nacionalidad` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `municipio` varchar(50) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `codigo_postal` varchar(10) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`folio`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pacientes`
--

LOCK TABLES `pacientes` WRITE;
/*!40000 ALTER TABLE `pacientes` DISABLE KEYS */;
INSERT INTO `pacientes` VALUES (7,'Jeancarlo','Majerley','M','1995-05-24',32,'Masculino','Casado','Consulta Medica',9,'Mexicana','Chiapas','Tuxtla Gutierrez','Conocida','29150','9611568497'),(8,'Alejandro','Trujillo','Delgado','1996-02-12',27,'Masculino','Soltero','Consulta Medica',8,'Mexicana','Chiapas','Ocozocoautla de Espinosa','Conocida','29140','9681324579');
/*!40000 ALTER TABLE `pacientes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-18 22:47:33
