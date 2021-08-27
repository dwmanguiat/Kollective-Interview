CREATE TABLE 'transfer' (
	'transfer_id' INT NOT NULL AUTO_INCREMENT,
	'timestamp' TIMESTAMP NOT NULL,
	'type' VARCHAR(6) NOT NULL,
	'duration' INT NOT NULL,
	'source_id' VARCHAR(36),
	'destination_id' VARCHAR(36),
	PRIMARY KEY ('transfer_id'),
	FOREIGN KEY ('source_id') REFERENCES node(id),
	FOREIGN KEY ('destination_id') REFERENCES node(id)

);

CREATE idx_transfer_transfer_id on transfer (transfer_id); --MySQL does not have this option, but in SQL server for examle this would be a clustered index
CREATE idx_transfer_source_id on transfer (source_id);
CREATE idx_transfer_destination_id on transfer (destination_id);
CREATE idx_transfer_timestamp on transfer (timestamp)