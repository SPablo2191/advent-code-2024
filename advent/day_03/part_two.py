import re
from advent.tools.reader import read_output

INPUT_DATA = "advent/day_03/input.txt"
regex = r"mul\((\d{1,3}),(\d{1,3})\)"
delimiters = r"don't\(\)|do\(\)"


def main():
    lines = read_output(INPUT_DATA)
    acc = 0
    for line in lines:
        parts = re.split(delimiters, line)
        for i in range(0, len(parts), 2):
            values = re.findall(regex, parts[i])
            if values:
                for value in values:
                    acc += int(value[0]) * int(value[1])
    print(acc)


if __name__ == "__main__":
    main()
