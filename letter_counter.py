# Program: Letter Counter App
# Description: This program counts occurrences of a specific letter in a message

#====== Welcome and User Input Section ======#
# Display welcome message
print("Welcome to my Letter counter app!")

# Get user's name and capitalize it
user_name = input("What is your name?")
user_name = user_name.title()

# Print personalized greeting
print(f"Hello {user_name}!")

#====== Program Purpose Section ======#
# Explain the program's goal to the user
print("I will count the number of times that a specific letter ocurs in a message")

#====== Message Input Section ======#
# Get message from user
while True:
    message_input = input("Please enter a message: ")
    if message_input.strip():  # Check if message is not empty after removing whitespace
        break
    print("Message cannot be empty. Please try again.")

# Get letter to count from user with validation
while True:
    letter_to_count = input("Which letter would you like me to count the occurrences of: ")
    if len(letter_to_count.strip()) == 1 and letter_to_count.isalpha():
        break
    print("Please enter a single letter.")

# Convert both message and letter to lowercase for case-insensitive counting
message_lower = message_input.lower()
letter_lower = letter_to_count.lower()

#====== Letter Counting Section ======#
# Create letter_count variable
# Use .count() method to count occurrences
# Store the result
letter_count = message_lower.count(letter_lower) #counts the number of instances of the letter in the message variable

#====== Result Output Section ======#
# Display formatted message with user's name and count result
print(f"{user_name}, your message has {letter_count} {letter_to_count}'s in it")

print(f"{user_name}, Thank you for testing my app!")