def list_data():
    print("id, item, price per kg")
    with open("hash.txt", "r") as file:
        print(file.read())

def query(id):
    with open("hash.txt", "r") as file:
        for line in file:
            tab = line.split(", ")
            if tab[0] == str(id).zfill(2):
                print("id, item, price")
                print(line)
                return None
        print("error, item not found")

def add_data(id, item, price):
    if not in_db():
        with open("hash.txt", "a") as file:
            file.write(f"\n{str(id).zfill(2)}, {item}, {price}\n")
    else:
        with open("hash.txt", "r") as file:
        for line in file:
            tab = line.split(", ")
            if tab[0] == str(id).zfill(2):
                tab[]
                return None

def in_db(id):
    with open("hash.txt", "r") as file:
        for line in file:
            tab = line.split(", ")
            if tab[0] == str(id).zfill(2):
                return True
    return False

def remove_data(id):
    with open("hash.txt", "r") as file:
        lines = file.readlines()

    with open("hash.txt", "w") as file:
        for line in lines:
            if line[0] != target:
                f.write(line)


add_data(88,"letus","16kr")
list_data()

