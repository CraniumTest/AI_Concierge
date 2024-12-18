import openai

class ConciergeService:
    def __init__(self, api_key):
        openai.api_key = api_key

    def request_service(self, user_input):
        try:
            response = openai.Completion.create(
              model="text-davinci-002",
              prompt=f"Concierge: {user_input}\nYou: ",
              temperature=0.5,
              max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {str(e)}"

# Example usage:
# concierge = ConciergeService(api_key='your_openai_api_key')
# response = concierge.request_service("I'd like to book a table at an Italian restaurant.")
