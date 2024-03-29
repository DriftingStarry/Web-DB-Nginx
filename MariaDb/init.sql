GRANT INSERT, UPDATE, CREATE
ON *.*
TO 'PyReptile'@'%'
IDENTIFIED BY 'Py_114514';

GRANT SELECT
ON *.*
TO 'Flask'@'%'
IDENTIFIED BY 'Flask_1919810';

GRANT ALL
ON *.*
TO 'ops'@'%'
IDENTIFIED BY 'ops';

flush privileges;

CREATE DATABASE hddata;
USE hddata;
CREATE TABLE news(
title TEXT,
turl TEXT,
id INT PRIMARY KEY
);