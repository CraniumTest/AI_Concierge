from nlp_interaction import NLPInteraction
from recommendation import RecommendationEngine
from itinerary import ItineraryPlanner

if __name__ == "__main__":
    # Initialize components
    nlp_module = NLPInteraction()
    recommendation_engine = RecommendationEngine()
    itinerary_planner = ItineraryPlanner()

    # Example interaction
    guest_request = "I would like to plan a day's visit around the city and need dining recommendations for tonight."
    response = nlp_module.process_request(guest_request)
    
    # Get recommendations
    user_profile = {"past_stays": 2, "preferences": ["vegan", "spa", "historical sites"]}
    dining_recommendations = recommendation_engine.get_recommendations(user_profile, category="dining")
    
    # Plan itinerary
    preferences = {"interests": ["museums", "parks"], "weather": "sunny"}
    itinerary = itinerary_planner.create_daily_itinerary(preferences)
    
    # Print or log results for demonstration
    print(f"NLP Response: {response}")
    print(f"Dining Recommendations: {dining_recommendations}")
    print(f"Generated Itinerary: {itinerary}")
