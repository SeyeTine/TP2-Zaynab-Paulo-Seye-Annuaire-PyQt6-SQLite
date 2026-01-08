def SupprimerContact(id_contact):
    """Supprimer un contact"""
    conn = sqlite3.connect("carnet_adresses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Contacts WHERE ID = ?", (id_contact,))
    conn.commit()
    conn.close()