--setup the db test environment

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED  BY 'hbnb_test_pwd';
GRANT ALL PRIVILEDGES
    ON `hbnb_test_db`.*
    TO 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT
    ON `perfomance_schema`.*
    TO 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEDGES;
