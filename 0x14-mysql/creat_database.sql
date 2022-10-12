-- creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges
-- cat 1-create_user.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 ( id smallint unsigned not null auto_increment, name
varchar(30) not null, constraint pk primary key (id) );
INSERT INTO nexus6 ( id, name ) VALUES ( null, 'Leon' );
GRANT SELECT ON `tyrell_corp`.`nexus6` TO 'holberton_user'@'localhost';