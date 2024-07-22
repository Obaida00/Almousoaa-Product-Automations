import os
import time

DIR_PATH = "f:/REPO/Almousoaa-Product-Automations/"


def find(name: str, path):
    name = name + ".txt"
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def search(name, path):
    search_res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.count(name) + file.count(".txt") > 1:
                search_res.append(file.removesuffix(".txt"))
    return search_res


def full_input(input_line):
    print(input_line)
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return "\n".join(lines)


while True:
    os.system("cls")

    name = input("enter the file name\n")
    if name == "E":
        break

    file_path = find(name, DIR_PATH)
    while file_path == None:
        print("file not found please retry")
        search_res = search(name, DIR_PATH)
        if len(search_res) == 1:
            print("found this.. " + search_res[0])
            file_path = find(search_res[0], DIR_PATH)
        else:
            print(search_res)
            name = input()
            file_path = find(name, DIR_PATH)

    print("file path is.. " + file_path + "\n")

    description = full_input("\nenter the desctiption you want")

    # currecting frequent spelling mistakes
    description = description.replace("Theraputic", "Therapeutic")

    with open(file_path, "w") as file_object:
        file_object.write(description)
