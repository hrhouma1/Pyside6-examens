-- Script SQL pour créer la base de données et la table messages
-- Exécutez ce script dans votre console MySQL si nécessaire

-- Création de la base de données
CREATE DATABASE IF NOT EXISTS messages_app 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Utilisation de la base de données
USE messages_app;

-- Création de la table messages
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texte VARCHAR(500) NOT NULL,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_date_creation (date_creation)
);

-- Insertion de quelques exemples de données (optionnel)
INSERT INTO messages (texte) VALUES 
('Premier message de test'),
('Deuxième message de test'),
('Troisième message de test');

-- Affichage des messages pour vérification
SELECT * FROM messages ORDER BY date_creation DESC; 