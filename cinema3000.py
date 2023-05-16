import datetime   # import the datetime module
import json       # import the json module
import os         # import the os module

# Define function to load data from json file
def load_data(file_name):             # Define a function called load_data which accepts a parameter called file_name
    with open(file_name) as f:        # Open the file in read mode and store the file object in variable f
        data = json.load(f)           # Load the JSON data from the file into the data variable
    return data                       # Return the data

# Greet the user
print("Welcome to the movie booking system!")   # Print a welcome message to the user
print(" ")

# Get the path to the current file
current_file_path = os.path.abspath(__file__)

# Get the directory containing the current file
current_dir_path = os.path.dirname(current_file_path)

os.chdir(current_dir_path)

try:
    # Load the theater data from the theaters.json file
    theaters = load_data('theaters.json')
    # Load the movie data from the movies.json file
    movies = load_data('movies.json')
    # Load the booking data from the bookings.json file
    bookings = load_data('bookings.json')
except FileNotFoundError:
    # If any of the data files are not found in the specified directory, print an error message and continue the loop to ask for a valid path
    print("Data file not found in specified directory, please try again.")

# Print message indicating that data files have been successfully loaded
print("Data files loaded successfully!")

# Define function to display menu options
def display_menu():
    # Print the menu options for the user to select
    print("1. View movies for a specific date")
    print("2. Book a ticket")
    print("3. New movie")
    print("4. Exit")

#this funtion is display all avalaible movies to a date from input, inputs: movies file, output - date from user input
    
def display_movies(movies):
    # Ask the user for the date
    while True:
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            # Attempt to convert the entered date string to a datetime.date object
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            # If the entered date string cannot be converted to a datetime.date object, prompt the user to try again
            print("Error: Please enter a date in the format YYYY-MM-DD.")     

    # Display the available movies and show times for the specified date
    print(f"Available movies for {date}:")
    temp = 0 # Initialize a counter variable to keep track of available movies
    for movie in movies:
        # Check if the movie has been released before the specified date
        if datetime.datetime.strptime(movie["release_date"], "%Y-%m-%d").date() <= date:
            # Display the movie title and show times if it has been released before the specified date
            print(f"{movie['title']}: {', '.join(movie['show_times'])}")
            temp =+ 1 # Increment the counter variable for available movies
    if temp == 0:
        # If there are no available movies, display a message to the user
        print('No movies available')
    print(" ")
    return date # Return the specified date

#this funtion is used add new movie to file from user inputs, inputs: movies, theaters files
def add_movie(movies, theaters):
    # create an empty dictionary to store movie data
    movie = {}
    
    # Get movie title from user input
    while True:
        title = input("Enter movie title: ")
        if len(title) == 0:
            print("Title cannot be empty")
        else:
            movie['title'] = title
            break

    # Get movie price from user input
    while True:
        try:
            price = float(input("Enter movie price: "))
            if price < 0:
                print("Price cannot be negative")
            else:
                movie['price'] = price
                break
        except ValueError:
            print("Price must be a number")

    # Get movie release date from user input
    while True:
        release_date_str = input("Enter movie release date (YYYY-MM-DD): ")
        try:
            release_date = datetime.datetime.strptime(release_date_str, '%Y-%m-%d').date()
            today = datetime.date.today()
            if release_date > today:
                print("Release date cannot be in the future")
            else:
                movie['release_date'] = release_date_str
                break
        except ValueError:
            print("Release date must be in the format YYYY-MM-DD")

    # Get movie show times from user input
    show_times = []
    while True:
        show_time_str = input("Enter movie show time (HH:MM), or 'done' to finish: ")
        if show_time_str.lower() == 'done':
            if len(show_times) == 0:
                print("At least one show time must be specified")
            else:
                movie['show_times'] = show_times
                break
        else:
            try:
                show_time = datetime.datetime.strptime(show_time_str, '%H:%M').time()
                show_times.append(show_time_str)
            except ValueError:
                print("Show time must be in the format HH:MM")
    
    # Generate a unique id for the new movie
    if len(movies) > 0:
        movie_id = max([movie['id'] for movie in movies]) + 1
    else:
        movie_id = 1

    # Add the id to the movie dictionary
    movie['id'] = movie_id
    
    # Append the new movie to the list of movies
    movies.append(movie)

    # Write the updated list of movies to the file
    with open('movies.json', 'w') as f:
        json.dump(movies, f, indent=4)
    
    # Add movies to theater
    for t in theaters:
        t["movies"].append(movie)

    # Write theater data to file
    with open('theaters.json', 'w') as f:
        json.dump(theaters, f, indent=4)
    # Display success message
    print("Movie added successfully")
    print(" ")
    
#this funtion is used add new booking to file, based on  user inputs, inputs: movies, bookings, theaters files
def book_ticket(movies,bookings,theaters):
        
    # Print available cinemas
    print("Available Cinemas:")
    for i, theater in enumerate(theaters): # iterate over theaters data
        print(f"{i+1}. {theater['name']}") # print the theater name with an index
    
    # Get user input for theater name
    while True:
        theater_name = input("Enter the name of the cinema you want to book a ticket for: ") # ask the user to enter theater name
        cinema = next((t for t in theaters if t['name'] == theater_name), None) # search for the theater name in the theaters data
        if cinema is None:
            print("Invalid theater name. Please try again.") # error message for invalid theater name
        else:
            break
    print(' ')  
    
    # Display available movies and showtimes
    date = display_movies(movies) # call display_movies() function to show the available movies and showtimes

    # Get user input for movie and showtime
    while True:
        movie_name = input("Enter the movie name: ") # ask the user to enter the movie name
        movie = next((m for m in movies if m['title'] == movie_name), None) # search for the movie name in the movies data
        if movie is None:
            print("Invalid movie name. Please try again.") # error message for invalid movie name
        else:
            break
    print(' ') 
    
    while True:
        show_time = input("Enter the show time (HH:MM): ") # ask the user to enter the show time
        if show_time not in movie['show_times']:
            print("Invalid show time for the selected movie. Please try again.") # error message for invalid show time
        else:
            break
    print(' ') 
    
    # Get available seats for the selected movie and showtime
    available_seats = get_available_seats(theaters, bookings, movies, theater_name, movie_name, show_time, str(date)) # call get_available_seats() function to get the number of available seats

    if available_seats == 0:
        print("No seats available, choose other options") # error message if there are no available seats
        return            
            
    # Get the number of tickets from the user
    while True:
        try:
            num_tickets = int(input(f"Enter the number of tickets (max {available_seats}): ")) # ask the user to enter the number of tickets
            if num_tickets <= 0:
                print("Number of tickets must be greater than 0.") # error message for invalid number of tickets
            elif num_tickets > available_seats:
                print(f"Only {available_seats} seats are available. Please enter a number less than or equal to {available_seats}.") # error message for number of tickets greater than available seats
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.") # error message for invalid input
    print(' ')  
    
    # Get the user's name
    while True:
        # Prompt the user to input their name
        name = input("Enter your name: ")
        # Check if the user's name is empty and prompt them again if it is
        if not name:
            print("Name cannot be empty.")
        else:
            # Break out of the loop if the user's name is not empty
            break
    print(' ') 
    # Create a new booking

    # Generate a unique booking ID for the new booking
    if len(bookings) > 0:
        booking_id = max([booking['id'] for booking in bookings]) + 1
    else:
        booking_id = 1

    # Get the ID of the selected movie
    movie_id = next(movie['id'] for movie in movies if movie['title'] == movie_name)

    # Create a new booking dictionary
    booking = {
        'id': booking_id,
        'customer_name': name,
        'date' : date.strftime('%Y-%m-%d'),
        'time': show_time,
        'movie_id': movie_id,
        'num_seats': num_tickets,
        "cinema": theater_name
    }

    # Add the new booking to the list of bookings
    bookings.append(booking)

    # Save the updated bookings list to the JSON file
    with open('bookings.json', 'w') as f:
        json.dump(bookings, f, indent=4)

    # Print a success message
    print("Booking successful.")
    print(" ")

#this funtion is used find movie id based on its title, inputs: movies file and title
    
def get_movie_id(movie_title, movies):
    # Loop through each movie in the list of movies loaded from the file
    for movie in movies:
        # Check if the movie title matches the input movie_title
        if movie['title'] == movie_title:
            # If there's a match, return the movie ID
            return movie['id']
    # If there's no match, return None
    return None
 
#this funtion is used calculate avalaible seats for selected inputs from user, 
#inputs: theaters, bookings, movies, theater_name, movie, show_time, date
#output: number of seats left
    
def get_available_seats(theaters, bookings, movies, theater_name, movie, show_time, date):
    
    # Find the theater's total number of seats
    total_seats = next(theater['seats'] for theater in theaters if theater['name'] == theater_name)
    
    # Find the movie and showtime
    movie_data = next((m for m in movies if m['title'] == movie), None)
    if not movie_data:
        return f"No movie found with title {movie}"
    
    if show_time not in movie_data['show_times']:
        return f"{movie} does not have a showtime at {show_time}"
    # Calculate number of seats booked for the given showtime
    
    num_booked_seats = 0
    movie_title = movie
    for booking in bookings:
        if booking.get('cinema', booking.get('name')) == theater_name and \
           int(booking['movie_id']) == get_movie_id(movie_title, movies) and \
           booking.get('time', booking.get('show_time')) == show_time and \
           booking['date'] == date:
            num_booked_seats += booking.get('num_seats', booking.get('num_tickets', 0))

    # Calculate number of seats left
    num_seats_left = total_seats - num_booked_seats
    
    # Print the number of available seats and return the value
    print(f"There are {num_seats_left} seats left for {movie} at {show_time} on {date} at {theater_name}.")
    print(" ")
    return num_seats_left 

# Display the main menu
while True:
    display_menu()

    # Get user's choice
    choice = input("Enter your choice: ")

    # Check user's choice and call the appropriate function
    if choice == "1":
        # View movies for a specific date
        display_movies(movies)
    elif choice == "2":
        # Book a ticket
        book_ticket(movies,bookings,theaters)
    elif choice == "3":
        # Add a new movie
        add_movie(movies, theaters)
    elif choice == "4":
        # Exit
        break
    else:
        # Notify user of invalid input
        print("Invalid choice. Please enter a valid choice.")