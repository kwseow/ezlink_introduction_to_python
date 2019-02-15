import os
where = "C:\\"

def searchByName(name):
    totalSize = 0
    for root, dirs, files in os.walk(where):
        for file in files:
            if file == name:
                print(os.path.join(root,file))
                totalSize += os.path.getsize(os.path.join(root,file))

    return totalSize

total = searchByName("students_attendance.xlsx")
print("Total file size : %d"%total)