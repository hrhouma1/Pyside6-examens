#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Configuration de la base de données
Modifiez ces paramètres selon votre configuration MySQL
"""

# Configuration de la base de données MySQL
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Modifiez selon votre mot de passe MySQL
    'database': 'messages_app',
    'port': 3306,
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

# Paramètres de l'application
APP_CONFIG = {
    'window_title': 'Application Messages - Signaux et Slots',
    'window_width': 600,
    'window_height': 400,
    'max_message_length': 500
} 