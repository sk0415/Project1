import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python logger.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]

if __name__ == "__main__":
    main()
