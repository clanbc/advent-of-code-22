from collections import defaultdict


def main():
    terminal_output = []
    filepath = []
    sizes = defaultdict(int)
    total = 0
    max_size = 100000

    with open("input.txt") as f:
        content = f.readlines()
        f.close()
        for line in content:
            terminal_output.append(line.strip())

    for line in terminal_output:
        if line.startswith("$ cd"):
            directory = line.split()[-1]
            if directory == "..":
                filepath.pop()
            else:
                filepath.append(directory)

        elif line.startswith("$ ls"):
            continue

        else:
            size, _ = line.split()
            if size.isdigit():
                size = int(size)
                for i in range(len(filepath)):
                    sizes["/".join(filepath[: i + 1])] += size

    for key, value in sizes.items():
        if value <= max_size:
            total += value

    print(total)


if __name__ == "__main__":
    main()
