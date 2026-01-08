"""
===========================================
FICHIER: ui/fenetre_principale.py
Fenêtre principale de l'application
===========================================
"""

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QMessageBox
)
from PyQt6.QtCore import Qt
from database import (
    AjouterContact,
    ModifierContact,
    SupprimerContact,
    RecupererTousLesContacts,
    RechercherContacts
)


class FenetrePrincipale(QWidget):
    """Fenêtre principale de l'application"""

    def __init__(self):
        super().__init__()
        self.selected_id = None
        self.initUI()
        self.afficher_tout()

    def initUI(self):
        """Initialiser l'interface utilisateur"""

        self.setWindowTitle("Mon Carnet d'Adresses")
        self.setGeometry(100, 100, 1000, 650)

        # Titre
        self.titre = QLabel(self)
        self.titre.setText("📇 MON CARNET D'ADRESSES")
        self.titre.setGeometry(35, 20, 930, 50)
        self.titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Section Recherche
        self.label_recherche = QLabel(self)
        self.label_recherche.setText("🔍 Recherche:")
        self.label_recherche.setGeometry(35, 90, 120, 30)

        self.line_edit_recherche = QLineEdit(self)
        self.line_edit_recherche.setGeometry(165, 90, 365, 35)
        self.line_edit_recherche.setPlaceholderText("Rechercher un contact...")

        self.line_edit_recherche.textChanged.connect(self.rechercher_contact)
