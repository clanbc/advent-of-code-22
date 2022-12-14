import numpy as np


def main():
    with open("input.txt") as f:
        content = f.read().splitlines()
        f.close()

    for (row, y) in zip(content, range(len(content))):
        content[y] = list(map(int, [*row]))

    forest = np.array(content)
    height, width = forest.shape
    edges = (2 * height) + (2 * width) - 4
    internal_trees = 0

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            tree_height = forest[row][col]
            up = forest[:, col][0:row]
            down = forest[:, col][row:][1:]
            left = forest[row][0:col]
            right = forest[row][col:][1:]

            if tree_height > np.amax(up):
                internal_trees += 1
                continue
            if tree_height > np.amax(down):
                internal_trees += 1
                continue
            if tree_height > np.amax(left):
                internal_trees += 1
                continue
            if tree_height > np.amax(right):
                internal_trees += 1
                continue

    print(edges + internal_trees)


if __name__ == "__main__":
    main()
