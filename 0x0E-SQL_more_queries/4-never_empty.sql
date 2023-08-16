-- script that creates the table id_not_null
CREATE TABLE id_not_null
-- id in definition
    id INT DEFAULT 1, name VARCHAR(256)
-- if the table already exists the script should not fail
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));