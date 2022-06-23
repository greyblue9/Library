#in python there are 2 confusing compare methodes that cannot be compared at first view

a = []

#those 2 are
True
a is a

#the is and the == are not 100% the same
#here you can see how they work

first = [] #first entity
second = [] #another entity
copyFirst = first #creates a copy of first

print(copyFirst is copyFirst, "copy which is the same")
print(copyFirst is second, "another entity")
print(copyFirst == second, "same value\n")
copyFirst.append("linked")
print(copyFirst, "since their both linked")
