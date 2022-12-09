def main():
    with open("input.txt") as f:
        content = f.readlines()
        f.close

    total_duplication = 0
    for line in content:
        section = line.rstrip().split(",")[0].split("-")
        second_section = line.rstrip().split(",")[1].split("-")

        first_range = []
        second_range = []

        for i in range(int(section[0]), int(section[1]) + 1):
            first_range.append(i)

        for j in range(int(second_section[0]), int(second_section[1]) + 1):
            second_range.append(j)

        if first_range == second_range:
            total_duplication += 1

        else:
            any_overlap = set(first_range).intersection(second_range)
            if any_overlap:
                total_duplication += 1

    print(f"total overlap is: {total_duplication} elfs")


if __name__ == "__main__":
    main()
