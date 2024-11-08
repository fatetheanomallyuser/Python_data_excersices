SHOW VARIABLES LIKE 'default_authetication_plugin';
SELECT user, plugin
FROM mysql.user
WHERE user='root';

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '#enter password here';
#OR
CREATE USER 'web_app_usr'@'localhost' IDENTIFIED WITH mysql_native_password BY '#enter password here!';

FLUSH privileges;
