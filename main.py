greeting = ("Welcome to your very own day trip generator!")
print(greeting)


import random
valid_response = False
destinations = ['Makapuu', 'Kaimana', 'Ala Moana', 'Kualoa']

while valid_response == False:
    user_input = input(f"Would you like to go to {random.choice(destinations)}? ")
    if user_input == "No":
        print("How about we try somewhere else.")
        valid_response = False
    elif user_input == "Yes":
        print("I love that location!")
        valid_response = True
    else:
        print("Please answer with Yes or No.")       
    
import random
valid_response = False
restaurants = ['Ono Ya', 'Foodland', 'Waikane Chicken', 'L&L']

while valid_response == False:
    user_input = input(f"How would you like to eat at {random.choice(restaurants)}? ")
    if user_input == "No":
        print("I don't like to eat there either.")
        valid_response = False
    elif user_input == "Yes":
        print("They have the best food on the island!")
        valid_response = True
    else:
        print("Please answer with Yes or No.")

import random
valid_response = False
transportation_mode = ['Bike', 'Bus', 'Surfboard','Car']

while valid_response == False:
    user_input = input(f"Would you like to travel by {random.choice(transportation_mode)}? ")
    if user_input == "No":
        print("Let's find a different way to travel.")
        valid_response = False
    elif user_input == "Yes":
        print("That's the easiest way to get around.")
        valid_response = True
    else:
        print("Please answer with Yes or No.")

import random
valid_response = False
entertainment_options = ['Surfing', 'Hiking', 'Sightseeing', 'Diving']

while valid_response == False:
    user_input = input(f"How does {(random.choice(entertainment_options))} sound? ")
    if user_input == "No":
        print("We can find something else to do.")
        valid_response = False
    elif user_input == "Yes":
        print("That is such a fun thing to do!")
        valid_response = True
    else:
        print("Please answer with Yes or No.")



