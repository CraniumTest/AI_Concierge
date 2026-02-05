class ItineraryPlanner:
    def create_daily_itinerary(self, preferences: dict) -> list:
        
        # Mock itinerary creation logic
        options = ["Museum Visit", "Park Walk", "Lunch at Local Cafe"]
        
        return [choice for choice in options if preferences["weather"] == "sunny"]
