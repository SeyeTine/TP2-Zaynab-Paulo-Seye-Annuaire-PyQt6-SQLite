# TP2-Zaynab-Paulo-Seye-PyQt6-SQLite
420-2PR-BB TP2 Développement d’applications PyQt6-SQLite

# Membres de l’équipe
Seye Tine – 6384223
Paulo Gualberto Correa Fernandes – 63334211
Zaynab Ahdadouch – 2321875

# Description
Cette application est un carnet d’adresses personnel développé en Python avec PyQt6 et SQLite.
Elle propose une interface graphique moderne, intuitive et conviviale permettant de gérer efficacement des contacts à l’aide des opérations CRUD (Create, Read, Update, Delete).

# Fonctionnalités
➕ Ajouter des contacts avec validation des données
✏️ Modifier les informations d'un contact existant
🗑️ Supprimer des contacts avec confirmation
🔍 Rechercher des contacts en temps réel
🔄 Actualiser l'affichage et réinitialiser l'interface
📊 Afficher tous les contacts dans un tableau interactif
✅ Validation automatique des emails

# Outils utilisées
Python 
PyQt6 - Framework d'interface graphique
SQLite3 - Base de données légère intégrée

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
<img width="1226" height="835" alt="image" src="https://github.com/user-attachments/assets/56cfe223-afa5-48f2-9c65-3d69a0b9e92f" />

➕ Ajouter un contact

Dans la fonction d’ajout d’un contact, une contrainte de validation a été appliquée à l’adresse courriel.
Cela empêche l’utilisateur de saisir une valeur invalide.
En effet, le courriel doit obligatoirement contenir :
    le caractère @
    le caractère .
Si ces conditions ne sont pas respectées, l’ajout du contact est refusé et un message d’erreur est affiché à l’utilisateur.

<img width="1228" height="820" alt="image" src="https://github.com/user-attachments/assets/6f63ae54-b20a-4ccd-b9ef-9a1b550fbf09" />

<img width="1227" height="836" alt="image" src="https://github.com/user-attachments/assets/05e3ea82-6d18-41bf-9d24-daf1c6688cef" />

Cette capture d’écran démontre que l’ajout de trois contacts a été effectué avec succès et que les données sont correctement affichées dans l’interface

<img width="1206" height="687" alt="image" src="https://github.com/user-attachments/assets/87531faa-73be-4663-8b45-ec8cbd7ffbd3" />

✏️ Modifier un contact

<img width="1190" height="631" alt="image" src="https://github.com/user-attachments/assets/05041c75-b92f-4f19-bb05-27c6bf18cfc3" />

Cette action montre que la fonctionnalité de modification fonctionne correctement, puisque le contact numéro 1 a été mis à jour et que son nom est passé de Seye à SeyeNabou.

<img width="1213" height="670" alt="image" src="https://github.com/user-attachments/assets/bf2a1580-09b6-490a-85b1-4a27d5951c76" />

🗑️ Supprimer un contact

<img width="1228" height="691" alt="image" src="https://github.com/user-attachments/assets/8955e32e-0e8e-49d7-a33d-1f41a6ef1bfb" />

Le contact toto a été ajouté uniquement dans le but de vérifier le bon fonctionnement de la fonctionnalité de suppression d’un contact.

<img width="1223" height="712" alt="image" src="https://github.com/user-attachments/assets/1bbcec4c-9963-4cb6-b15a-9dcd19f950af" />

🔍 Rechercher un contact

Dans ce projet, nous n’avons que trois contacts. Cependant, dans un véritable annuaire, le nombre de contacts peut être très élevé. Nous avons donc jugé nécessaire d’ajouter une fonctionnalité de recherche afin de faciliter et d’accélérer la recherche d’un contact.

<img width="1232" height="603" alt="image" src="https://github.com/user-attachments/assets/2e7451f1-c13b-416d-85dd-05d6cf893761" />

🗄️ Vérifier le contenu de la base de données carnet_adresses.db

Cette capture montre que notre base de données a été correctement créée et connectée à notre application graphique. Toutes les actions effectuées via l’interface sont automatiquement enregistrées dans la base de données.

<img width="986" height="288" alt="image" src="https://github.com/user-attachments/assets/30b863b8-dd18-491e-9a2e-22199d285481" />


✅ Conclusion
Ce projet nous a permis de mettre en pratique le développement d’une application graphique complète en PyQt6, connectée à une base de données SQLite, tout en appliquant les principes CRUD et une bonne organisation du code.
