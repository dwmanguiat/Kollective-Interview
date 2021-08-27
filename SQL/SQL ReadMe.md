SQL Questions: 

1. Create a schema for a transfer table with the appropriate data fields.
    a. Explain any primary keys or indexes you choose to put on the table.
    DM - See schema/transfer.sql and schema/node.sql

2. How might you get your dataset from python into SQL?

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