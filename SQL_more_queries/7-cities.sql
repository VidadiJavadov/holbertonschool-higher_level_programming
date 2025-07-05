-- This script creates the database hbtn_0d_usa and the table cities on your MySQL server.

-- Create the database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database.
USE hbtn_0d_usa;

-- Create the table 'cities' if it does not already exist.
-- Description:
-- id: INT, unique, auto-generated, cannot be null, and is a primary key.
-- state_id: INT, cannot be null, and must be a FOREIGN KEY that references the id of the states table.
-- name: VARCHAR(256), cannot be null.
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);
