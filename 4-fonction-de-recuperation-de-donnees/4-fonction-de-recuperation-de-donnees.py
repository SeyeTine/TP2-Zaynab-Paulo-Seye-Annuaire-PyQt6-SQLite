def RecupererTousLesContacts():
    """Récupérer tous les contacts"""
    conn = sqlite3.connect("carnet_adresses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contacts ORDER BY Nom, Prenom")
    resultat = cursor.fetchall()
    conn.close()
    return resultat