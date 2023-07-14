from models.user import User
from models.itinerary import Itinerary
from services.openai_service import OpenAIService

def main():
    while True:
        print("\n1. Create a custom travel itinerary")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user = User.from_input()
            itinerary_details = OpenAIService.generate_itinerary(str(user))
            
            if itinerary_details is not None:
                itinerary = Itinerary.from_dict(itinerary_details)
                print("\nYour custom itinerary is as follows:")
                print(itinerary)
            else:
                print("\nUnable to create itinerary. Please try again.")

        elif choice == '2':
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
