#for loop
 #for i in  range(10):
  #  print(i)

#user array input

size = int(input("Enter Array Size:"))
array = []
for i in range(0, size):
    element=input("Enter Array Element:")
    array.append(element)

print("ArrayList:", array)
