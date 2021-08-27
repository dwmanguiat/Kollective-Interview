CREATE TABLE `node` (
	`id` VARCHAR(36) NOT NULL,
	`name` VARCHAR(100),
	`office` VARCHAR(100),
	PRIMARY KEY (`id`)

);

CREATE INDEX idx_node_id on 'node' (id);
