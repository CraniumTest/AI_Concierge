import language_processor
import user_preferences
import hotel_system_interface
import local_insights

def main():
    print("Welcome to AI Concierge")
    
    while True:
        user_input = input("How can I assist you today? (Type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using AI Concierge. Have a great day!")
            break
        
        response = language_processor.process_input(user_input)
        personalized_response = user_preferences.apply_preferences(response)
        
        print(personalized_response)

if __name__ == "__main__":
    main()
