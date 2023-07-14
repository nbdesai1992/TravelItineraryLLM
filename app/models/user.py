class User:
    def __init__(self, destination, accommodation, activities, food, budget):
        self.destination = destination
        self.accommodation = accommodation
        self.activities = activities
        self.food = food
        self.budget = budget

    def __str__(self):
        return f"Destination: {self.destination}, Accommodation: {self.accommodation}, Activities: {self.activities}, Food: {self.food}, Budget: {self.budget}"

    @staticmethod
    def from_input():
        destination = input("Enter your preferred destination: ")
        accommodation = input("Enter your preferred type of accommodation (e.g. hotel, hostel, bed & breakfast, etc.): ")
        activities = input("Enter your preferred types of activities (e.g. nature, culture, adventure, relaxation, etc.): ")
        food = input("Enter any specific food preferences: ")
        budget = input("Enter your budget range: ")

        return User(destination, accommodation, activities, food, budget)
