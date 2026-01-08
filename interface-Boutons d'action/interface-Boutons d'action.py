from PyQt6.QtWidgets import QPushButton

# Boutons d'action
btn_config = [
    ("➕ Ajouter", 370, 145, self.ajouter_contact),
    ("✏️ Modifier", 370, 195, self.modifier_contact),
    ("🗑️ Supprimer", 370, 245, self.supprimer_contact),
    ("🔄 Actualiser", 370, 295, self.afficher_tout)
]

for text, x, y, fonction in btn_config:
    btn = QPushButton(self)
    btn.setText(text)
    btn.setGeometry(x, y, 150, 40)
    btn.clicked.connect(fonction)
