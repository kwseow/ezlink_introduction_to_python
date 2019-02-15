import os
where = "C:\\Program Files"
ext = ".txt"
keyword = "Test"

def searchByContent(where, ext,keyword):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            fullName = os.path.join(root,file)
            fileSize = os.path.getsize(os.path.join(root,file))
            if file.endswith(ext) and keyword in open(fullName,encoding="Latin-1").read():
                print ("%d %s"%(fileSize, fullName))
                totalSize += fileSize

    return totalSize

print("Total is %d"%searchByContent(where,ext,keyword))
