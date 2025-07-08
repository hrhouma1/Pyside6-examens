#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import Error
from datetime import datetime

def add_test_data():
    """Ajoute des données de test dans la table messages"""
    
    # Configuration de la base de données
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',  # Mot de passe MySQL
        'database': 'messages_app',
        'port': 3306
    }
    
    connection = None
    
    # Données de test à insérer
    test_messages = [
        "Bonjour, ceci est un message de test!",
        "Test de l'application PyQt6/PySide6",
        "Insertion automatique de données de test",
        "Fonctionnalité de base de données opérationnelle",
        "Message avec accents: éàèùç",
        "Test avec des caractères spéciaux: @#$%^&*()",
        "Message plus long pour tester la capacité de stockage et la gestion des textes de différentes longueurs",
        "🎉 Test avec émojis et caractères Unicode 🚀",
        "Test final - Données insérées avec succès!"
    ]
    
    try:
        print("🔄 Connexion à la base de données...")
        connection = mysql.connector.connect(**db_config)
        
        if connection.is_connected():
            print("✅ Connexion réussie")
            
            cursor = connection.cursor()
            
            # Vérifier si des données existent déjà
            cursor.execute("SELECT COUNT(*) FROM messages")
            existing_count = cursor.fetchone()[0]
            print(f"📊 Messages existants: {existing_count}")
            
            # Insérer les données de test
            insert_query = "INSERT INTO messages (texte) VALUES (%s)"
            
            print("🔄 Insertion des données de test...")
            for i, message in enumerate(test_messages, 1):
                cursor.execute(insert_query, (message,))
                print(f"  [{i}/{len(test_messages)}] ✅ {message[:50]}...")
            
            # Confirmer les modifications
            connection.commit()
            print(f"✅ {len(test_messages)} messages de test insérés avec succès!")
            
            # Vérifier l'insertion
            cursor.execute("SELECT COUNT(*) FROM messages")
            new_count = cursor.fetchone()[0]
            print(f"📊 Total de messages après insertion: {new_count}")
            
            # Afficher les derniers messages
            cursor.execute("SELECT id, texte, date_creation FROM messages ORDER BY date_creation DESC LIMIT 5")
            latest_messages = cursor.fetchall()
            
            print("\n📋 Les 5 derniers messages:")
            for msg in latest_messages:
                print(f"  ID: {msg[0]} | {msg[2]} | {msg[1][:50]}...")
            
            cursor.close()
            
    except Error as e:
        print(f"❌ Erreur lors de l'ajout des données: {e}")
        return False
        
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("🔒 Connexion fermée")
    
    return True

def clear_test_data():
    """Supprime toutes les données de test (optionnel)"""
    
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',  # Mot de passe MySQL
        'database': 'messages_app',
        'port': 3306
    }
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Compter les messages avant suppression
        cursor.execute("SELECT COUNT(*) FROM messages")
        count_before = cursor.fetchone()[0]
        
        # Supprimer tous les messages
        cursor.execute("DELETE FROM messages")
        
        # Réinitialiser l'auto-increment
        cursor.execute("ALTER TABLE messages AUTO_INCREMENT = 1")
        
        connection.commit()
        
        print(f"🗑️ {count_before} messages supprimés")
        print("✅ Table vidée et auto-increment réinitialisé")
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print(f"❌ Erreur lors de la suppression: {e}")

def main():
    """Fonction principale"""
    print("=" * 60)
    print("📝 AJOUT DE DONNÉES DE TEST - APPLICATION MESSAGES")
    print("=" * 60)
    
    print("Que souhaitez-vous faire?")
    print("1. Ajouter des données de test")
    print("2. Supprimer toutes les données")
    print("3. Ajouter des données de test (sans demander)")
    
    try:
        choice = input("\nVotre choix (1-3, ou Entrée pour option 3): ").strip()
        
        if choice == "2":
            confirm = input("⚠️ Êtes-vous sûr de vouloir supprimer toutes les données? (oui/non): ")
            if confirm.lower() in ['oui', 'o', 'yes', 'y']:
                clear_test_data()
            else:
                print("❌ Suppression annulée")
                
        else:  # choice == "1" or choice == "3" or default
            success = add_test_data()
            
            if success:
                print("\n🎉 Données de test ajoutées avec succès!")
                print("📱 Vous pouvez maintenant lancer l'application:")
                print("   python main.py")
            else:
                print("\n❌ Échec de l'ajout des données")
                print("🔧 Vérifiez la connexion à la base de données")
                
    except KeyboardInterrupt:
        print("\n❌ Opération annulée par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")

if __name__ == "__main__":
    main() 