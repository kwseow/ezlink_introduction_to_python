num_list=[]
for i in range(10):
     num_list.append(int(input("Enter number %d:"%(i+1))))

even_count = 0
odd_count = 0
for i in range(10):
    if num_list[i] % 2 :
        odd_count += 1
    else:
        even_count +=1

print("Ëven #: %d"%even_count)
print("Odd #: %d"%odd_count)