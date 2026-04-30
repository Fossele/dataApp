# Nom: Fossele Tazon Wilfried
# Matricule: 24G2430


# Analyse de l’impact du temps d’écran sur les performances scolaires des étudiants

## Description du projet

Cette application est un outil d’analyse de données et de machine learning permettant d’étudier l’impact du temps d’écran, du temps d’étude et du sommeil sur les performances académiques des étudiants.

Elle combine des techniques de collecte de données, d’analyse descriptive et de modèles d’apprentissage automatique pour fournir des insights sur les comportements des étudiants.

---

## Objectifs

- Collecter des données sur les habitudes quotidiennes des étudiants
- Réaliser une analyse descriptive des données
- Appliquer des modèles de machine learning pour la prédiction et la classification
- Identifier des profils d’étudiants à travers le clustering

---

## Fonctionnalités

### 1. Collecte des données
- Saisie manuelle des données
- Importation de fichiers CSV

### 2. Analyse descriptive
- Calcul des moyennes (temps d’écran, étude, sommeil, MGP)
- Identification des valeurs maximales et minimales
- Visualisation des données

### 3. Régression linéaire
- Prédiction du MGP à partir des habitudes des étudiants

### 4. Régression logistique
- Classification des étudiants en réussite ou échec

### 5. Clustering (KMeans)
- Regroupement des étudiants en profils similaires
- Identification des étudiants disciplinés et à risque

### 6. Prédiction interactive
- Estimation du MGP pour un nouvel étudiant

---

## Technologies utilisées

- Python
- Streamlit
- Pandas
- Scikit-learn (LinearRegression, LogisticRegression, KMeans)

---

## Structure du projet

- Interface utilisateur développée avec Streamlit
- Traitement des données avec Pandas
- Modèles de machine learning avec Scikit-learn
- Gestion des données en session avec Streamlit Session State

---

## Installation et exécution

### 1. Installer les dépendances
```bash
pip install streamlit pandas scikit-learn
````

### 2. Lancer l’application

```bash
streamlit run app.py
```

---

## Utilisation

1. Entrer ou importer des données d’étudiants
2. Consulter l’analyse descriptive
3. Observer les résultats des modèles de machine learning
4. Tester des prédictions en temps réel
5. Analyser les profils générés par le clustering

---

## Auteur

Fossele Tazon Wilfried

Projet réalisé dans le cadre du cours INF232 - Analyse de données et Machine Learning.

```
