class Itinerary:
    def __init__(self, details):
        self.schedule = details.get('schedule', [])
        self.accommodation = details.get('accommodation', '')
        self.activities = details.get('activities', [])
        self.food = details.get('food', [])

    def __str__(self):
        return (f"Schedule: {self.schedule}\n"
                f"Accommodation: {self.accommodation}\n"
                f"Activities: {self.activities}\n"
                f"Food: {self.food}\n")

    @staticmethod
    def from_dict(details):
        return Itinerary(details)
