
CREATE DATABASE IF NOT EXISTS ADDATABASE;

USE ADDATABASE;
--drop table

DROP TABLE IF EXISTS Ad;
DROP TABLE IF EXISTS AdvertiserTable;
-- adver.. table
CREATE TABLE IF NOT EXISTS AdvertiserTable (
    id INT PRIMARY KEY AUTO_INCREMENT,
    views INT,
    clicks INT,
    name VARCHAR(512)
);

-- Ad table
CREATE TABLE IF NOT EXISTS Ad (
    id INT PRIMARY KEY AUTO_INCREMENT,
    clicks INT,
    views INT,
    title VARCHAR(512),
    imgUrl VARCHAR(512),
    link VARCHAR(512),
    advertiser_id INT,
    FOREIGN KEY (advertiser_id) REFERENCES AdvertiserTable(id)
);
