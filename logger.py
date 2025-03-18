import sys
import datetime

def main():
    if len(sys.argv) != 2:
        print("Usage: python logger.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]

    with open(log_file, "a") as f:
        while True:
            try:
                line = input().strip()
                if not line:
                    continue

                if line.startswith("QUIT"):
                    break 
                
                current_time = datetime.datetime.now().strftime( "%Y-%m-%d %H:%M" )

                words = line.split()
                action = words[0]
                message = ' '.join( words[1:] )

                newLine = current_time + ' [' + action + '] ' + message

                f.write(newLine + "\n")
                f.flush()
            except EOFError:
                break 

if __name__ == "__main__":
    main()
