def main():
    with open("input.txt") as f:
        content = f.readlines()
        f.close()

    total_score = 0
    for line in content:
        list = line.rstrip().split(" ")
        if list[0] == "A":
            if list[1] == "X":
                # 1 point for rock, 3 points for draw
                total_score += 4
            if list[1] == "Y":
                # 2 points for paper, 6 points for win
                total_score += 8
            if list[1] == "Z":
                # 3 points for scissors, 0 points for lose
                total_score += 3
        if list[0] == "B":
            if list[1] == "X":
                # 1 point for rock, 0 points for lose
                total_score += 1
            if list[1] == "Y":
                # 2 points for paper, 3 points for draw
                total_score += 5
            if list[1] == "Z":
                # 3 points for scissors, 6 points for win
                total_score += 9
        if list[0] == "C":
            if list[1] == "X":
                # 1 point for rock, 6 points for win
                total_score += 7
            if list[1] == "Y":
                # 2 points for paper, 0 points for lose
                total_score += 2
            if list[1] == "Z":
                # 3 points for scissors, 3 points for draw
                total_score += 6

    print(f"Stragery points total: {total_score}")


if __name__ == "__main__":
    main()
