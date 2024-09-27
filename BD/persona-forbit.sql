-- MySQL Script generated by MySQL Workbench
-- Thu Sep 26 23:48:07 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema persona-forbit
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema persona-forbit
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `persona-forbit` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs ;
USE `persona-forbit` ;

-- -----------------------------------------------------
-- Table `persona-forbit`.`estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `persona-forbit`.`estado` (
  `id` INT NOT NULL DEFAULT '1',
  `descrip` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `persona-forbit`.`persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `persona-forbit`.`persona` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `apellido` VARCHAR(100) NULL DEFAULT NULL,
  `nombres` VARCHAR(100) NULL DEFAULT NULL,
  `dni` VARCHAR(8) NULL DEFAULT NULL,
  `domicilio` VARCHAR(100) NULL DEFAULT NULL,
  `telefono` VARCHAR(15) NULL DEFAULT NULL,
  `id_estado` INT NULL DEFAULT NULL,
  `fecHora_registro` DATE NULL DEFAULT NULL,
  `fecHora_modificacion` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_estado` (`id_estado` ASC) VISIBLE,
  CONSTRAINT `persona_ibfk_1`
    FOREIGN KEY (`id_estado`)
    REFERENCES `persona-forbit`.`estado` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `persona-forbit` ;

-- -----------------------------------------------------
-- procedure SP_ConsultarPersona
-- -----------------------------------------------------

DELIMITER $$
USE `persona-forbit`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `SP_ConsultarPersona`()
begin
select apellido,nombres,dni,domicilio,telefono,fechora_registro
from persona
where id_estado = 1;
end$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure SP_REGISTROPERSONA
-- -----------------------------------------------------

DELIMITER $$
USE `persona-forbit`$$
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
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure SP_UpdatePersona
-- -----------------------------------------------------

DELIMITER $$
USE `persona-forbit`$$
CREATE PROCEDURE SP_UpdatePersona(
    IN p_Id INT,
    IN p_Apellido VARCHAR(255),
    IN p_Nombres VARCHAR(255),
    IN p_DNI VARCHAR(20),
    IN p_Domicilio VARCHAR(255),
    IN p_Telefono VARCHAR(20)
)
BEGIN
    UPDATE Personas
    SET 
        Apellido = p_Apellido,
        Nombres = p_Nombres,
        DNI = p_DNI,
        Domicilio = p_Domicilio,
        Telefono = p_Telefono,
        FecHora_Modificacion = NOW()
    WHERE Id = p_Id;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure SP_DeletePersona
-- -----------------------------------------------------

DELIMITER $$
USE `persona-forbit`$$
CREATE PROCEDURE SP_DeletePersona(
    IN p_Id INT
)
BEGIN
    UPDATE Personas
    SET 
        Id_Estado = 2,  -- Cambia el estado a "Inactivo"
        FecHora_Modificacion = NOW()
    WHERE Id = p_Id;
END$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
