def main():
    with open("input.txt") as f:
        content = f.readlines()
        f.close()

    total_score = 0
    for line in content:
        list = line.rstrip().split(" ")
        if list[0] == "A":
            if list[1] == "X":
                # I need to lose, play scissors
                # 0 for lose, 3 for scissors
                total_score += 3
            if list[1] == "Y":
                # I need to draw, play rock
                # 3 for draw, 1 for rock
                total_score += 4
            if list[1] == "Z":
                # I need to win, play paper
                # 6 for win, 2 for paper
                total_score += 8
        if list[0] == "B":
            if list[1] == "X":
                # I need to lose, play rock
                # 0 for lose, 1 for rock
                total_score += 1
            if list[1] == "Y":
                # I need to draw, play paper
                # 3 for draw, 2 for paper
                total_score += 5
            if list[1] == "Z":
                # I need to win, play scissors
                # 6 for win, 3 for scissors
                total_score += 9
        if list[0] == "C":
            if list[1] == "X":
                # I need to lose, play paper
                # 0 for lose, 2 for paper
                total_score += 2
            if list[1] == "Y":
                # I need to draw, play scissors
                # 3 for draw, 3 for scissors
                total_score += 6
            if list[1] == "Z":
                # I need to win, play rock
                # 6 points for win, 1 for rock
                total_score += 7

    print(f"Stragery points total: {total_score}")


if __name__ == "__main__":
    main()
