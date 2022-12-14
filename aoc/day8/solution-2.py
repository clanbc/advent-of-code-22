import numpy as np


def get_score_for_direction(trees, tree_height):
    # if all(true) i.e. tree_height is greater than all tress
    if all(tree_height > tree for tree in trees):
        return len(trees)
    # create an index, value of tress i.e. 0,x 1,y 2,z
    # then see how many you are higher than and return
    # that number
    for index, value in enumerate(trees):
        if value >= tree_height:
            return index + 1


def main():
    with open("input.txt") as f:
        content = f.read().splitlines()
        f.close()

    for (row, y) in zip(content, range(len(content))):
        content[y] = list(map(int, [*row]))

    forest = np.array(content)
    height, width = forest.shape

    max_score = -1

    for row in range(0, height):
        for col in range(0, width):
            tree_height = forest[row][col]
            score = 1

            up = np.flip(forest[:, col][0:row])
            down = forest[:, col][row:][1:]
            left = np.flip(forest[row][0:col])
            right = forest[row][col:][1:]

            score *= get_score_for_direction(up, tree_height)
            score *= get_score_for_direction(down, tree_height)
            score *= get_score_for_direction(left, tree_height)
            score *= get_score_for_direction(right, tree_height)

            max_score = max(score, max_score)
    print(max_score)


if __name__ == "__main__":
    main()
