import os

def import_items(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            items = f.readlines()
            for item in items:
                print(item)
