-- Creating the database
CREATE DATABASE  hbtn_0d_usa;

-- cd/use the database created
USE hbtn_0d_usa;

-- creating table 'cities'
CREATE TABLE cities (
    id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);