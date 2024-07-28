# making a json to contain the discription for each drug
import json
import os

DIR_PATH = "f:/REPO/Almousoaa-Product-Automations/"
output_json_path = "products_data.json"
DATA = json.load(open(output_json_path))


def find(name: str):
    if find_path(name) != None:
        return True
    return False


def find_path(name: str):
    name1 = name + ".png"
    name2 = name + ".jpg"
    for root, dirs, files in os.walk(DIR_PATH):
        if name1 in files:
            return os.path.relpath(os.path.join(root, name1))
        if name2 in files:
            return os.path.relpath(os.path.join(root, name2))

def search(name):
    search_res = []
    for root, dirs, files in os.walk(DIR_PATH):
        for file in files:
            # added the count(.txt) so it gives me just the txt files
            if file.count(name) + file.count(".png") + file.count(".jpg") > 1:
                search_res.append(file.removesuffix(".png").removesuffix(".jpg"))
    return search_res


def split(string: str):
    return string.split(sep="\\")


def get_type(path: str):
    splits_len = len(path.split(sep="\\"))
    if splits_len == 3:
        return "simple"
    elif splits_len == 4:
        return "variable"
    else:
        raise TypeError(f"looks like there is alot going on in this file... {path}")


def add_description_simple(name, desc):
    if not (name in DATA.keys()):
        DATA[name] = [None, None]
    DATA[name][0] = desc


def add_description_variation(name, desc):
    splits = split(find_path(name))
    parent = splits[len(splits) - 2]
    if not (parent in DATA.keys()):
        DATA[parent] = {}
    if not (name in DATA[parent].keys()):
        DATA[parent][name] = [None, None]
    DATA[parent][name][0] = desc


def add_description(name, desc):
    path = find_path(name)
    product_type = get_type(path)
    if product_type == "simple":
        add_description_simple(name, desc)
    elif product_type == "variable":
        add_description_variation(name, desc)


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

    exists = find(name)

    while exists == False:
        print("file not found please retry")
        search_res = search(name)
        if len(search_res) == 1:
            print("found this.. " + search_res[0])
            exists = find(search_res[0])
            name = search_res[0]
        else:
            print(search_res)
            name = input()
            exists = find(name)

    print("file path is.. " + find_path(name) + "\n")

    description = full_input("\nenter the desctiption you want")

    # currecting frequent spelling mistakes
    description = description.replace("Theraputic", "Therapeutic")

    # with open(file_path, "w") as file_object:
    #     file_object.write(description)
    add_description(name, description)

    with open(output_json_path, "w") as outfile:
        json.dump(DATA, outfile, indent=5)
    