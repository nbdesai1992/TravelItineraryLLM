from flask import Flask, request, render_template
from models.user import User
from models.itinerary import Itinerary
from services.openai_service import OpenAIService

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    itinerary = None
    if request.method == 'POST':
        location = request.form.get('location')
        days = request.form.get('days')
        budget = request.form.get('budget')
        activities = request.form.get('activities')
        cuisine = request.form.get('cuisine')

        user = User(location=location, days=days, budget=budget, activities=activities, cuisine=cuisine)

        service = OpenAIService()
        itinerary_details = service.generate_itinerary(user.preferences)

        if itinerary_details:
            itinerary = itinerary_details
        else:
            return "Error: Could not generate itinerary. Please check your input and try again."

    return render_template('index.html', itinerary=itinerary)

if __name__ == "__main__":
    app.run(debug=True)
