-- creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges
-- cat 1-create_user.sql | mysql -hlocalhost -uroot -p

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
-- GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';