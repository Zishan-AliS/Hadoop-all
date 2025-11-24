import sys

for line in sys.stdin: # Read each line from standard input
    key, value = line.strip().split('\t') # Split the line into key and value
    print(f"{key}: {value}") # Output the key and value in a readable format
