starting_crates = {
    "col_1": ["C", "Z", "N", "B", "M", "W", "Q", "V"],
    "col_2": ["H", "Z", "R", "W", "C", "B"],
    "col_3": ["F", "Q", "R", "J"],
    "col_4": ["Z", "S", "W", "H", "F", "N", "M", "T"],
    "col_5": ["G", "F", "W", "L", "N", "Q", "P"],
    "col_6": ["L", "P", "W"],
    "col_7": ["V", "B", "D", "R", "G", "C", "Q", "J"],
    "col_8": ["Z", "Q", "N", "B", "W"],
    "col_9": ["H", "L", "F", "C", "G", "T", "J"],
}


def main():
    with open("input.txt") as f:
        content = f.readlines()
        f.close()

    for line in content:
        instruction = (
            line.replace("move ", "")
            .replace(" from ", ",")
            .replace(" to ", ",")
            .split(",")
        )
        no_creates_to_move = int(instruction[0])
        col_to_move_from = int(instruction[1])
        col_to_move_to = int(instruction[2])

        creates_to_move = starting_crates[f"col_{col_to_move_from}"][
            -no_creates_to_move:
        ]
        print(f"moving {creates_to_move} from {col_to_move_from} to {col_to_move_to}")

        creates_ordered = creates_to_move[::-1]
        for create in creates_ordered:
            starting_crates[f"col_{col_to_move_from}"].pop()
            starting_crates[f"col_{col_to_move_to}"].append(create)

    top_row = ""
    for col in starting_crates:
        print(f"Top create in col is {starting_crates[col][-1]}")
        top_row += starting_crates[col][-1]
    print(top_row)


if __name__ == "__main__":
    main()
