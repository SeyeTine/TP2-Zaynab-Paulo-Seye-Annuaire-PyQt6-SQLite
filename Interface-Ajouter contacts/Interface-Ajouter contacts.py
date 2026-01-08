from PyQt6.QtWidgets import QMessageBox
from database import AjouterContact
def ajouter_contact(self):
    """Ajouter un nouveau contact"""
    valeurs = [le.text() for le in self.line_edits]

    if not all(valeurs):
        QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs!")
        return

    # Validation de l'email
    email = valeurs[3]  # L'email est le 4ème champ
    if '@' not in email or '.' not in email:
        QMessageBox.warning(self, "Erreur", "L'email doit contenir @ et un point (.)")
        return

    AjouterContact(*valeurs)
    self.vider_champs()
    self.afficher_tout()

