#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic


class MessageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_connection = None
        self.init_ui()
        self.init_database()
        self.connect_signals()
        
    def init_ui(self):
        """Charge l'interface depuis le fichier .ui"""
        uic.loadUi('interface.ui', self)
        
    def connect_signals(self):
        """Connecte les signaux aux slots"""
        self.sendButton.clicked.connect(self.on_send_button_clicked)
        self.refreshButton.clicked.connect(self.load_messages_from_db)
        self.messageInput.returnPressed.connect(self.on_send_button_clicked)
        
    def init_database(self):
        """Initialise la connexion à la base de données"""
        try:
            self.db_config = {
                'host': 'localhost',
                'user': 'root',
                'password': '',  # Modifiez selon votre configuration
                'database': 'messages_app'
            }
            
            self.connect_to_database()
            self.create_table_if_not_exists()
            self.load_messages_from_db()
            
        except mysql.connector.Error as err:
            self.show_error_message(f"Erreur de base de données : {err}")
            
    def connect_to_database(self):
        """Établit la connexion à la base de données"""
        try:
            self.db_connection = mysql.connector.connect(**self.db_config)
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.create_database()
                self.db_connection = mysql.connector.connect(**self.db_config)
            else:
                raise err
                
    def create_database(self):
        """Crée la base de données si elle n'existe pas"""
        try:
            temp_config = self.db_config.copy()
            del temp_config['database']
            temp_connection = mysql.connector.connect(**temp_config)
            
            cursor = temp_connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_config['database']}")
            cursor.close()
            temp_connection.close()
            
        except mysql.connector.Error as err:
            self.show_error_message(f"Erreur lors de la création de la base de données : {err}")
            
    def create_table_if_not_exists(self):
        """Crée la table messages si elle n'existe pas"""
        try:
            cursor = self.db_connection.cursor()
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                texte VARCHAR(500) NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            
            cursor.execute(create_table_query)
            self.db_connection.commit()
            cursor.close()
            
        except mysql.connector.Error as err:
            self.show_error_message(f"Erreur lors de la création de la table : {err}")
            
    def on_send_button_clicked(self):
        """Slot appelé lorsque le bouton d'envoi est cliqué"""
        message_text = self.messageInput.text().strip()
        
        if not message_text:
            self.show_warning_message("Veuillez saisir un message avant d'envoyer.")
            return
            
        # Afficher le message dans le QLabel
        self.messageDisplay.setText(f"Message saisi : {message_text}")
        
        # Insérer le message dans la base de données
        self.insert_message_to_db(message_text)
        
        # Vider le champ de saisie
        self.messageInput.clear()
        
        # Rafraîchir l'affichage des messages
        self.load_messages_from_db()
        
    def insert_message_to_db(self, message_text):
        """Insère le message dans la base de données"""
        try:
            if self.db_connection and self.db_connection.is_connected():
                cursor = self.db_connection.cursor()
                
                insert_query = "INSERT INTO messages (texte) VALUES (%s)"
                cursor.execute(insert_query, (message_text,))
                
                self.db_connection.commit()
                cursor.close()
                
                self.show_info_message("Message enregistré avec succès !")
                
        except mysql.connector.Error as err:
            self.show_error_message(f"Erreur lors de l'insertion : {err}")
            
    def load_messages_from_db(self):
        """Charge et affiche tous les messages de la base de données"""
        try:
            if self.db_connection and self.db_connection.is_connected():
                cursor = self.db_connection.cursor()
                
                select_query = "SELECT id, texte, date_creation FROM messages ORDER BY date_creation DESC"
                cursor.execute(select_query)
                
                messages = cursor.fetchall()
                cursor.close()
                
                messages_text = ""
                if messages:
                    for message in messages:
                        messages_text += f"ID: {message[0]} | {message[2]} | {message[1]}\n"
                else:
                    messages_text = "Aucun message dans la base de données."
                    
                self.dbMessagesDisplay.setPlainText(messages_text)
                
        except mysql.connector.Error as err:
            self.show_error_message(f"Erreur lors du chargement des messages : {err}")
            
    def show_error_message(self, message):
        """Affiche une boîte de dialogue d'erreur"""
        QMessageBox.critical(self, "Erreur", message)
        
    def show_warning_message(self, message):
        """Affiche une boîte de dialogue d'avertissement"""
        QMessageBox.warning(self, "Avertissement", message)
        
    def show_info_message(self, message):
        """Affiche une boîte de dialogue d'information"""
        QMessageBox.information(self, "Information", message)
        
    def closeEvent(self, event):
        """Ferme proprement la connexion à la base de données"""
        if self.db_connection and self.db_connection.is_connected():
            self.db_connection.close()
        event.accept()


def main():
    """Fonction principale"""
    app = QApplication(sys.argv)
    window = MessageApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main() 