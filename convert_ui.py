#!/usr/bin/env python3
"""
Script pour convertir le fichier .ui en Python
Utilisation: python convert_ui.py
"""

import subprocess
import sys
import os

def convert_ui_to_py():
    """Convertit interface.ui en interface_ui.py"""
    ui_file = "interface.ui"
    py_file = "interface_ui.py"
    
    if not os.path.exists(ui_file):
        print(f"Erreur: Le fichier {ui_file} n'existe pas.")
        return False
    
    try:
        # Commande pour convertir .ui en .py
        result = subprocess.run([
            "pyside6-uic", ui_file, "-o", py_file
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Conversion réussie: {ui_file} → {py_file}")
            return True
        else:
            print(f"❌ Erreur lors de la conversion:")
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ Erreur: pyside6-uic n'est pas trouvé.")
        print("Assurez-vous que PySide6 est installé avec:")
        print("pip install pyside6")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return False

if __name__ == "__main__":
    convert_ui_to_py() 