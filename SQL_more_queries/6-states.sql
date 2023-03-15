-- Creates the database and the table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY (id), UNIQUE (id));
