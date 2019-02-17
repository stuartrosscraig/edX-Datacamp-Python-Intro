# Having learned a little about GitHub and PyCharm, I'm now returning to the course!
# I don't yet know what exctly I'll put in the file - notes from the course, notes from the test or a mix

print("hello world, of course")

# ** is to-the-power-of
print(3**2)

savings = 100
growth_multiplier = 1.1
result = savings * growth_multiplier**7
print(result)

profitable = True
whatisit = type(profitable)
print(whatisit)

x: bool = True
y: int = 3


print(type(x) == type(y))
print(type(type(x) == type(y)))

z = str(y)
print(z)
print(type(y), type(z))

my_list = ["this", "is", "my", "list"]
print(my_list)

quicky_list = [1,2,3,4,5,6,7,8,9]
print(quicky_list[:4])
print(quicky_list[3:])
quicky_list = quicky_list + [11]
print(quicky_list)
quicky_list[9] = 10
print(quicky_list)
del(quicky_list[9])
print(quicky_list, "second print");print("third print")

list_1 = ["a", "b","c" ,"d" ,"e" ,"f"]
print("list 1 starts off as: ", list_1)

list_2 = list_1
list_2[0] = "z"
print("1:", list_1, "2:", list_2)

list_3 = list(list_1)
list_3[0] = "x"
print("1:", list_1, "3:", list_3)

list_4 = list_1[:]
list_4[0] = "y"
print("1:", list_1, "4:", list_4)

print("\n ---------- \n")

largest = max(quicky_list)
print(largest)
smallest = min(quicky_list)
print(smallest)

print(round(1.67, 1))
print(round(1.67))
print(round(1.9345935875345475734557734547345, 6))

# help(round)

scrambled_list = [6,2,8,5,2,6,9]
ordered_list = sorted(scrambled_list)
print(ordered_list)

# testing testing


