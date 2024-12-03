from advent.tools.reader import read_output

INPUT_DATA = "advent/day_02/input.txt"


def get_reports(lines: list[str]):
    reports = []
    for line in lines:
        aux = line.split(" ")
        report = []
        for element in aux:
            report.append(int(element if element[-1] != "\n" else element[:-1]))
        reports.append(report)
    return reports


def is_valid_report(report: list[int]):
    for i in range(len(report) - 1):
        j = i + 1
        if not report[i] - report[j] in [1, 2, 3]:
            return False
    return True


def main():
    output = read_output(INPUT_DATA)
    reports = get_reports(output)
    safe_count = 0
    for report in reports:
        if is_valid_report(report):
            safe_count += 1
        if is_valid_report(report[::-1]):
            safe_count += 1
    print(safe_count)


if __name__ == "__main__":
    main()
