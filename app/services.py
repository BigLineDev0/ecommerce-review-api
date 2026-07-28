import os
from dotenv import load_dotenv
from transformers import pipeline
from concurrent.futures import ThreadPoolExecutor, TimeoutError

executor = ThreadPoolExecutor(max_workers=1)

load_dotenv()

# Chargement des variables d'environement

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "cmarkea/distilcamembert-base-sentiment")
MAX_TEXT_LENGTH = int(os.getenv("MAX_TEXT_LENGTH", 1000))

if not MODEL_NAME:
    raise RuntimeError("La variable MODEL_NAME doit être définie dans .env")


# Chargement du modele
classifier = pipeline(
    task="sentiment-analysis",
    model=MODEL_NAME,
    token=HF_TOKEN
)

print("Modèle chargé avec succès !")

# Mot cles d'urgence
URGENT_KEYWORDS = [
    "arnaque",
    "escroquerie",
    "vol",
    "plainte",
    "justice",
    "urgent",
    "remboursement",
    "cassé",
    "défectueux",
    "litige",
    "danger",
]

def convert_label(label: str) -> str:
    """
    Convertit les labels du modèle
    (1 star -> negatif, etc.)
    """

    mapping = {
        "1 star": "Négatif",
        "2 stars": "Négatif",
        "3 stars": "Neutre",
        "4 stars": "Positif",
        "5 stars": "Positif",
    }

    return mapping.get(label.lower(), "inconnue")


def detect_urgency(text: str) -> bool:
    """
    Retourne True si le texte contient
    un mot-clé considéré comme urgent.
    """

    text = text.lower()

    return any(
        keyword in text
        for keyword in URGENT_KEYWORDS
    )

# Fonction principale
def analyze_review(text: str) -> dict:
    """
    Analyse un avis client.
    """

    # Validation
    if not text.strip():
        raise ValueError("Le texte est vide.")

    if len(text) > MAX_TEXT_LENGTH:
        raise ValueError(
            f"Le texte dépasse {MAX_TEXT_LENGTH} caractères."
        )

    # Appel du modèle
    future = executor.submit(classifier, text)

    try:
        result = future.result(timeout=10)[0]
    except TimeoutError:
        raise TimeoutError(
            "L'analyse a dépassé le délai maximal de 10 secondes."
        )
        
    label = result["label"]
    score = result["score"]

    # Conversion du sentiment

    sentiment = convert_label(label)

    # Détection urgence

    is_urgent = detect_urgency(text)

    # Réponse

    return {
        "sentiment": sentiment,
        "confidence": round(score, 4),
        "is_urgent": is_urgent,
    }

