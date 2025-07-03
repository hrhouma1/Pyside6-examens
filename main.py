#!/usr/bin/env python3
"""
Examen PyQt6 - Partie 1: Signaux, Slots et affichage de message
Auteur: [Votre nom]
Date: [Date]
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

class MessageApp(QMainWindow):
    """
    Application principale pour l'examen Partie 1
    Gère l'affichage de messages via signaux et slots
    """
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.connect_signals()
    
    def load_ui(self):
        """Charge l'interface utilisateur depuis le fichier .ui"""
        try:
            # Chargement du fichier .ui
            loader = QUiLoader()
            ui_file = QFile("interface.ui")
            
            if not ui_file.open(QIODevice.ReadOnly):
                raise Exception("Impossible d'ouvrir le fichier interface.ui")
            
            self.ui = loader.load(ui_file, self)
            ui_file.close()
            
            # Configuration de la fenêtre
            self.setCentralWidget(self.ui.centralwidget)
            self.setWindowTitle("Examen PyQt6 - Partie 1")
            self.resize(400, 300)
            
        except Exception as e:
            print(f"Erreur lors du chargement de l'interface: {e}")
            sys.exit(1)
    
    def connect_signals(self):
        """
        Connecte les signaux aux slots
        Contrainte de l'examen: utiliser le signal clicked du bouton
        """
        # Connexion du signal clicked du bouton au slot afficher_message
        self.ui.pushButton_afficher.clicked.connect(self.afficher_message)
        
        # Optionnel: permettre l'activation par la touche Entrée
        self.ui.lineEdit_message.returnPressed.connect(self.afficher_message)
    
    @Slot()
    def afficher_message(self):
        """
        Slot pour afficher le message saisi
        Contraintes de l'examen:
        - Traitement exclusivement via cette méthode
        - Aucune action si le champ est vide
        - Afficher avec le préfixe "Message saisi : "
        """
        # Récupération du texte saisi
        message_saisi = self.ui.lineEdit_message.text().strip()
        
        # Vérification: aucune action si le champ est vide
        if not message_saisi:
            # Optionnel: feedback visuel pour champ vide
            self.ui.label_affichage.setText("⚠️ Veuillez saisir un message avant de cliquer sur le bouton.")
            self.ui.label_affichage.setStyleSheet("""
                QLabel {
                    border: 2px solid #ff6b6b;
                    border-radius: 5px;
                    padding: 10px;
                    background-color: #ffe0e0;
                    color: #d63031;
                }
            """)
            return
        
        # Affichage du message avec le préfixe requis
        message_affiche = f"Message saisi : {message_saisi}"
        self.ui.label_affichage.setText(message_affiche)
        
        # Style pour message valide
        self.ui.label_affichage.setStyleSheet("""
            QLabel {
                border: 2px solid #00b894;
                border-radius: 5px;
                padding: 10px;
                background-color: #e0f8f4;
                color: #00695c;
            }
        """)
        
        # Alternative: affichage dans une autre fenêtre (comme mentionné dans l'énoncé)
        self.afficher_dans_autre_fenetre(message_saisi)
        
        # Optionnel: vider le champ après affichage
        self.ui.lineEdit_message.clear()
        self.ui.lineEdit_message.setFocus()
    
    def afficher_dans_autre_fenetre(self, message):
        """
        Alternative: affichage dans une autre fenêtre
        Comme mentionné dans l'énoncé de l'examen
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Message affiché")
        msg_box.setText(f"Message saisi : {message}")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()

def main():
    """Fonction principale de l'application"""
    # Création de l'application Qt
    app = QApplication(sys.argv)
    
    # Création et affichage de la fenêtre principale
    window = MessageApp()
    window.show()
    
    # Lancement de la boucle d'événements
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 