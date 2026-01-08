def AjouterContact(nom, prenom, telephone, email):
    """Ajouter un nouveau contact"""
    conn = sqlite3.connect("carnet_adresses.db")
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO Contacts (Nom, Prenom, Telephone, Email)
                   VALUES (?, ?, ?, ?)
                   """, (nom, prenom, telephone, email))

    conn.commit()
    conn.close()