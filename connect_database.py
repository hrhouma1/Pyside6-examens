#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import Error

def test_database_connection():
    """Teste la connexion à la base de données MySQL"""
    
    # Configuration de la base de données
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',  # Mot de passe MySQL
        'port': 3306
    }
    
    connection = None
    
    try:
        print("🔄 Tentative de connexion à MySQL...")
        
        # Connexion à MySQL (sans spécifier de base de données)
        connection = mysql.connector.connect(**db_config)
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"✅ Connexion réussie à MySQL Server version {db_info}")
            
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"📊 Base de données actuelle: {record}")
            
            # Créer la base de données si elle n'existe pas
            cursor.execute("CREATE DATABASE IF NOT EXISTS messages_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✅ Base de données 'messages_app' créée ou vérifiée")
            
            # Utiliser la base de données
            cursor.execute("USE messages_app")
            print("✅ Utilisation de la base de données 'messages_app'")
            
            # Créer la table si elle n'existe pas
            create_table_query = """
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                texte VARCHAR(500) NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                INDEX idx_date_creation (date_creation)
            )
            """
            cursor.execute(create_table_query)
            print("✅ Table 'messages' créée ou vérifiée")
            
            # Vérifier la structure de la table
            cursor.execute("DESCRIBE messages")
            columns = cursor.fetchall()
            print("\n📋 Structure de la table 'messages':")
            for column in columns:
                print(f"  - {column[0]}: {column[1]}")
            
            # Compter les messages existants
            cursor.execute("SELECT COUNT(*) FROM messages")
            count = cursor.fetchone()[0]
            print(f"\n📊 Nombre de messages existants: {count}")
            
            cursor.close()
            print("\n🎉 Test de connexion terminé avec succès!")
            
    except Error as e:
        print(f"❌ Erreur lors de la connexion à MySQL: {e}")
        return False
        
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("🔒 Connexion MySQL fermée")
    
    return True

def main():
    """Fonction principale"""
    print("=" * 50)
    print("🔍 TEST DE CONNEXION À LA BASE DE DONNÉES")
    print("=" * 50)
    
    success = test_database_connection()
    
    if success:
        print("\n✅ Configuration de la base de données OK!")
        print("📝 Vous pouvez maintenant exécuter:")
        print("   python add_mysql_test_data.py")
        print("   python main.py")
    else:
        print("\n❌ Problème de configuration détecté")
        print("🔧 Vérifiez:")
        print("   - MySQL Server est démarré")
        print("   - Les paramètres de connexion sont corrects")
        print("   - L'utilisateur a les privilèges nécessaires")

if __name__ == "__main__":
    main() 