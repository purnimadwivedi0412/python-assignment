set_1={22,56,77,94,32}
set_2={46,90,56,32,48,88}
for i in set_1:
    print(i)
union=set_1.union(set_2)
print("the union of the two set is",union)
intersection=set_1.intersection(set_2)
print("the intersection of the two set are",intersection)
diff=set_1-set_2
print("The difference of the two set is",diff)