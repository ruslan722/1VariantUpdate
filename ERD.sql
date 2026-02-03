-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema var
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema var
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `var` DEFAULT CHARACTER SET utf8mb3 ;
USE `var` ;

-- -----------------------------------------------------
-- Table `var`.`punkt`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `var`.`punkt` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `adress` VARCHAR(255) NOT NULL,
  `number` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 36
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `var`.`tovar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `var`.`tovar` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `article` VARCHAR(255) NOT NULL,
  `edinisa` VARCHAR(255) NOT NULL,
  `price` INT NOT NULL,
  `postavsik` VARCHAR(255) NOT NULL,
  `proizvod` VARCHAR(255) NOT NULL,
  `category` VARCHAR(255) NOT NULL,
  `sale` INT NOT NULL,
  `kolvo` INT NOT NULL,
  `opis` VARCHAR(255) NOT NULL,
  `photo` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 31
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `var`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `var`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fio` VARCHAR(255) NOT NULL,
  `login` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `var`.`zakaz`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `var`.`zakaz` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `article` VARCHAR(255) NOT NULL,
  `data` VARCHAR(255) NOT NULL,
  `data_dostavki` VARCHAR(255) NOT NULL,
  `adress` VARCHAR(255) NOT NULL,
  `fio` VARCHAR(255) NOT NULL,
  `status` VARCHAR(255) NOT NULL,
  `code` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
