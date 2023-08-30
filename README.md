# Travel Itinerary Generator

This is a Flask-based web application that uses the OpenAI GPT-3.5 model to generate custom travel itineraries based on user preferences.

## Setup

1. Clone the repository:

\```
git clone https://github.com/yourusername/travel-itinerary-generator.git
cd travel-itinerary-generator
\```

2. Set up a Python virtual environment and install the required dependencies:

\```bash
make env
\```

3. Create an environment variable for your OpenAI API key:

\```bash
export OPENAI_API_KEY=your-openai-api-key
\```

Replace `your-openai-api-key` with your actual OpenAI API key.

## Usage

1. Activate the virtual environment:

\```bash
source venv/bin/activate
\```

2. Run the Flask application from the repository root:

\```bash
python app/main.py
\```

The Flask server will start, and you can access the application at `http://localhost:5000`.

3. To generate a travel itinerary, navigate to `http://localhost:5000` in your web browser. Enter your travel preferences in the form and click the "Generate Itinerary" button. The generated itinerary will be displayed on the page.

4. To stop the Flask application, press `Ctrl+C` in the terminal.

5. To deactivate the virtual environment:

\```bash
deactivate
\```

6. To clean up the environment (deactivate and delete the virtual environment):

\```bash
make clean
\```

## Details

This application uses the OpenAI GPT-3.5 model to generate custom travel itineraries. The user's preferences are used to generate a prompt, which is passed to the GPT-3.5 model via the OpenAI API. The model generates a response, which is parsed and displayed as the custom travel itinerary.

This project is a demonstration of how OpenAI's powerful GPT-3.5 model can be used to create practical applications. The generated itineraries are for demonstration purposes and may not be entirely accurate or realistic.

## Disclaimer

This project is not affiliated with, sponsored by, or endorsed by OpenAI.
