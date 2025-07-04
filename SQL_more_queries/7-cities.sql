--cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(256) NOT NULL,PRIMARY KEY(id));
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT,state_id INT NOT NULL,name VARCHAR(256) NOT NULL,PRIMARY KEY(id),FOREIGN KEY(state_id) REFERENCES states(id));
INSERT INTO states(name) VALUES('California'),('Arizona');
INSERT INTO cities(state_id,name) VALUES(1,'San Francisco'),(1,'San Diego'),(2,'Page'),(2,'Phoenix');
