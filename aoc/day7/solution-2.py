from collections import defaultdict


def main():
    terminal_output = []
    filepath = []
    sizes = defaultdict(int)

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

    total_needed = 30000000 - (70000000 - sizes.get("/"))
    options = []
    for i in sizes.items():
        if i[1] > total_needed:
            options.append(i[1])
    options.sort()
    print(options[0])


if __name__ == "__main__":
    main()
