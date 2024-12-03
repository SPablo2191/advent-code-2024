import re
from advent.tools.reader import read_output

INPUT_DATA = "advent/day_03/input.txt"
regex = r"mul\((\d{1,3}),(\d{1,3})\)"


def main():
    lines = read_output(INPUT_DATA)
    acc = 0
    for line in lines:
        matches = re.findall(regex, line)
        if matches:
            for match in matches:
                acc += int(match[0]) * int(match[1])
    print(acc)


if __name__ == "__main__":
    main()
