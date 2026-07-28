# E-commerce Review Analyzer API

## Description

Cette application est un micro-service développé avec **FastAPI** permettant d'analyser automatiquement les avis clients d'une plateforme e-commerce.

L'API réalise deux traitements :

* Analyse du sentiment d'un avis (Positif, Neutre ou Négatif).
* Détection des avis urgents grâce à une liste de mots-clés.

Le modèle d'intelligence artificielle est chargé une seule fois au démarrage de l'application afin d'améliorer les performances.

---

# Fonctionnalités

* Analyse automatique du sentiment.
* Détection des avis urgents.
* Chargement unique du modèle Hugging Face.
* Variables d'environnement avec fichier `.env`.
* Documentation interactive Swagger.
* Gestion des erreurs (texte vide, texte trop long, timeout).

---

# Technologies utilisées

* Python 3.12+
* FastAPI
* Uvicorn
* Hugging Face Transformers
* PyTorch
* python-dotenv
* SentencePiece
* Protobuf

---

# Structure du projet

```text
ecommerce-review-api/
│
├── app/
│   ├── main.py
│   └── services.py
│
├── .env.example
├── requirements.txt
├── models_evaluation.md
└── README.md
```

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/BigLineDev0/ecommerce-review-api.git
cd ecommerce-review-api
```

---

## 2. Créer un environnement virtuel

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 4. Créer le fichier `.env`

Copier le fichier d'exemple :

```bash
cp .env.example .env
```

Puis compléter les valeurs :

```dotenv
HF_TOKEN=hf_votre_token
MODEL_NAME=cmarkea/distilcamembert-base-sentiment
MAX_TEXT_LENGTH=1000
```

---

# Lancer le serveur

Depuis la racine du projet :

```bash
uvicorn app.main:app --reload
```

Le serveur sera disponible à l'adresse :

```
http://127.0.0.1:8000
```

---

# Documentation interactive

Swagger UI :

```
http://127.0.0.1:8000/docs
```

Documentation ReDoc :

```
http://127.0.0.1:8000/redoc
```

---

# Endpoint principal

## POST `/analyze-review`

Analyse un avis client.

### Corps de la requête

```json
{
    "text": "Le produit est arrivé cassé et je souhaite un remboursement."
}
```

### Exemple de réponse

```json
{
    "sentiment": "Négatif",
    "confidence": 0.9987,
    "is_urgent": true
}
```

---

# Variables d'environnement

| Variable        | Description                            |
| --------------- | -------------------------------------- |
| HF_TOKEN        | Token d'accès Hugging Face             |
| MODEL_NAME      | Nom du modèle Hugging Face             |
| MAX_TEXT_LENGTH | Nombre maximal de caractères autorisés |

---

# Gestion des erreurs

L'API retourne des erreurs HTTP adaptées aux différents cas :

| Code | Description                                       |
| ---- | ------------------------------------------------- |
| 200  | Analyse réalisée avec succès                      |
| 400  | Texte vide ou dépassement de la longueur maximale |
| 500  | Erreur interne du serveur                         |
| 504  | Temps d'analyse dépassé (timeout)                 |

---

# Choix du modèle

Le modèle retenu est :

```
cmarkea/distilcamembert-base-sentiment
```

Ce modèle a été choisi pour :

* son adaptation au français ;
* sa faible taille ;
* sa rapidité d'inférence ;
* sa licence MIT compatible avec un usage commercial.

---

# Auteur

Projet réalisé dans le cadre de l'atelier :

**Le Filtre Intelligent et Sécurisé d'Avis E-commerce (Sentiment & Urgence)**

Formation Développement Web, Mobile et Intelligence Artificielle — Simplon Sénégal.
