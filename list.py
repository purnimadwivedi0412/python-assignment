#creating a list
num=[10,55,86,90,33,58,66]
print("the original list is",num)
print("first element of the list is",num[0])
print("last element of the list is",num[-1])
num.append(43)
print("adding elements to list",num)
num.remove(55)
print("removing element from list",num)
num.pop()
print("removing the last element of the list",num)
num.sort()
print("sorting the list",num)
num.sort(reverse=True)
print("sorting the list in reverse order",num)


