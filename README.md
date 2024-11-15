# **Quiz App**

Bienvenue dans l'application **Quiz App**, une plateforme simple et interactive construite avec **Streamlit** pour créer et jouer à des questionnaires personnalisés.

---

## **Objectifs du Projet**

1. **Configurer un Quiz** : Permettre aux utilisateurs de saisir des questions, réponses, indices, et bonnes réponses.
2. **Jouer au Quiz** : Afficher une question à la fois, valider les réponses, et fournir un score final à la fin du quiz.

---

## **Technologies Utilisées**

- **Python** : Langage principal du projet.
- **Streamlit** : Framework pour créer des applications web interactives.
- **Pydantic** : Validation des données des questions.
- **JSON** : Stockage persistant des données du quiz.

---

## **Fonctionnalités**

### **1. Configurer le Quiz**
- L'utilisateur peut :
  - Ajouter une question.
  - Fournir une liste de réponses possibles (une réponse par ligne).
  - Ajouter un indice pour aider les joueurs.
  - Spécifier la bonne réponse.
- Les données sont validées avec **Pydantic** :
  - Minimum de 2 réponses obligatoires.
  - Message d'erreur si un champ est vide ou incorrect.
- Les questions sont enregistrées dans un fichier `question.json` pour un stockage permanent.

---

### **2. Jouer au Quiz**
- Les questions sont affichées une par une, avec :
  - La question.
  - Les options de réponse au format **QCM**.
  - Un bouton pour afficher un indice si nécessaire.
- Validation de la réponse :
  - **Bonne réponse** : Message de succès.
  - **Mauvaise réponse** : Message d'erreur.
- Score :
  - Le score est calculé dynamiquement en fonction des réponses correctes.
- Navigation :
  - **Valider** : Vérifie la réponse.
  - **Passer à la question suivante** : Charge la question suivante.
- Fin du quiz : Affiche le score final lorsque toutes les questions ont été répondues.

---

## **Pré-requis**

1. **Python 3.9 ou plus**.
2. Installer les dépendances :
   ```bash
   pip install streamlit pydantic
