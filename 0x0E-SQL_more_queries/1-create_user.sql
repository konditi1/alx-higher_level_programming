--  script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
-- grants all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
-- flush privileges to apply
FLUSH PRIVILEGES;
