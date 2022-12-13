def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False
    return True


def main():
    with open("input.txt") as f:
        content = f.read()
        f.close()

        char_total = 14
        for char in content:
            char_total += 1
            potential_marker = content[(char_total - 14) : char_total]  # noqa:E203

            marker = check_unique(potential_marker)
            if marker:
                print(f"marker is {potential_marker} & processed chars is {char_total}")
                break


if __name__ == "__main__":
    main()
