-- Create user
-- Create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all classic privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;
