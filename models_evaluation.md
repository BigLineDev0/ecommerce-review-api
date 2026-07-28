## Modèle 1 : cmarkea/distilcamembert-base-sentiment
 
- **Lien** : https://huggingface.co/cmarkea/distilcamembert-base-sentiment
- **Taille** : environ 272 Mo (poids `safetensors`)
- **Licence** : MIT — usage commercial autorisé sans restriction
- **Langue** : français uniquement
- **Architecture** : DistilCamemBERT, une version distillée de CamemBERT
  (modèle RoBERTa entraîné sur du texte français). La distillation divise
  le temps d'inférence par deux par rapport à CamemBERT pour une précision
  quasi équivalente.
- **Entraînement** : avis Amazon et critiques Allociné, ramenés à une
  échelle de 1 à 5 étoiles.
- **Sortie** : 5 classes (`1 star` à `5 stars`), converties en `Positif`,
  `Neutre`, `Négatif` dans l'API.


## Modèle 2 : nlptown/bert-base-multilingual-uncased-sentiment
 
- **Lien** : https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment
- **Taille** : environ 669 Mo (poids `safetensors`)
- **Licence** : MIT — usage commercial autorisé sans restriction
- **Langues** : anglais, néerlandais, allemand, français, italien, espagnol
- **Architecture** : bert-base-multilingual-uncased, finetuné pour la
  classification de sentiment sur des avis produits.
- **Sortie** : 5 classes (`1 star` à `5 stars`), même logique de conversion
  que le modèle 1.

## Comparatif
 
| Critère                        | DistilCamemBERT-sentiment | mBERT multilingual sentiment |
|--------------------------------|----------------------------|-------------------------------|
| Taille                         | ~272 Mo                    | ~669 Mo                       |
| Licence                        | MIT                         | MIT                            |
| Adaptation au français         | Spécialisé français         | Correcte mais généraliste      |
| Vitesse d'inférence            | Rapide (modèle distillé)    | Plus lente (modèle plus lourd) |
| Couverture multilingue         | Aucune                      | 6 langues                      |
 
## Choix final
 
**Modèle retenu : `cmarkea/distilcamembert-base-sentiment`**
 
Justification :
 
- La plateforme cible des avis rédigés en français ; un modèle spécialisé
  français offre une meilleure qualité de classification qu'un modèle
  multilingue généraliste sur cette langue.
- Sa taille réduite (~272 Mo contre ~669 Mo) et son architecture distillée
  réduisent la latence par requête et l'empreinte mémoire du service, deux
  critères explicitement demandés dans le cahier des charges.
- La licence MIT autorise sans ambiguïté un usage commercial.
Le modèle `nlptown/bert-base-multilingual-uncased-sentiment` reste une
option pertinente si la plateforme devait traiter des avis dans plusieurs
langues (marché sous-régional par exemple) ; le nom du modèle chargé est
donc géré via la variable d'environnement `MODEL_NAME` pour permettre de
basculer de l'un à l'autre sans modifier le code.