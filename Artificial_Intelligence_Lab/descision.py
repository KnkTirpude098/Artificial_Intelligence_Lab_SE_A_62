# Decision making program for selecting one subject out of 3

print("Select a subject from the following:")
print("1. Mathematics")
print("2. Physics")
print("3. Computer Science")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    print("You have selected Mathematics.")
elif choice == 2:
    print("You have selected Physics.")
elif choice == 3:
    print("You have selected Computer Science.")
else:
    print("Invalid choice. Please select a number between 1 and 3.")

