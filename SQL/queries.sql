-- Question 4
SELECT
    n_source.name as SourceName
    ,n_dest.name as DestName
    ,SUM(size) as bytesTransferred
FROM transfer tr
JOIN node n_source
    on tr.source_id = node.id
JOIN node n_dest
    on tr.destination_id = node.id
GROUP BY
    n_source.name
    ,n_dest.name

-- Question 5
SELECT
    n_source.name as SourceName
    n_source.offie as SourceOffice
    ,n_dest.name as DestName
    ,n_dest.office as DestOffice
    ,SUM(size) as bytesTransferred
FROM transfer tr
JOIN node n_source
    on tr.source_id = node.id
JOIN node n_dest
    on tr.destination_id = node.id
WHERE
    n_source.office != n_dest.office
GROUP BY
    n_source.name
    ,n_source.office
    ,n_dest.name
    ,n_dest.office