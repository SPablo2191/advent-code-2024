import re
from advent.tools.reader import read_output

INPUT_DATA = "advent/day_04/input.txt"
MAGIC_WORD = "XMAS"


def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
    ]

    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, direction):
        dx, dy = direction
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for direction in directions:
                if search_from(r, c, direction):
                    count += 1

    return count


def main():
    data = read_output(INPUT_DATA)
    grid = [[value for value in row if value != "\n"] for row in data]
    occurrences = count_word_occurrences(grid, MAGIC_WORD)
    print(occurrences)
