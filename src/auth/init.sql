CREATE USER IF NOT EXISTS 'auth_server'@'localhost' IDENTIFIED BY 'Piamonte1212!';

CREATE DATABASE IF NOT EXISTS auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_server'@'localhost';

USE auth;

CREATE TABLE IF NOT EXISTS user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    admin BOOLEAN DEFAULT FALSE
);
-- Quitar esto
INSERT IGNORE INTO user (email, password, admin) VALUES 
('jaimecrispi@email.com', 'PruebaDeConexion', TRUE);


DELIMITER //

CREATE PROCEDURE CheckLoginCredentials(
    IN user_email VARCHAR(255), 
    IN user_password VARCHAR(255)
)
BEGIN
    SELECT id, email, admin
    FROM user 
    WHERE email = user_email AND password = user_password LIMIT 1;
END//

DELIMITER ;