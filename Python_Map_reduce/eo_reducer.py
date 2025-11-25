import sys

even = 0
odd = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key == "even":
        even += int(value)
    else:
        odd += int(value)

print(f"even\t{even}")
print(f"odd\t{odd}")
