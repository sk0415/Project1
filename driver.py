import sys
import subprocess
from subprocess import Popen, PIPE

currentPassword = None
history = []

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

def showHistory( fromMain = False ):
    global history

    print()
    print("-" * 35)
    print("               History               ")
    print("-" * 35)

    if history:
        for i, item in enumerate(history, 1):
            print(f"{i}. {item}")
        if not fromMain:
            print(f"{len(history) + 1}. (Go Back)")
    else:
        print("No history avaliable.") 
    
    print("-" * 35)
    print()

def configurePassword( encryption , logger ):

    log_message( logger , "SET_PASSWORD Setting passkey.")

    if history:
        answer = input( "Do you want to use a string from history? [y/n]" ).strip().lower()
        if( answer == "y" ):
            if not history:
                print( "No history avaliable." )
                newPassword = input( "Enter new password: ").strip()

                while not newPassword :
                    newPassword = input( "Password cannot be blank. Enter new password: ").strip()

                response = encryption_command( encryption , f"PASS {newPassword}" )
                if( response.startswith("RESULT") ):
                    log_message( logger , "SET_PASSWORD Success.")
                    print( "Password set succesfully.\n" )
                else:
                    log_message( logger , "SET_PASSWORD Error.")
                    print( "Error setting password.\n")
            else:
                showHistory()
                choice = input("Enter a number from history: ")

                if not choice.isdigit() or int(choice) < 0 or int(choice) > len(history):
                    print("Invalid choice. Try again.")
                    return

                if int(choice) == len( history ) + 1:
                    return
                elif choice.isdigit() and 1 <= int(choice) <= len(history):
                    newPassword = history[ int(choice) - 1 ]
                    response = encryption_command( encryption , f"PASS {newPassword}" )
                    log_message( logger , "SET_PASSWORD Success.")
                    print( "Password set succesfully.\n" )
                else:
                    print("Invalid Choice.")
                    return

        elif( answer == "n" ):
            newPassword = input( "Enter new password: ").strip()

            while not newPassword :
                newPassword = input( "Password cannot be blank. Enter new password: ").strip()
            
            if not newPassword.isalpha():
                print("ERROR: Password must contain only letters (A-Z).")
                return

            response = encryption_command( encryption , f"PASS {newPassword}" )
            if( response.startswith("RESULT") ):
                log_message( logger , "SET_PASSWORD Success.")
                print( "Password set succesfully.\n" )
            else:
                log_message( logger , "SET_PASSWORD Error.")
                print( "Error setting password.\n")
        else:
            print( "Invalid response.\n")
    
    else:
        newPassword = input( "Enter new password: ").strip()

        while not newPassword :
            newPassword = input( "Password cannot be blank. Enter new password: ").strip()
        
        if not newPassword.isalpha():
            print("ERROR: Password must contain only letters (A-Z).")
            return

        response = encryption_command( encryption , f"PASS {newPassword}" )
        if( response.startswith("RESULT") ):
            log_message( logger , "SET_PASSWORD Success.")
            print( "Password set succesfully.\n" )
        else:
            log_message( logger , "SET_PASSWORD Error.")
            print( "Error setting password.\n")

def encrypt( encryption , logger ):

    if history:
        answer = input( "Do you want to use a string from history? [y/n]" ).strip().lower()

        if answer == "y":
            showHistory()

            choice = input("Enter a number from history: ")

            if not choice.isdigit() or int(choice) < 0 or int(choice) > len(history):
                print("Invalid choice. Try again.")
                return

            if int(choice) == len( history ) + 1:
                return
            elif choice.isdigit() and 1 <= int(choice) <= len(history):
                word = history[ int(choice) - 1 ]
                
            else:
                print("Invalid Choice.")
                return

        elif answer == "n":
            word = input( "Enter string to encrypt: ").strip().upper()

            if not word or not word.isalpha():  
                print("ERROR: Input must contain only letters (A-Z).")
                return
            
            history.append( word.strip().upper() )
        else:
            print( "Invalid response.\n")
            return
    else: 
        word = input( "Enter string to encrypt: ").strip().upper()

        if not word or not word.isalpha():  
            print("ERROR: Input must contain only letters (A-Z).")
            return
        
        history.append( word.strip().upper() )
    
    log_message( logger , f"ENCRYPT {word}" )
    encryptedWord = encryption_command( encryption , f"ENCRYPT {word}")
    if( encryptedWord.startswith("RESULT") ):
        result = encryptedWord.split(":", 1)[1].strip()
        history.append( result.upper() )
        log_message( logger , f"ENCRYPT Success : {result}" )
    else:
        log_message( logger , "ENCRYPT Error : Passkey Not Set." )

    print( "\n" + encryptedWord )


def decrypt( encryption , logger ):

    if history:
        answer = input( "Do you want to use a string from history? [y/n]" ).strip().lower()

        if answer == "y":
            showHistory()
            choice = input("Enter a number from history: ")
            if not choice.isdigit() or int(choice) < 0 or int(choice) > len(history):
                print("Invalid choice. Try again.")
                return
            if int(choice) == len( history ) + 1:
                return
            elif choice.isdigit() and 1 <= int(choice) <= len(history):
                word = history[ int(choice) - 1 ]
            else:
                print("Invalid Choice.")
                return
        elif answer == "n":
            word = input( "Enter string to decrypt: ").strip().upper()

            if not word or not word.isalpha():  
                print("ERROR: Input must contain only letters (A-Z).")
                return
            
            history.append( word.strip().upper() )

        else:
            print( "Invalid response.\n")
            return
    else:
        word = input( "Enter string to decrypt: ").strip().upper()

        if not word or not word.isalpha():  
            print("ERROR: Input must contain only letters (A-Z).")
            return
        
        history.append( word.strip().upper() )

    
    log_message( logger , f"DECRYPT {word}" )
    decryptedWord = encryption_command( encryption , f"DECRYPT {word}")
    if( decryptedWord.startswith("RESULT") ):
        result = decryptedWord.split(":", 1)[1].strip()
        history.append( result.upper() )
        log_message( logger , f"DECRYPT Success : {result}" )
    else:
        log_message( logger , "DECRYPT Error : Passkey Not Set." )

    print( decryptedWord )

def main():
    if len(sys.argv) != 2:
        print( "Usage : python driver.py <log_file_name>.")
        sys.exit( 1 )

    log_fileName = sys.argv[1]

    logger = subprocess.Popen(['python' , 'logger.py' , log_fileName] , stdout = subprocess.PIPE , stdin = subprocess.PIPE , encoding = 'utf8')
    encryption = subprocess.Popen(['python' , 'encryption.py'] , stdout = subprocess.PIPE , stdin = subprocess.PIPE , encoding = 'utf8')

    log_message( logger , "START Driver program started.")

    while True:
        print_menu()

        command = input( "Enter command: ").strip().lower()

        if command == 'password':
            configurePassword( encryption , logger )

        elif command == 'encrypt':
            encrypt( encryption , logger )

        elif command == 'decrypt':
            decrypt( encryption , logger )

        elif command == 'history':
            showHistory( fromMain = True )
            log_message( logger , "HISTORY History Checked.")
            
        elif command == 'quit':
            encryption_command( encryption , command )
            log_message( logger , "STOP Program terminated." )
            print("Quitting.")
            break

        else:
            print( "Invalid command. Try again" )

        input( "\nPress Enter to Continue.\n" )

    logger.terminate()
    encryption.terminate()

if __name__ == '__main__':
    main()