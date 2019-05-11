'''
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''

def build(matrix):
    n = len(matrix)
    k = len(matrix[0])
    solm = [[0] * k]

    for r, row in enumerate(matrix):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(min(solm[r][i] for i in range(k) if i != c) + val)
            print(f'row_cost: {row_cost}')
        solm.append(row_cost)
        print(f'solm: {solm}')
    return min(solm[-1])






if __name__ == '__main__':
    matrix = [
        [12, 4, 6, 9],
        [3, 25, 14, 16],
        [1, 12, 7, 18]
    ]
