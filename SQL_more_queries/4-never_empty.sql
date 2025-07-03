-- ID cant be null
CREATE TABLE IF NOT EXISTS id_not_null (id DEFAULT 1, name VARCHAR(256));
GRANT ALL PRIVILEGES ON force_name TO 'user'@'localhost';
