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
    n = len(report)
    for i in range(n):
        modified = report[:i] + report[i + 1 :]
        if is_safe(modified):
            return True
    return False


def is_safe(levels):
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    if all(1 <= abs(diff) <= 3 for diff in diffs):
        return all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)
    return False


def main():
    output = read_output(INPUT_DATA)
    reports = get_reports(output)
    safe_count = 0
    for report in reports:
        if is_safe(report) or is_valid_report(report):
            safe_count += 1
    print(safe_count)


if __name__ == "__main__":
    main()
