"""
===========================================
FICHIER: database/db_manager.py
Gestionnaire de base de données
===========================================
"""

import sqlite3


def CreerTable():
    """Créer la table Contacts si elle n'existe pas"""
    conn = sqlite3.connect("carnet_adresses.db")
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Contacts
                   (
                       ID
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       Nom
                       TEXT
                       NOT
                       NULL,
                       Prenom
                       TEXT
                       NOT
                       NULL,
                       Telephone
                       TEXT
                       NOT
                       NULL,
                       Email
                       TEXT
                       NOT
                       NULL
                   );
                   """)

    conn.commit()
    conn.close()