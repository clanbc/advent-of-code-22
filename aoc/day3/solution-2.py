def main():
    with open("input.txt") as f:
        content = f.readlines()
        f.close

    total_priorities = 0
    for i in range(0, len(content), 3):
        group = content[i: i + 3]
        common = (
            "".join(set(group[0]).intersection(group[1]).intersection(group[2]))
            .rstrip()
            .replace("\n", "")
        )
        if common.islower():
            total_priorities += ord(common) - 96
        else:
            total_priorities += ord(common) - 38
    print(f"Total group priorities is {total_priorities}")


if __name__ == "__main__":
    main()
