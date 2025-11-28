# ml_engine.py
"""
Moteur Machine Learning (préparation)
-------------------------------------
Ce module prépare l'intégration future d'un modèle de recommandation basé
sur le Machine Learning. Il n'est PAS utilisé pour l'instant.
"""

import logging

logger = logging.getLogger(__name__)


class MLRecommender:
    """Classe future pour gérer un modèle ML"""

    def __init__(self):
        self.model = None  
        logger.info("MLRecommender initialisé (pas encore utilisé).")

    def load_model(self, model_path: str):
        """
        Charge un modèle entraîné (futur)
        """
        logger.info(f"Tentative de chargement du modèle : {model_path}")

        # À remplacer plus tard par du vrai ML (scikit-learn, tensorflow...)
        try:
            # Exemple fictif
            self.model = f"MODELE_CHARGE_DEPUIS_{model_path}"
            logger.info("Modèle chargé avec succès.")
        except Exception as e:
            logger.error(f"Erreur chargement modèle : {e}")

    def predict(self, user_data):
        """
        Effectue une prédiction (futur)
        """
        if self.model is None:
            logger.warning("Aucun modèle chargé. ML non utilisé.")
            return []

        # Simulation d’une prédiction future
        logger.info("Prédiction ML effectuée (mock).")
        return ["resultat_1", "resultat_2"]
