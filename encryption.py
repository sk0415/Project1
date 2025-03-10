from itertools import starmap, cycle


def encrypt(message, key):
    message = filter(str.isalpha, message.upper())

    def enc(c, k):
        return chr(((ord(k) + ord(c) - 2 * ord('A')) % 26) + ord('A'))

    return ''.join(starmap(enc, zip(message, cycle(key))))


def decrypt(message, key):

    def dec(c, k):
        return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))

    return ''.join(starmap(dec, zip(message, cycle(key))))


def main():

    passkey = None

    while True:
        try:
            command = input().strip()
            args = None

            if not command:
                continue

            commandParts = command.split( " " , 1 )
            cmd = commandParts[0].upper()
            
            if( len(commandParts) > 1 ):
                args = commandParts[1].upper()

            if cmd == "PASS":
                passkey = args
                print( "RESULT : Passkey set.")

            elif cmd == "ENCRYPT":
                if passkey == None:
                    print( "ERROR : No Passkey set.")
                else:
                    encrypted = encrypt( args , passkey )
                    print( "RESULT : " , encrypted )

            elif cmd == "DECRYPT":
                if passkey == None:
                    print( "ERROR : No Passkey set.")
                else:
                    decrypted = decrypt( args , passkey )
                    print( "RESULT : " , decrypted )

            elif cmd == "QUIT":
                print( "RESULT : Quitting program.")
                break

            else:
                print( "ERROR : Unknown command. Try again. ")

        except EOFError:
             break

if __name__ == '__main__':
    main()