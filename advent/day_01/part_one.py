from advent.tools.reader import read_output


def get_papers(lines):
    paper_1 = []
    paper_2 = []
    for line in lines:
        aux_1, aux2 = line.split("   ")
        paper_1.append(aux_1)
        aux_3 = aux2 if aux2[-1] != "\n" else aux2[:-1]
        paper_2.append(aux_3)
    paper_1.sort()
    paper_2.sort()
    return paper_1, paper_2


def main():
    lines = read_output("advent/day_01/input.txt")
    paper_1, paper_2 = get_papers(lines)
    if len(paper_1) != len(paper_2):
        print("Error: Different length of papers")
        return
    total_distance = 0
    for i in range(len(paper_1)):
        total_distance += abs(int(paper_1[i]) - int(paper_2[i]))
    print(total_distance)


if __name__ == "__main__":
    main()
