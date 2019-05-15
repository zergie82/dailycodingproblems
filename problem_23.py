'''
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''

from collections import deque

def is_allowed(board, row, column):
    if  row < 0 or column <0: 
        return False
    elif row >= len(board) or column >= len(board[0]):
        return False
    return not board[row][column]

def possible_next(board, row, column):
    return [(r, c) for r, c in [
        (row, column - 1),
        (row - 1, column),
        (row + 1, column),
        (row, column + 1)]
        if is_allowed(board, r, c)
    ]

def play(board, start, end):
    visited, queue = set(), deque()
    queue.append((start, 0))

    while queue:
        cords, count = queue.popleft()
        if cords == end:
            return count
        visited.add(cords)
        neighbours = possible_next(board, cords[0], cords[1])
        queue.extend((neighbour, count + 1) for neighbour in neighbours if neighbour not in visited)

if __name__ == '__main__':
    board = [
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]
    ]

    start = (3, 0)
    end = (0, 0)
