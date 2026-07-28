from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.services import analyze_review

from concurrent.futures import TimeoutError

app = FastAPI(title="Review Analyzer API", version="1.0.0")

@app.get("/")
def home():
    return {
        "message": "API opérationnelle"
    }
    
# Modele de requete
class ReviewRequest(BaseModel):
    text: str
    
@app.post("/analyze-review")
def analyze(request: ReviewRequest):
    try:
        return analyze_review(request.text)

    except TimeoutError:
        raise HTTPException(
            status_code=504,
            detail="L'analyse a dépassé le délai maximal."
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Une erreur est survenue lors de l'analyse."
        )