class User:
    def __init__(self, location, days, budget, activities, cuisine):
        self.location = location
        self.days = int(days)
        self.budget = float(budget)
        self.activities = [activity.strip() for activity in activities.split(",")]
        self.cuisine = [food.strip() for food in cuisine.split(",")]

    @property
    def preferences(self):
        return {
            "location": self.location,
            "days": self.days,
            "budget": self.budget,
            "activities": self.activities,
            "cuisine": self.cuisine
        }
