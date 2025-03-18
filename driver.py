import sys
import subprocess
from subprocess import Popen, PIPE

def log_message( logger , message ):
    logger.stdin.write( message + "\n" )
    logger.stdin.flush()

def encryption_command( encryption , command ):
    encryption.stdin.write( command + "\n" )
    encryption.stdin.flush()
    return encryption.stdout.readline().strip()

def print_menu():
    print("              Menu                 ")
    print("-----------------------------------")
    print("password   - Set password for encryption/decryption")
    print("encrypt    - Encrypt string")
    print("decrypt    - Decrypt string")
    print("history    - Show history")
    print("quit       - Quit program")
    print("-----------------------------------")

def showHistory():
    print()

def main():
    if len(sys.argv) != 2:
        print( "Usage : python driver.py <log_file_name.")
        sys.exit( 1 )

    log_fileName = sys.argv[1]

    logger = subprocess.Popen(['python' , 'logger.py' , log_fileName] , stdout = subprocess.PIPE , stdin = subprocess.PIPE , encoding = 'utf8')
    encryption = subprocess.Popen(['python' , 'encryption.py'] , stdout = subprocess.PIPE , stdin = subprocess.PIPE , encoding = 'utf8')

    log_message( logger , "START Driver program started.")

    while True:
        print_menu()

        command = input( "Enter command: ").strip().lower()

        if command == 'password':
            print()
            
        elif command == 'encrypt':
            print()

        elif command == 'decrypt':
            print()

        elif command == 'history':
            showHistory()

        elif command == 'quit':
            encryption_command( encryption , command )
            log_message( logger , "STOP Program terminated." )
            break

        else:
            print( "Invalid command. Try again" )

    logger.terminate
    encryption.terminate

if __name__ == '__main__':
    main()