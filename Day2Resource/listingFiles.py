import os
where = "C:\\Program Files"

def listFile(where):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            print(os.path.getsize(os.path.join(root,file)), (os.path.join(root,file)))
            totalSize += os.path.getsize(os.path.join(root, file))

    return totalSize

print("Total is %d"%listFile(where))
