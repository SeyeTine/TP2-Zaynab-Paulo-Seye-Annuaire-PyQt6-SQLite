# Labels et champs de saisie
labels_text = ["Nom:", "Prénom:", "Téléphone:", "Email:"]
self.line_edits = []

for i, label_text in enumerate(labels_text):
    # Label
    label = QLabel(self)
    label.setText(label_text)
    label.setGeometry(35, 145 + i * 50, 120, 30)
# Labels et champs de saisie
labels_text = ["Nom:", "Prénom:", "Téléphone:", "Email:"]
self.line_edits = []

for i, label_text in enumerate(labels_text):
    # Label
    label = QLabel(self)
    label.setText(label_text)
    label.setGeometry(35, 145 + i * 50, 120, 30)
