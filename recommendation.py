import random

class RecommendationEngine:
    def __init__(self):
        # Initialization code e.g., loading models, embeddings etc.
        pass
    
    def get_recommendations(self, user_profile: dict, category: str) -> list:
        # Mock recommendation logic
        recommendations = {
            "dining": ["Gourmet Vegan Bistro", "Eco-Friendly Eatery"],
            "entertainment": ["Open-Air Concert", "Theater Show"]
        }
        return recommendations.get(category, [])
