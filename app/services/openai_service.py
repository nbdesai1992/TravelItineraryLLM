import openai
import json

openai.api_key = 'your-api-key'

class OpenAIService:
    @staticmethod
    def generate_itinerary(user_preferences):
        prompt = f"A custom travel itinerary based on the following preferences: {user_preferences}"
        
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=prompt,
          temperature=0.5,
          max_tokens=500
        )

        # The response is assumed to be in JSON format. Parse it into a dictionary
        try:
            details = json.loads(response.choices[0].text.strip())
        except json.JSONDecodeError:
            print("Error: The response from the OpenAI API is not in valid JSON format.")
            return None

        # Validate the structure of the dictionary
        if not OpenAIService._validate_itinerary(details):
            print("Error: The structure of the itinerary is invalid.")
            return None

        return details

    @staticmethod
    def _validate_itinerary(details):
        # An itinerary should include a schedule, accommodation, activities, and food.
        # If any of these keys is missing, the itinerary is invalid.
        required_keys = ['schedule', 'accommodation', 'activities', 'food']
        for key in required_keys:
            if key not in details:
                return False
        return True
