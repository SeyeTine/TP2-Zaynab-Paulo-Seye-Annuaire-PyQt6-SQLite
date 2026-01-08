def RechercherContacts(terme):
    """Rechercher des contacts"""
    conn = sqlite3.connect("carnet_adresses.db")
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT *
                   FROM Contacts
                   WHERE Nom LIKE ?
                      OR Prenom LIKE ?
                      OR Telephone LIKE ?
                      OR Email LIKE ?
                   ORDER BY Nom, Prenom
                   """, (f'%{terme}%', f'%{terme}%', f'%{terme}%', f'%{terme}%'))

    resultat = cursor.fetchall()
    conn.close()
    return resultat