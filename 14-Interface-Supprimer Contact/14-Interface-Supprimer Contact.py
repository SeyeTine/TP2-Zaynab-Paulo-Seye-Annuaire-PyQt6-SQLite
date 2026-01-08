from database import SupprimerContact
def supprimer_contact(self):
    """Supprimer le contact sélectionné"""
    if not self.selected_id:
        QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un contact à supprimer!")
        return

    reponse = QMessageBox.question(
        self,
        "Confirmation",
        "Êtes-vous sûr de vouloir supprimer ce contact?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )

    if reponse == QMessageBox.StandardButton.Yes:
        SupprimerContact(self.selected_id)
        self.selected_id = None
        self.afficher_tout()
