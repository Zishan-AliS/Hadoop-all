import sys

for line in sys.stdin:
    number = line.strip()
    if number:
        doubled = int(number) * 2
        print(f"number\t{doubled}")
