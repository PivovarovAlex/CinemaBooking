# CinemaBooking

This is my assignment for LMU MMT program. Link for tasks https://www.mmt.bwl.uni-muenchen.de/application/admissions/process/essay-application-ws2324.pdf


## Full task discription

CINEMA 3000 needs a new booking system, so their customers can easily buy their tickets for their favorite movies! 
Please write a booking program that helps you with this task. It should be able to record current movies and bookings. 

Further, the program should be able to: 
1. Read a file of previous bookings, theater characteristics and current movies from disk. 
2. Booking: The file is structured to include an ID of the transaction, customer name, date and time of the ticket, Movie ID. 
3. Movie: The file is structured to include an ID, title, price, release date, and a list of show times.
4. Theater: The theater should have number of seats, and a list of available movies.
5. Write additional bookings and movies to the file. You can choose txt, csv, json or xlsx as format for the transaction file. 

Interaction: 
- Your program should display to the user all the available movies for that day with the respective time slots. 
- Your program lets the user book a ticket. This function should update the number of available seats for that show time and add the purchased ticket to bookings transaction file. 
- More than one spot can be booked. For example, you are going with a friend and buy two tickets for the same movie and showtime. 
- When booked, the system shows a confirmation message to the client. 
- Exit the program. 
- The program shuts down gracefully without any error messages. Error handling is expected.

Please annotate each line of code with a comment explaining its purpose. Each method should have documentation as to what it does, how it works and what parameters are expected. The program should be standalone and executable from a standard computer with minimal amount of dependencies. The transaction file should be saved in the same directory. The interaction can be via a graphical user interface or a terminal. The selection of the interaction method has no influence on our evaluation of your code.

## How to run this program

To run this program, you need Python 3 installed on your computer, as well as the datetime, json, and os modules. These modules are typically included in a standard Python installation and should not require any additional installation steps. You also need to have three JSON files ('theaters.json', 'movies.json', and 'bookings.json') in the same directory as the Python file to load data from.

### To run a Python program on Mac OS: 

1. Open the Terminal application and navigate to the directory where your Python file is located. You can use the cd command to change directory. For example, to change to a directory using an absolute path: cd /Users/your-username/Desktop

2. Once you're in the directory containing the Python file, simply run the program by entering the following command in the terminal:
python cinema3000.py

This should execute your Python code and start the movie booking system.

### To run Python on Windows:

1. You can open the command prompt by pressing the Windows key + R, typing "cmd" in the Run dialog box, and pressing Enter.

2. In the command prompt, type "python" to open the Python interpreter. You should see the Python version number and the ">>>" prompt.

3. To run a Python script saved in a file, navigate to the directory where the file is saved using the "cd" command (like this cd C:\Users\UserName\Documents) and type "python cinema3000.py" to run the script.

This should execute your Python code and start the movie booking system.
