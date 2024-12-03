from advent.tools.reader import read_output
from advent.day_01.part_one import get_papers


def main():
    lines = read_output("advent/day_01/input.txt")
    paper_1, paper_2 = get_papers(lines)
    if len(paper_1) != len(paper_2):
        print("Error: Different length of papers")
        return
    total_distance = 0
    for i in range(len(paper_1)):
        location_count = paper_2.count(paper_1[i])
        total_distance += int(paper_1[i]) * location_count
    print(total_distance)


if __name__ == "__main__":
    main()
