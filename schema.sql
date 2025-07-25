CREATE DATABASE IF NOT EXISTS chicken_database;
USE chicken_database

CRETAE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chicken_name VARCHAR(100),
    breed VARCHAR(100),
    age INT,
    birthday DATETIME
);