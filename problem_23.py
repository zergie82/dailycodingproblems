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

def is_allowed(point, board):
    M = len(board)
    N = len(board[0])
    x, y = point

    if  x < 0 or y <0: 
        return False
    elif x >= M or y >= N:
        return False
    elif board[x][y]:
        return False
    else:
        return True

def play(board, start, end):
    x, y = start
    visited, queue = [], deque()
    queue.append((x, y))
    visited.append((x, y))

    #while queue:
    #    cx, cy = queue.popleft()
    #    for next_point in ((cx + 1, cy), (cx -1, cy), (cx, cy + 1), (cx, cy - 1)):
    #        if is_allowed(next_point, board):
    #            if next_point not in visited:
    #                visited.append(next_point)
    #                queue.append(next_point)
    #                if next_point == end:
    #                    break
    #    return visited
    def bfs():
        while queue:
            cx, cy = queue.popleft()
            for next_point in ((cx + 1, cy), (cx -1, cy), (cx, cy + 1), (cx, cy - 1)):
                if is_allowed(next_point, board):
                    if next_point not in visited:
                        visited.append(next_point)
                        queue.append(next_point)
                        if next_point == end:
                            break




if __name__ == '__main__':
    board = [
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]
    ]

    start = (3, 0)
    end = (0, 0)
