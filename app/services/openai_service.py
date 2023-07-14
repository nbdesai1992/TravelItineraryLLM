import os
import openai
import json

class KeyManager:
    def get_api_key(self, keyName):
        d = json.load('keys/currentKeys.json')
        return d[keyName]

class OpenAIService:

    key = KeyManager()
    openai.api_key = key.get_api_key('NBDKey')
    
    @staticmethod
    def generate_itinerary(user_preferences):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"I need a travel itinerary. Here are my preferences: {user_preferences}"}
        ]
        
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages,
        )

        details = response["choices"][0]["message"]["content"]

        # The response is assumed to be in JSON format. Parse it into a dictionary
        # try:
        #     details = json.loads(response['choices'][0]['message']['content'])
        # except json.JSONDecodeError:
        #     print("Error: The response from the OpenAI API is not in valid JSON format.")
        #     return None

        # Validate the structure of the dictionary
        # if not OpenAIService._validate_itinerary(details):
        #     print("Error: The structure of the itinerary is invalid.")
        #     return None

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
    
