from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt
from database import RecupererTousLesContacts
def afficher_tout(self):
    """Afficher tous les contacts"""
    resultats = RecupererTousLesContacts()
    self.remplir_tableau(resultats)
