FILES IN THE PROJECT:

There are 3 files within this project.

driver.py : main part of the program. Manages user interactions. 
Communicates with the encryption.py and logger.py files in order to perform necessary actions. 
Creates two subprocesses to handle the logger and encryption program, whose standard input and outputs are connected to the main program by pipes.

encryption.py : performs the encryption and decrpytion commands using the Vigenère cipher. 
It recieves a passkey from driver.py, processes commands and returns the result to the main program.

logger.py : writes messages to a log file (specified from the command line).
Log messages are written in the format: YYYY-MM-DD HH:MM [ACTION] MESSAGE. It accepts messages until it recieves a "QUIT" command.


HOW TO RUN THE PROGRAM:

1. cd into the proper directory in the command prompt. ( cd C:\...\cs4348\Project1)
2. Run the driver.py file along with the name you want for the log file (python driver.py <logfile.txt> )
3. A menu will print with avaliable options, and you can follow instructions as directed. There will be a "Press Enter to Continue" between each action.

