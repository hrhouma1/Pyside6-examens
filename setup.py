#!/usr/bin/env python3
"""
Script d'installation et de lancement pour l'examen PyQt6
Automatise la configuration de l'environnement et le lancement de l'application
"""

import subprocess
import sys
import os
import platform

def run_command(command, description=""):
    """Exécute une commande et affiche le résultat"""
    print(f"🔄 {description}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Succès")
            if result.stdout.strip():
                print(f"   {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {description} - Échec")
            print(f"   Erreur: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description} - Exception: {e}")
        return False

def check_python_version():
    """Vérifie la version de Python"""
    version = sys.version_info
    print(f"🐍 Version Python détectée: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Version Python compatible")
        return True
    else:
        print("❌ Version Python trop ancienne (minimum 3.8 requis)")
        return False

def setup_environment():
    """Configure l'environnement virtuel"""
    print("\n" + "="*50)
    print("🔧 CONFIGURATION DE L'ENVIRONNEMENT")
    print("="*50)
    
    # Détecter l'OS
    system = platform.system()
    
    # Créer l'environnement virtuel
    if not os.path.exists("env"):
        if not run_command(f"{sys.executable} -m venv env", "Création de l'environnement virtuel"):
            return False
    else:
        print("✅ Environnement virtuel déjà existant")
    
    # Commandes d'activation selon l'OS
    if system == "Windows":
        pip_cmd = ".\\env\\Scripts\\pip"
        python_cmd = ".\\env\\Scripts\\python"
    else:
        pip_cmd = "./env/bin/pip"
        python_cmd = "./env/bin/python"
    
    # Installer les dépendances
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installation des dépendances"):
        return False
    
    return True, python_cmd

def launch_application(python_cmd):
    """Lance l'application"""
    print("\n" + "="*50)
    print("🚀 LANCEMENT DE L'APPLICATION")
    print("="*50)
    
    # Convertir le fichier .ui si nécessaire
    if not os.path.exists("interface_ui.py"):
        run_command(f"{python_cmd} convert_ui.py", "Conversion du fichier .ui")
    
    # Lancer l'application
    print("📱 Démarrage de l'application Examen PyQt6...")
    print("   (Fermez la fenêtre de l'application pour revenir au terminal)")
    
    try:
        subprocess.run(f"{python_cmd} main.py", shell=True)
        print("✅ Application fermée normalement")
    except KeyboardInterrupt:
        print("\n⚠️ Application interrompue par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")

def main():
    """Fonction principale"""
    print("🎓 EXAMEN PYQT6 - CONFIGURATION ET LANCEMENT")
    print("="*60)
    
    # Vérifier Python
    if not check_python_version():
        sys.exit(1)
    
    # Configurer l'environnement
    result = setup_environment()
    if isinstance(result, tuple):
        success, python_cmd = result
        if not success:
            sys.exit(1)
    else:
        sys.exit(1)
    
    # Lancer l'application
    launch_application(python_cmd)
    
    print("\n🎉 Session terminée. Merci d'avoir utilisé l'application d'examen!")

if __name__ == "__main__":
    main() 