-- creates the mysql server user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
ON MySQL.*
TO 'user_0d_1'@'localhost';
