import re
from advent.tools.reader import read_output

INPUT_DATA = "advent/day_04/input.txt"
MAGIC_WORD = "XMAS"


def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Check if the given center forms an X-MAS
    def is_xmas(x, y):
        # Check bounds
        if x - 1 < 0 or x + 1 >= rows or y - 1 < 0 or y + 1 >= cols:
            return False

        # Define the two MAS sequences
        mas1 = [
            grid[x - 1][y - 1],
            grid[x][y],
            grid[x + 1][y + 1],
        ]  # Top-left to bottom-right
        mas2 = [
            grid[x + 1][y - 1],
            grid[x][y],
            grid[x - 1][y + 1],
        ]  # Bottom-left to top-right

        # Check if either MAS forms an X-MAS
        return (mas1 == ["M", "A", "S"] or mas1 == ["S", "A", "M"]) and (
            mas2 == ["M", "A", "S"] or mas2 == ["S", "A", "M"]
        )

    # Traverse the grid
    for r in range(rows):
        for c in range(cols):
            if is_xmas(r, c):
                count += 1

    return count


def main():
    data = read_output(INPUT_DATA)
    grid = [[value for value in row if value != "\n"] for row in data]
    occurrences = count_word_occurrences(grid, MAGIC_WORD)
    print(occurrences)
