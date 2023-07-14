# Custom Travel Itinerary Creator

This is a Python application that uses the OpenAI API to generate a custom travel itinerary based on user input. The user can specify their preferred destination, type of accommodation, activities, food, and budget. 

## Installation

1. Clone this repository.
2. Install the required Python dependencies by running `pip install -r requirements.txt` in the root directory of the repository.

## Usage

Run the application by executing `python app/main.py` in the root directory of the repository.

## Repository Structure

The repository contains the following files and directories:

- `app/`: This directory contains the main application code.
  - `models/`: This directory contains the data models.
    - `user.py`: This file defines the User class, which includes attributes for user preferences.
    - `itinerary.py`: This file defines the Itinerary class, which includes attributes for a travel itinerary.
  - `services/`: This directory contains the service classes.
    - `openai_service.py`: This file defines the OpenAIService class, which interacts with the OpenAI API.
  - `main.py`: This file includes the main application logic.
- `tests/`: This directory should contain unit tests for the application (currently not implemented).
- `.gitignore`: This file specifies what files and directories Git should ignore.
- `README.md`: This markdown file contains information about the project and instructions for usage.
- `requirements.txt`: This file lists the Python dependencies needed to run the application.
