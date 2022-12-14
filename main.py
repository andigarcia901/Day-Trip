print('')
greeting = ("Welcome to the day trip generator!")
print(greeting)

print('')
print("First, lets find where to go for the day.")
print('')

import random

destinations = ['Makapuu', 'Kaimana', 'Ala Moana', 'Kualoa']
def random_destination_picker(list):    # we turned this into a function so we can control when it runs
    valid_response = False
    while valid_response == False:
        random_dest = random.choice(list)  # made a variable to hold the value so we could refer back to it later in the function
        user_input = input(f"Would you like to go to {random_dest}? (Yes or No) ")
        if user_input == "No":
            print("How about we try somewhere else.")
            valid_response = False
        elif user_input == "Yes":
            print("I love that location!")
            valid_response = True
            return random_dest   # added this retrun to extract the value the user approved 
        else:
            print("Please answer with Yes or No.")
random_destination = random_destination_picker(destinations)    # here we call the function but also catch the return value 

print('')  
print("You'll probably want some good food to eat.")
print('')

restaurants = ['Ono Ya', 'Foodland', 'Waikane Chicken', 'L&L']
def random_restaurant_picker(list):
    valid_response = False
    while valid_response == False:
        random_restaurant = random.choice(list)
        user_input = input(f"How would you like to eat at {random_restaurant}? (Yes or No) ")
        if user_input == "No":
            print("I don't like to eat there either.")
            valid_response = False
        elif user_input == "Yes":
            print("They have the best food on the island!")
            valid_response = True
            return random_restaurant
        else:
            print("Please answer with Yes or No.")
random_restaurant = random_restaurant_picker(restaurants)
      
print('')
print("There are lots of transportation options.")
print('')

transportation_mode = ['Bike', 'Bus', 'Surfboard','Car']
def random_transportation_picker(list):
    valid_response = False
    while valid_response == False:
        random_transportation = random.choice(list)
        user_input = input(f"Would you like to travel by {random_transportation}? (Yes or No) ")
        if user_input == "No":
            print("Let's find a different way to travel.")
            valid_response = False
        elif user_input == "Yes":
            print("That's the easiest way to get around.")
            valid_response = True
            return random_transportation
        else:
            print("Please answer with Yes or No.")
random_transportation = random_transportation_picker(transportation_mode)

print('')
print("Now we can decide what fun thing we can do.")
print('')

entertainment_options = ['Surfing', 'Hiking', 'Sightseeing', 'Diving']
def random_entertainment_picker(list):
    valid_response = False
    while valid_response == False:
        random_entertainment = random.choice(list)
        user_input = input(f"How does {random_entertainment} sound? ")
        if user_input == "No":
            print("We can find something else to do.")
            valid_response = False
        elif user_input == "Yes":
            print("That is such a fun thing to do!")
            valid_response = True
            return random_entertainment
        else:
            print("Please answer with Yes or No.")
random_entertainment = random_entertainment_picker(entertainment_options)

my_day_trip = {"destination": random_destination, 
"restaurant":random_restaurant,
"entertainment":random_entertainment, 
"transportation":random_transportation}   
print(my_day_trip)
print('')
print(f"For your day trip, you will be going to {random_destination} and eating at {random_restaurant}. You will also be going {random_entertainment} by way of {random_transportation}!")
print("")
print("Your trip is confirmed and we hope you enjoy your day here on the island.")

