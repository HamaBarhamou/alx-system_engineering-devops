-- user_0d_1 should have all privileges
-- cat 1-create_user.sql | mysql -hlocalhost -uroot -p

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'Jaimelep0ulet';
-- GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%'
GRANT SELECT ON `mysql`.`user` TO 'holberton_user'@'localhost';