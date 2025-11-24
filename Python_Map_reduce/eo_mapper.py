import sys

for line in sys.stdin:
    number = line.strip()
    if number:
        num = int(number)
        if num % 2 == 0:
            print("even\t1")
        else:
            print("odd\t1")
