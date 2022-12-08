def main():
    with open("input.txt") as f:
        content = f.readlines()
        f.close

    total_priorities = 0
    for line in content:
        half = int(len(line.rstrip()) / 2)
        common = "".join(set(line[:half]).intersection(line[half:]))
        if common.islower():
            total_priorities += ord(common) - 96
        else:
            total_priorities += ord(common) - 38
    print(f"Total priorities is {total_priorities}")


if __name__ == "__main__":
    main()
