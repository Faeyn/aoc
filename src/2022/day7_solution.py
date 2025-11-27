import logging
from collections import namedtuple

File = namedtuple("File", ["size", "name"])


class Dir:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return self.items

    @property
    def size(self):
        return sum([item.size for item in self.items])


def create_dir_tree(input_list):
    level = 1
    current_folder = Dir(input_list[0].split(" ")[-1])

    for index, line in enumerate(input_list[1:], start=1):
        split_lines = line.split(" ")

        if level == 1:
            if split_lines[0].isnumeric():
                current_folder.add_item(File(int(split_lines[0]), split_lines[1]))

            elif "cd" in split_lines and ".." not in split_lines:
                folder = create_dir_tree(input_list[index:])
                current_folder.add_item(folder)

        if "cd" in split_lines:
            if ".." not in split_lines:
                level += 1
            else:
                level -= 1

        if level == 0:
            break
    return current_folder


def find_size(dir_tree):
    size = 0
    for item in dir_tree.items:
        if isinstance(item, Dir):
            if item.size < 100000:
                size += item.size

            size += find_size(item)
    return size


def find_smallest_folder_larger_than_reference(dir_tree, ref, all_folders):
    for item in dir_tree.items:
        if isinstance(item, Dir):
            if item.size > ref:
                all_folders.append(item.size)

            all_folders.append(find_smallest_folder_larger_than_reference(item, ref, all_folders))

    if all_folders:
        return min(all_folders)

    return float("inf")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    with open("day7_input") as f:
        lines = f.read().splitlines()

    dir_tree = create_dir_tree(lines)

    print(f"Total size: {dir_tree.size}")
    print(f"Total folder size smaller than 100000: {find_size(dir_tree)}")

    total_drive_size = 70000000
    required_free_space = 30000000
    size_to_free_up = required_free_space - (total_drive_size - dir_tree.size)
    print(f"Size to free up: {size_to_free_up}")

    print(find_smallest_folder_larger_than_reference(dir_tree, size_to_free_up, []))
