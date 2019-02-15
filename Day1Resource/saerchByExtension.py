import os
where = "C:\\Program Files"
ext = ".txt"

def searchByExtension(where, ext):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            fullName = os.path.join(root,file)
            fileSize = os.path.getsize(os.path.join(root,file))
            if file.endswith(ext):
                print ("%d %s"%(fileSize, fullName))
                totalSize += fileSize

    return totalSize

print("Total is %d"%searchByExtension(where,ext))
