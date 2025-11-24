import sys

for line in sys.stdin: # Read each line from standard input
    number = line.strip()   # Remove leading/trailing whitespace
    if number:  # Ensure the line is not empty
        halved = float(number) / 2  # Double the number
        print(f"number\t{halved}") # Output the result in key-value format
