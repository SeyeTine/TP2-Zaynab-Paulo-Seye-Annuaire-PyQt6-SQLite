from database import ModifierContact
def modifier_contact(self):
    """Modifier le contact sélectionné"""
    if not self.selected_id:
        QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un contact à modifier!")
        return

    valeurs = [le.text() for le in self.line_edits]

    if not all(valeurs):
        QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs!")
        return

    # Validation de l'email
    email = valeurs[3]  # L'email est le 4ème champ
    if '@' not in email or '.' not in email:
        QMessageBox.warning(self, "Erreur", "L'email doit contenir @ et un point (.)")
        return

    ModifierContact(self.selected_id, *valeurs)
    self.vider_champs()
    self.selected_id = None
    self.afficher_tout()
