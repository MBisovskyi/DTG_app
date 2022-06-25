import random

list_of_destinations = ["Kyiv", "Ternopil", "Lviv", "Ivano-Frankivsk", "Vinnytsya", "Rivne", "Chernihiv", "Kherson", "Kharkiv", "Mariupol"]
list_of_transportations = ["Train", "Airplane", "Rental car", "Bicycle", "Bus", "a walk"]
list_of_entertainments = ['tour thru "Caves of Dovbush"', "Andrew's descent", "Baturin Castle", "The old fortress of Kamyanets-Podilsky", "Askania Nova Nature Reserve", '"Hoverla" hiking',  ]
list_of_restaurants = ["Bachevsky Restaurant", "Coffee Roasters Foundation", "Parovoz Speak Easy", "SHOco", "Fenix Asia, Fenix Italia", "Bunker"]
list_of_choises = []

def random_city():
    random_city = random.choice(list_of_destinations)
    return random_city

def random_transport():
    random_transport = random.choice(list_of_transportations)
    return random_transport

def random_enterteinment():
    random_entertainments = random.choice(list_of_entertainments)
    return random_entertainments

def random_restaurant():
    random_restaurant = random.choice(list_of_restaurants)
    return random_restaurant

def add_to_list(element):
    list_of_choises.append(element)
    
def trip_generator_completed_strings_concatenation(list_of_choises1,list_of_choises2,list_of_choises3, list_of_choises4):
    string = (f"Let's get a final look at your folowing trip. City you're going to is {list_of_choises1}. You'll get there by {list_of_choises2}. You will see {list_of_choises3}. Don't forget to take your loved one to {list_of_choises4}. Have a nice trip!")
    print(string)
def trip_generator():
        print("Hello! Looks like you want to generate a trip thru Ukraine today! I can help! Let's do it!")
        destination = True
        while destination is True:
            city = random_city()
            yes_or_no = input(f"Would you like to visit {city}? Yes/No?: ")
            if yes_or_no == "Yes" or yes_or_no == "yes" or yes_or_no == "y" or yes_or_no == "Y" or yes_or_no == "YEs" or yes_or_no == "YES" or yes_or_no == "yeS" or yes_or_no == "yES" or yes_or_no == "YeS":
                add_to_list(city)
                print("Great choice!")
                break
            else:
                print(f"Not a big deal.")
            continue
        print("Before, we go any further, you need to choose a transportation!")
        transportation = True
        while transportation is True:
            transport = random_transport()
            yes_or_no = input(f"Would you like to take {transport}? Yes/No?: ")
            if yes_or_no == "Yes" or yes_or_no == "yes" or yes_or_no == "y" or yes_or_no == "Y" or yes_or_no == "YEs" or yes_or_no == "YES" or yes_or_no == "yeS" or yes_or_no == "yES" or yes_or_no == "YeS":
                add_to_list(transport)
                print("That will be fun!")
                break
            else:
                print(f"I'll find something else!")
            continue
        print("Hm... What is next? Next is your pick of enterteinment!")
        enterteinment = True
        while enterteinment is True:
            place = random_enterteinment()
            yes_or_no = input(f'They can offer {place}. Yes/No?: ')
            if yes_or_no == "Yes" or yes_or_no == "yes" or yes_or_no == "y" or yes_or_no == "Y" or yes_or_no == "YEs" or yes_or_no == "YES" or yes_or_no == "yeS" or yes_or_no == "yES" or yes_or_no == "YeS":
                add_to_list(place)
                print("Such a great place to see!")
                break
            else:
                print(f"Don't you want to see {place}? Ok... keep moving.")
            continue
        print("Are you taking your loved one? Oh... not my bussines. The reason I'm asking is your next choice - restaurant!")
        restaurant = True
        while restaurant is True:
            food_place = random_restaurant()
            yes_or_no = input(f'"{food_place}" has a very high rate . Yes/No?: ')
            if yes_or_no == "Yes" or yes_or_no == "yes" or yes_or_no == "y" or yes_or_no == "Y" or yes_or_no == "YEs" or yes_or_no == "YES" or yes_or_no == "yeS" or yes_or_no == "yES" or yes_or_no == "YeS":
                add_to_list(food_place)
                print("You will like it, i'm sure!")
                break
            else:
                print(f"Yea, it doesn't look like tasty place.")
            continue

        is_trip_generated = True
        while is_trip_generated is True:
            print("Here is a trip we generated for you:")
            print(f"1. Destination - {list_of_choises[0]}")
            print(f"2. Transportation - {list_of_choises[1]}")
            print(f"3. Enterteinment - {list_of_choises[2]}")
            print(f"4. Restaurant - {list_of_choises[3]}")
            confirmation_answer_input = input("Do you want to keep it (Yes) or start it over (No)?: ")
            if confirmation_answer_input == confirmation_answer_input == "Yes" or confirmation_answer_input == "yes" or confirmation_answer_input == "y" or confirmation_answer_input == "Y" or confirmation_answer_input == "YEs" or confirmation_answer_input == "YES" or confirmation_answer_input == "yeS" or confirmation_answer_input == "yES" or confirmation_answer_input == "YeS":
                trip_generator_completed_strings_concatenation(list_of_choises[0], list_of_choises[1], list_of_choises[2], list_of_choises[3])
                break
            else:
                list_of_choises.clear()
                trip_generator()
                break
        
        

trip_generator()