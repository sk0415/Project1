import sys
from subprocess import Popen, PIPE

def log_message( logger , message ):
    logger.stdin.write( message + "\n" )
    logger.stdin.flush()

def encryption_command( encryption , command ):
    encryption.stdin.write( command + "\n" )
    encryption.stdin.flush()
    return encryption.stdout.readline().strip()

def main():
    if len(sys.argv) != 2:
        print( "Usage : python driver.py <log_file_name.")
        sys.exit( 1 )

    log_fileName = sys.argv[1]

    logger = Popen(['python' , 'logger.py' , log_fileName] , stdout = PIPE , stdin = PIPE , encoding = 'utf8')
    encryption = Popen(['python' , 'encryption.py'] , stdout = PIPE , stdin = PIPE , encoding = 'utf8')

    log_message( logger , "START : Driver program started.")

if __name__ == '__main__':
    main()