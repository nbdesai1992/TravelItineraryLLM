import re

from flask import Flask, request, render_template
from models.user import User
from services.openai_service import OpenAIService

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    itinerary = {}
    user = None  # Initialize user here

    if request.method == 'POST':
        location = request.form.get('location')
        days = int(request.form.get('days'))
        budget = request.form.get('budget')
        activities = request.form.get('activities')
        cuisine = request.form.get('cuisine')

        user = User(location=location, days=days, budget=budget, activities=activities, cuisine=cuisine)

        service = OpenAIService()
        itinerary_string = service.generate_itinerary(user.preferences)
        #print(itinerary_string)

        if itinerary_string:
            days_splits = re.split(r'(Day \d+)', itinerary_string)
            for i in range(1, len(days_splits), 2): # Skipping over the non-"Day x" pieces
                day = days_splits[i].strip()
                content = days_splits[i + 1].strip().lstrip(": - ")
                activities = {}

                morning = ""
                afternoon = ""

                if "Morning:" in content:
                    morning, rest = content.split("Morning:", 1)
                    morning = morning.strip().lstrip("- ").rstrip("-")
                    if "Afternoon:" in rest:
                        morning_activities, afternoon = rest.split("Afternoon:", 1)
                        morning += " " + morning_activities.strip().lstrip("- ").rstrip("-")
                        afternoon = afternoon.strip().lstrip("- ").rstrip("-")
                    else:
                        afternoon = ""

                if "Afternoon:" in content and not morning:
                    afternoon, rest = content.split("Afternoon:", 1)
                    afternoon = afternoon.strip().lstrip("- ").rstrip("-")

                activities["morning"] = morning
                activities["afternoon"] = afternoon

                itinerary[day] = activities
        else:
            return "Error: Could not generate itinerary. Please check your input and try again."

    return render_template('index.html', itinerary=itinerary, user=user)

if __name__ == "__main__":
    app.run(debug=True)
