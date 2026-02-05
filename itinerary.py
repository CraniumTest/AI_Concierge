class ItineraryPlanner:
    def create_daily_itinerary(self, preferences: dict) -> list:
        
        # Mock itinerary creation logic
        options = ["Museum visit", "Park walk", "Lunch At local cafe"]
        
        return [choice for choice in options if preferences["weather"] == "sunny"]
