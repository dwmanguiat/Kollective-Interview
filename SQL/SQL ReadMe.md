SQL Questions: 

1. Create a schema for a transfer table with the appropriate data fields.
    a. Explain any primary keys or indexes you choose to put on the table.
    DM - See schema/transfer.sql and schema/node.sql
        - Primary Key + index on transfer.transfer_id: This field denotes a unique integer identifier for each transfer record. Assuming this is a large dataset, this will facilitate archiving and cleanup operations as the table size grows and performance begins to degrade
        - Foreign Key constraints on transfer.source_id and transfer.dest_id: These fields should be join-able out to our node table for more metadata on the actual user/client. The id missing in the node table would denote an issue, for example an impossible client id.
        - Indexes on transfer.source_id and transfer_dest_id: These indexes faclitate perfomant queries on common joins that multiple users/services are likely using.
        - Index on transfer.timestamp: I am inferring that end users will need this data in a time series format, this index will facilitate queries looking at different date ranges. 

2. How might you get your dataset from python into SQL?
    DM - The exact solution would depend on the size and velocity of the dataset, i.e. if you are recieveing 100k records sporadically throughout the day vs a constant stream of 10 Million records streaming in 24/7. 

    In general, the 5000 record output of the python question would be achievable and reliable generating bull inserts into the database directly via another python script. Another pattern could be dumping the records to a csv and inserting the csv via an SSIS or your favorite non-Microsoft equivalent. This does present the challenge of what to do with your intermediate files though, i.e. can they be deleted after succcess? Do they need to be archived somewhere? etc.

    As the dataset grows you can evaluate other tools that are more oriented toward a larger dataset. For example, instead of dumping the recordsets to a csv, you could write to a parquet and upload to a datalake instead, then read in a SQL context via a Spark or Synapse type solution.

3. Create a schema for a second table called node. This table should have the following fields:
    a. id : string (the UUID of the node, will match either source_id or dest_id inthe transfer table)
    b. name: string (the name of the employee representing that node, e.g. “Joe”, “Carol”, “Bob”, etc.)
    c. office: string (the name of the office where the employee works, e.g. “BostonHQ”, “Chicago Branch”, etc.)
    DM - see schema/node.sql

4. Write a query that shows how many bytes one employee downloaded from another. e.g.:
    a. Bob downloaded 100MB from Carol
    b. Bob downloaded 80MB from Joe
    DM - See queries.sql: "Question 4"

5. Write a query that shows who downloaded bytes from someone in another office, e.g.:
    a. Bob (Boston HQ) downloaded bytes from Carol (Chicago Branch)
    DM - See queries.sql: "Question 5"