CREATE TABLE `transfer` (
	`transfer_id` INT NOT NULL AUTO_INCREMENT,
	`timestamp` TIMESTAMP NOT NULL,
	`type` VARCHAR(6) NOT NULL,
	`duration` INT NOT NULL,
	`source_id` VARCHAR(36),
	`destination_id` VARCHAR(36),
	PRIMARY KEY (`transfer_id`)
);