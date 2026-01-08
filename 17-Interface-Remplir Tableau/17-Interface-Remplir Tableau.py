from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt
from database import RecupererTousLesContacts

def remplir_tableau(self, resultats):
    """Remplir le tableau avec des données"""
    self.tableau.setRowCount(len(resultats))

    for i in range(len(resultats)):
        for j in range(5):
            item = QTableWidgetItem(str(resultats[i][j]))
            if j == 0:  # ID en lecture seule
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.tableau.setItem(i, j, item)

def cellule_cliquee(self, row, column):
    """Remplir les champs quand on clique sur une ligne"""
    id_item = self.tableau.item(row, 0)
    if id_item:
        self.selected_id = id_item.text()

    # Remplir les champs avec les données de la ligne
    for j in range(4):
        item = self.tableau.item(row, j + 1)
        if item:
            self.line_edits[j].setText(item.text())

def vider_champs(self):
    """Vider tous les champs de saisie"""
    for le in self.line_edits:
        le.clear()
