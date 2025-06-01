def main():
    while True:
        # Prompt for task input
        task = input("Enter your task: ")
        priority = input("Priority (high/medium/low): ").lower()
        time_bound = input("Is it time-bound? (yes/no): ").lower()

        # Process using match-case based on priority
        match priority:
            case "high":
                if time_bound == "yes":
                    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
                else:
                    print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
            case "medium":
                if time_bound == "yes":
                    print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
                else:
                    print(f"Reminder: '{task}' is a medium priority task. Plan to finish it soon.")
            case "low":
                if time_bound == "yes":
                    print(f"Reminder: '{task}' is a low priority task but it still requires attention today.")
                else:
                    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            case _:
                print("Invalid priority entered. Please choose from high, medium, or low.")

        # Ask if user wants to enter another task
        again = input("\nWould you like to enter another task? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye! Stay productive!")
            break

# Run the program
if __name__ == "__main__":
    main()
