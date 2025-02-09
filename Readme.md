# Enregistrement des certifications dans la blockchain

## Auteurs
- Alexia NICOLEAU
- Thibaut MOSTEAU

## Description du Projet
Cette application MVP vise à démontrer la faisabilité d'un système de gestion des diplômes utilisant la technologie blockchain. L'objectif est de sécuriser et de rendre infalsifiables les diplômes et certifications délivrés par les établissements d'enseignement.

## Fonctionnalités Principales
- Émission de diplômes sur la blockchain
- Vérification de l'authenticité des diplômes
- Gestion des établissements autorisés

## Architecture Technique
- **Frontend** : HTML, CSS (Tailwind CSS), JavaScript
- **Backend** : Python (Flask)
- **Blockchain** : Ethereum (via Ganache pour le développement)
- **Smart Contract** : Solidity
- **Interaction Blockchain** : Web3.py

## Prérequis
- Python 3.8+
- Ganache (pour simuler la blockchain)
- Node.js et npm (pour Ganache)

## Installation
1. Cloner le dépôt :
```bash
git clone [adresse ssh du repo]
cd diploma_registry
```

2. Installer les dépendances Python :
```bash
pip install flask web3
```

3. Installer et lancer Ganache :
```bash
npm install -g ganache
ganache-cli
```

## Configuration
1. Démarrer Ganache (dans un terminal séparé) :
```bash
ganache-cli
```

2. Lancer l'application Flask :
```bash
python -m src.app
ou macos :
python3 -m src.app
```

L'application sera accessible à l'adresse : http://localhost:5000

## Utilisation
1. **Page d'accueil** : Vue d'ensemble des établissements autorisés et de l'état du réseau

2. **Émission de diplôme** :
   - Accéder à l'onglet "Émettre un Diplôme"
   - Remplir les informations du diplôme
   - Sélectionner l'établissement émetteur
   - Valider l'émission

3. **Vérification de diplôme** :
   - Accéder à l'onglet "Vérifier un Diplôme"
   - Entrer le hash du diplôme
   - Consulter les informations de validité

## Aspects Techniques Importants
- Les transactions sont simulées sur un réseau Ethereum local via Ganache
- Chaque établissement est représenté par une adresse Ethereum
- Les diplômes sont stockés de manière immuable dans la blockchain
- Le système utilise des smart contracts pour gérer les autorisations et les émissions

## Notes pour le Développement Futur
- Implémenter l'authentification des établissements
- Ajouter la gestion des métadonnées des diplômes
- Développer un système de révocation des diplômes
- Mettre en place une interface d'administration
- Intégrer un stockage décentralisé pour les documents
