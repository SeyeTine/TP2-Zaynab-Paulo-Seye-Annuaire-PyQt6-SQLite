from database import RechercherContacts
def rechercher_contact(self):
    """Rechercher des contacts en temps réel"""
    terme = self.line_edit_recherche.text()

    if not terme:
        self.afficher_tout()
        return

    resultats = RechercherContacts(terme)
    self.remplir_tableau(resultats)
