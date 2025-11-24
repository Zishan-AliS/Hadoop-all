import sys

for line in sys.stdin:
    key, value = line.strip().split('\t')
    print(f"{key}: {value}")
