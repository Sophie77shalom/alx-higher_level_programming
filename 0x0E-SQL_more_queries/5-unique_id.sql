-- This script creates the table unique_id on your MySQL server.

-- creating table unique id
CREATE TABLE unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);