def ModifierContact(id_contact, nom, prenom, telephone, email):
    """Modifier un contact existant"""
    conn = sqlite3.connect("carnet_adresses.db")
    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE Contacts
                   SET Nom       = ?,
                       Prenom    = ?,
                       Telephone = ?,
                       Email     = ?
                   WHERE ID = ?
                   """, (nom, prenom, telephone, email, id_contact))

    conn.commit()
    conn.close()