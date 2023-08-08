import os
import openai
import json

class KeyManager:
    def get_api_key(self, key_name):
        with open('keys/currentKeys.json', 'r') as f:
            d = json.load(f)
        return d[key_name]


class OpenAIService:

    key = KeyManager()
    openai.api_key = key.get_api_key('NBDKey')

    @staticmethod
    def generate_itinerary(user_preferences):
        # Define the instruction for the model to generate a structured response
        instruction = f"Based on the user preferences: {user_preferences}, please provide a travel itinerary for each day in the following format: "
        example_format = "\"Day 1: - Morning: [Morning activities here]. - Afternoon: [Afternoon activities here].\""

        # Merge the instruction and example_format
        complete_prompt = instruction + example_format

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": complete_prompt}
        ]
        
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        )

        details = response["choices"][0]["message"]["content"]

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
    
