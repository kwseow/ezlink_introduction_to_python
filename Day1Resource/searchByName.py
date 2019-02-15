import os
where = "C:\\Program Files"

def searchByName(name):
    for root, dirs, files in os.walk(where):
        for file in files:
            if file == name:
                print(os.path.join(root,file))

searchByName("readme.txt")
