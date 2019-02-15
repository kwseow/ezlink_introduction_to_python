import os
where = "C:\\Program Files"
size = 25000000

def searchBySize(where, size):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            fullName = os.path.join(root,file)
            fileSize = os.path.getsize(os.path.join(root,file))
            if fileSize > size:
                print ("%d %s"%(fileSize, fullName))
                totalSize += fileSize

    return totalSize

print("Total is %d"%searchBySize(where,size))
