# Ajouter dans la méthode initUI (après les boutons)
from PyQt6.QtWidgets import QTableWidget

# Tableau
self.tableau = QTableWidget(self)
self.tableau.setRowCount(0)
self.tableau.setColumnCount(5)
self.tableau.setGeometry(35, 360, 930, 260)
self.tableau.setHorizontalHeaderLabels(
    ['ID', 'Nom', 'Prénom', 'Téléphone', 'Email']
)
self.tableau.cellClicked.connect(self.cellule_cliquee)

# Ajuster largeur des colonnes
self.tableau.setColumnWidth(0, 60)
self.tableau.setColumnWidth(1, 200)
self.tableau.setColumnWidth(2, 200)
self.tableau.setColumnWidth(3, 200)
self.tableau.setColumnWidth(4, 240)
