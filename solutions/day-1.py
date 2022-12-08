def main():
    with open("day-1.txt") as f:
        content = f.read()
        all_elfs_food = content.split("\n\n")
        f.close()

        elf_index = 0
        list_of_totals = []
        for elfs_food in all_elfs_food:
            elf_index += 1
            items = elfs_food.split("\n")
            int_items = [int(x) for x in items]
            list_of_totals.append(sum(int_items))

        print(f"highest calories is: {max(list_of_totals)}")


if __name__ == "__main__":
    main()
