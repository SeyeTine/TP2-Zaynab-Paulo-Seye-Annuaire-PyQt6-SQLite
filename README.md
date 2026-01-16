# TP2-Zaynab-Paulo-Seye-PyQt6-SQLite
420-2PR-BB TP2 Développement d’applications PyQt6-SQLite

# Membres de l’équipe
Seye Tine – 6384223
Paulo Gualberto Correa Fernandes – 63334211
Zaynab Ahdadouch – 2321875

# Description
Cette application est un carnet d’adresses personnel développé en Python avec PyQt6 et SQLite.
Elle propose une interface graphique permettant de gérer efficacement des contacts à l’aide des opérations CRUD (Creer, Ajouter, Supprimer ...).

# Fonctionnalités
➕ Ajouter des contacts avec validation des données
✏️ Modifier les informations d'un contact existant
🗑️ Supprimer des contacts avec confirmation
🔍 Rechercher des contacts en temps réel
🔄 Actualiser l'affichage et réinitialiser l'interface
✅ Validation automatique des emails

# Outils utilisées
Python - Language de programmation 
PyQt6 - Framework d'interface graphique
SQLite3 - Base de données intégrée

# Gestion de projet avec Github/Pycharm
Création du répertoire GitHub
Ajout des membres de l’équipe
Mise en place d’un tableau Kanban pour la gestion des tâches
Clonage du projet sur PyCharm
Création des issues et des branches associées
Développement du code sur chaque branche par la personne désignée
Commit régulier après chaque modification
Pull Request et merge vers la branche main

# Structure du projet

<img width="850" height="156" alt="image" src="https://github.com/user-attachments/assets/4330e362-88fb-4562-b2d2-685053743c06" />

# Des captures d’écran illustrant les fonctionnalités
Lorsqu'on lance l'application, on arriva à ce sésultat.

<img width="1223" height="818" alt="image" src="https://github.com/user-attachments/assets/82fb54bc-92d3-47dd-a499-998840d06b28" />


➕ Ajouter un contact

Dans la fonction d’ajout d’un contact, une contrainte de validation a été appliquée à l’adresse courriel.
Cela empêche l’utilisateur de saisir une valeur invalide.
En effet, le courriel doit obligatoirement contenir :
    le caractère @
    le caractère .
Si ces conditions ne sont pas respectées, l’ajout du contact est refusé et un message d’erreur est affiché à l’utilisateur.

<img width="1215" height="810" alt="image" src="https://github.com/user-attachments/assets/1fa4d077-0a7c-43f3-8ff8-54f8712a1257" />

<img width="1217" height="823" alt="image" src="https://github.com/user-attachments/assets/2fa2941f-e738-4003-a5e6-c39392f1fead" />

Cette capture d’écran démontre que l’ajout de trois contacts a été effectué avec succès et que les données sont correctement affichées dans l’interface

<img width="1213" height="812" alt="image" src="https://github.com/user-attachments/assets/d84db834-5ee4-4959-85ab-76fa4975bd93" />

✏️ Modifier un contact

<img width="1216" height="815" alt="image" src="https://github.com/user-attachments/assets/36c2670d-118d-4872-8766-efb54ccd28e3" />

Cette action montre que la fonctionnalité de modification fonctionne correctement, puisque le contact Tine a été mis à jour et que son prénom est passé de Seye à SeyeNabou.

<img width="1236" height="817" alt="image" src="https://github.com/user-attachments/assets/abf361ca-c5c8-4d34-a7b2-1a4ab12a93ce" />

🗑️ Supprimer un contact

<img width="1227" height="821" alt="image" src="https://github.com/user-attachments/assets/0d2e0eb5-4aa9-4a43-aa28-0a0f9d2f4180" />

Le contact toto a été ajouté uniquement dans le but de vérifier le bon fonctionnement de la fonctionnalité de suppression d’un contact.

<img width="1231" height="822" alt="image" src="https://github.com/user-attachments/assets/cbca3e09-4ae0-4391-b918-8f1c40cb1c18" />

🔍 Rechercher un contact

Dans ce projet, nous n’avons que trois contacts. Cependant, dans un véritable annuaire, le nombre de contacts peut être très élevé. Nous avons donc jugé nécessaire d’ajouter une fonctionnalité de recherche afin de faciliter et d’accélérer la recherche d’un contact.

<img width="1211" height="822" alt="image" src="https://github.com/user-attachments/assets/50cd5950-4567-4ccf-a128-51731a009451" />

🗄️ Vérifier le contenu de la base de données carnet_adresses.db

Ces captures montrent que notre base de données a été correctement créée et connectée à notre application graphique. Toutes les actions effectuées via l’interface sont automatiquement enregistrées dans la base de données.

Avant modification du contact Tine

<img width="960" height="182" alt="image" src="https://github.com/user-attachments/assets/c38e0dab-3ba7-426f-ae8d-8618bec925f9" />

Apres modification du contact Tine

<img width="952" height="182" alt="image" src="https://github.com/user-attachments/assets/c67b7857-d59f-46cd-ad4f-2e69f861febe" />

# Conclusion
Ce projet nous a permis de mettre en pratique le développement d’une application graphique complète en PyQt6, connectée à une base de données SQLite, tout en appliquant les principes CRUD et une bonne organisation du code.
