# Having learned a little about GitHub and PyCharm, I'm now returning to the course!
# I don't yet know what exctly I'll put in the file - notes from the course, notes from the test or a mix
import numpy as np


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

print("BREAK")

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
third = first + second
print(third)

fourth = sorted(third)
print(fourth)

fifth = sorted(third, key=None, reverse=True)
print(fifth)

sixth = sorted(third, reverse=True)
print(sixth)


string: str = "Ok, here is a rather long string I'm typing out so that I can test out string methods"
print(string)

# string.__add__('THIS HAS BEEN ADDED')
# print(string)
# print(string)

print(string.__add__(" THIS HAS BEEN ADDEDEDED"))
print(string)

print(string.upper())
print(string)

#
# NUMPY
print("NUMPY/n")
#
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height," ",np_weight)

bmi = np_weight / np_height ** 2
print(bmi)

print(bmi[2])
print(bmi>23)
over_23 = bmi[bmi>23]
print(over_23)


myarray1 = np.array([6,3,8,6,4,1,0,5,88,3,66,99,3])
print("myarray1 ", myarray1)
print("1 type ", type(myarray1))
# print()
myarray2 = myarray1[[True,True,True,True,True,True,True,True,True,True,True,True,True]]
print("myarray2 ", myarray2)
print("2 type ", type(myarray2))

# !!!! so when i had myarray2 = myarray1[True,True,True,True,True,True,True,True,True,True,True,True,True] -- i don't
# know what this is called, i'm not passing in a list of 'True's, i'm just passing in many arguments -- the output was
# [[ 6  3  8  6  4  1  0  5 88  3 66 99  3]] an array consisting of one element, which was an array containing the
# values. But, when i write myarray2 = myarray1[[True,True,True,True,True,True,True,True,True,True,True,True,True]]
# -- feeding a list into the array -- the output is [ 6  3  8  6  4  1  0  5 88  3 66 99  3] which is what i wanted in
# the first place.
# Also, when i write print(myarray1[True]) i also get [[ 6  3  8  6  4  1  0  5 88  3 66 99  3]] -- so perhaps the other
# 'True's made no difference

myarray3 = myarray1 >= 0
print("myarray3 ", myarray3)
print(type(myarray3))

myarray4 = myarray1[myarray3]
print("myarray4 ", myarray4)
print(type(myarray4))

print("hold up, yayyyy")

print(myarray1[True])
# single_True_array = np.array([True])
# print("second print: ", myarray1[single_True_array])

print("\nBREAK\n")

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d)
print(np_2d.shape)

print(np_2d[1][2])
print(np_2d[1, 2])

# to select (subset) the height and weight of the second and third family members - select both rows with ':' (to access
# the height and weight rows - then select the second and third elements of them with 1:3 (1 is incl, 3 is not))

print(np_2d[:,1:3])

# to select the weights of all family members:-

print(np_2d[1, :])

np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

print(np_mat)
print(np_mat * 2)
print("break")
print(np_mat + [10, 10])
print(np_mat + np_mat)
print('break')
print(np_mat * [2,3])
print('this is not a matrix proper\n\n')

height = np.round(np.random.normal(1.75, 0.2, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000) , 2)

print(height, "\n", type(height))

qwe = np.round(np.random.normal(1.5, 0.5, 10000), 2)
print(qwe)

np_city = np.column_stack((height, weight))
print(np_city)
# things are heating up now!!

print("break\n")

arr1 = np.array([9,8,7,6,5,4,3,2])
arr2 = np.array([45,78,32,77,94,35,17,50])

arr3 = arr1[arr1 >5]
print(arr3)

arr4 = arr1[arr1 == 9]
print(arr4)

print(len(arr1))

arr5 = np.array([[1,2,3,4],[4,3,2,1]])
print(arr5)
print(len(arr5))
print(arr5.shape)

#
# EXERCISES
#
print("break\n")



positions = ['GK', 'M', 'A', 'D', 'M', 'D', 'M', 'M', 'M', 'A', 'M', 'M', 'A', 'A', 'A', 'M', 'D', 'A', 'D', 'M', 'GK', 'D', 'D',
 'M', 'M', 'M', 'M', 'D', 'M', 'GK', 'D', 'GK', 'D', 'D', 'M', 'A', 'M', 'D', 'M', 'GK', 'M', 'GK', 'A', 'D', 'GK', 'A',
 'GK', 'GK', 'GK', 'GK', 'A', 'D', 'A', 'D', 'D', 'M', 'D', 'M', 'D', 'D', 'GK', 'GK', 'D', 'M', 'M', 'GK', 'M', 'D',
 'M', 'M', 'D', 'D', 'M', 'M', 'D', 'A', 'A', 'M', 'M', 'M', 'A', 'D', 'D', 'A', 'A', 'M', 'M', 'M', 'D', 'D', 'A', 'A',
 'D', 'M', 'M', 'M', 'D', 'M', 'M', 'D', 'M', 'A', 'M', 'M', 'GK', 'M', 'D', 'M', 'M', 'D', 'M', 'M', 'A', 'GK', 'D',
 'M', 'GK', 'M', 'M', 'M', 'M', 'D', 'D', 'M', 'D', 'M', 'D', 'M', 'M', 'A', 'M', 'GK', 'A', 'M', 'D', 'M', 'D', 'GK',
 'D', 'D', 'M', 'A', 'GK', 'M', 'D', 'A', 'D', 'A', 'A', 'M', 'D', 'M', 'A', 'GK', 'D', 'M', 'GK', 'A', 'D', 'D', 'D',
 'GK', 'GK', 'M', 'D', 'GK', 'D', 'M', 'GK', 'A', 'D', 'GK', 'GK', 'D', 'M', 'GK', 'D', 'D', 'D', 'M', 'D', 'M', 'D',
 'D', 'A', 'D', 'D', 'D', 'M', 'M', 'A', 'D', 'M', 'M', 'D', 'M', 'A', 'A', 'D', 'A', 'GK', 'M', 'A', 'A', 'D', 'D',
 'A', 'D', 'GK', 'D', 'M', 'D', 'D', 'M', 'M', 'GK', 'D', 'M', 'GK', 'GK', 'D', 'M', 'D', 'D', 'M', 'A', 'D', 'D', 'M',
 'A', 'A', 'A', 'A', 'A', 'M', 'D', 'D', 'A', 'M', 'GK', 'M', 'GK', 'A', 'A', 'GK', 'M', 'D', 'M', 'D', 'D', 'M', 'M',
 'A', 'A', 'D', 'D', 'D', 'M', 'M', 'GK', 'D', 'M', 'M', 'D', 'D', 'D', 'M', 'M', 'M', 'D', 'M', 'A', 'A', 'D', 'D',
 'M', 'GK', 'A', 'D', 'D', 'D', 'GK', 'D', 'M', 'D', 'A', 'A', 'GK', 'A', 'D', 'M', 'M', 'GK', 'A', 'A', 'M', 'D', 'A',
 'M', 'M', 'M', 'D', 'D', 'D', 'M', 'D', 'A', 'M', 'M', 'M', 'A', 'M', 'M', 'D', 'M', 'D', 'M', 'M', 'A', 'D', 'D', 'M',
 'A', 'D', 'D', 'M', 'M', 'M', 'D', 'M', 'D', 'A', 'D', 'D', 'M', 'D', 'A', 'D', 'D', 'GK', 'M', 'M', 'M', 'GK', 'M',
 'A', 'D', 'D', 'M', 'A', 'GK', 'M', 'D', 'A', 'M', 'A', 'A', 'A', 'M', 'GK', 'A', 'A', 'M', 'A', 'D', 'D', 'D', 'A',
 'GK', 'D', 'D', 'D', 'D', 'GK', 'A', 'GK', 'D', 'D', 'M', 'GK', 'D', 'D', 'D', 'A', 'D', 'D', 'GK', 'D', 'D', 'D',
 'GK', 'D', 'GK', 'A', 'M', 'A', 'M', 'A', 'D', 'D', 'D', 'GK', 'GK', 'GK', 'M', 'A', 'M', 'D', 'M', 'A', 'GK', 'M',
 'D', 'M', 'M', 'D', 'A', 'GK', 'M', 'A', 'GK', 'GK', 'M', 'A', 'A', 'M', 'GK', 'GK', 'D', 'M', 'A', 'D', 'A', 'D', 'D',
 'A', 'D', 'M', 'D', 'D', 'M', 'D', 'A', 'GK', 'D', 'D', 'GK', 'A', 'D', 'D', 'GK', 'D', 'A', 'M', 'A', 'A', 'GK', 'D',
 'A', 'D', 'A', 'D', 'GK', 'D', 'D', 'A', 'A', 'M', 'A', 'GK', 'M', 'D', 'A', 'D', 'M', 'M', 'D', 'M', 'GK', 'D', 'M',
 'A', 'A', 'M', 'M', 'M', 'GK', 'GK', 'D', 'A', 'M', 'GK', 'D', 'M', 'GK', 'M', 'M', 'GK', 'M', 'D', 'A', 'D', 'M', 'M',
 'A', 'M', 'GK', 'A', 'GK', 'A', 'M', 'GK', 'GK', 'D', 'D', 'M', 'M', 'D', 'GK', 'A', 'M', 'GK', 'A', 'GK', 'D', 'D',
 'M', 'M', 'M', 'D', 'M', 'M', 'GK', 'M', 'D', 'M', 'D', 'GK', 'M', 'A', 'GK', 'A', 'M', 'M', 'A', 'M', 'M', 'A', 'A',
 'A', 'M', 'GK', 'D', 'D', 'M', 'D', 'GK', 'D', 'M', 'M', 'M', 'A', 'D', 'A', 'D', 'A', 'M', 'M', 'D', 'M', 'M', 'D',
 'D', 'GK', 'M', 'A', 'GK', 'A', 'A', 'M', 'D', 'GK', 'D', 'M', 'M', 'GK', 'GK', 'D', 'D', 'M', 'D', 'M', 'M', 'M', 'M',
 'GK', 'M', 'D', 'M', 'D', 'GK', 'A', 'M', 'D', 'M', 'A', 'A', 'D', 'D', 'D', 'M', 'GK', 'D', 'A', 'M', 'D', 'A', 'GK',
 'M', 'D', 'M', 'D', 'A', 'A', 'M', 'A', 'D', 'D', 'M', 'A', 'M', 'M', 'A', 'D', 'GK', 'A', 'M', 'D', 'M', 'A', 'D',
 'D', 'D', 'GK', 'D', 'M', 'GK', 'M', 'M', 'GK', 'M', 'M', 'D', 'M', 'D', 'D', 'M', 'D', 'A', 'M', 'D', 'D', 'GK', 'D',
 'M', 'M', 'GK', 'GK', 'M', 'D', 'D', 'A', 'GK', 'D', 'D', 'D', 'GK', 'A', 'A', 'D', 'A', 'D', 'M', 'D', 'D', 'A', 'M',
 'GK', 'D', 'M', 'D', 'M', 'A', 'A', 'GK', 'M', 'D', 'A', 'D', 'D', 'M', 'A', 'A', 'D', 'M', 'M', 'D', 'A', 'D', 'M',
 'A', 'M', 'D', 'D', 'D', 'A', 'GK', 'D', 'D', 'M', 'M', 'A', 'M', 'A', 'D', 'M', 'A', 'A', 'GK', 'A', 'D', 'A', 'M',
 'A', 'D', 'D', 'D', 'GK', 'A', 'D', 'D', 'D', 'A', 'A', 'A', 'M', 'GK', 'GK', 'D', 'A', 'GK', 'D', 'A', 'M', 'M', 'D',
 'GK', 'M', 'A', 'M', 'D', 'M', 'M', 'M', 'D', 'A', 'GK', 'GK', 'D', 'M', 'D', 'D', 'D', 'M', 'GK', 'M', 'D', 'D', 'D',
 'A', 'A', 'GK', 'D', 'D', 'M', 'M', 'D', 'D', 'M', 'M', 'D', 'A', 'M', 'D', 'M', 'M', 'M', 'A', 'GK', 'D', 'D', 'D',
 'A', 'M', 'M', 'A', 'M', 'M', 'D', 'M', 'D', 'M', 'A', 'D', 'D', 'M', 'M', 'M', 'D', 'M', 'M', 'D', 'M', 'M', 'M', 'D',
 'D', 'A', 'D', 'A', 'A', 'D', 'D', 'M', 'M', 'A', 'A', 'GK', 'A', 'GK', 'M', 'M', 'GK', 'D', 'GK', 'A', 'GK', 'D', 'M',
 'GK', 'M', 'D', 'D', 'D', 'GK', 'M', 'GK', 'D', 'D', 'D', 'D', 'GK', 'A', 'M', 'M', 'D', 'GK', 'GK', 'GK', 'D', 'D',
 'M', 'D', 'D', 'GK', 'D', 'A', 'D', 'M', 'D', 'D', 'D', 'M', 'D', 'M', 'D', 'M', 'D', 'D', 'M', 'M', 'D', 'D', 'A',
 'M', 'D', 'M', 'A', 'M', 'D', 'A', 'M', 'D', 'GK', 'D', 'D', 'A', 'D', 'M', 'D', 'GK', 'A', 'D', 'A', 'M', 'A', 'A',
 'GK', 'D', 'M', 'D', 'A', 'D', 'A', 'M', 'M', 'D', 'D', 'D', 'A', 'GK', 'A', 'D', 'M', 'M', 'M', 'D', 'A', 'A', 'D',
 'D', 'M', 'D', 'D', 'D', 'GK', 'D', 'M', 'D', 'D', 'A', 'D', 'M', 'M', 'M', 'M', 'A', 'M', 'M', 'D', 'A', 'M', 'D',
 'M', 'M', 'M', 'M', 'M', 'GK', 'D', 'M', 'A', 'D', 'D', 'M', 'M', 'M', 'A', 'M', 'GK', 'A', 'A', 'GK', 'A', 'A', 'GK',
 'M', 'D', 'M', 'D', 'A', 'D', 'D', 'M', 'D', 'M', 'D', 'D', 'M', 'D', 'D', 'A', 'A', 'A', 'M', 'A', 'D', 'D', 'M', 'A',
 'GK', 'D', 'M', 'A', 'D', 'GK', 'D', 'M', 'M', 'A', 'D', 'M', 'D', 'D', 'D', 'GK', 'M', 'A', 'A', 'A', 'D', 'GK', 'M',
 'GK', 'M', 'GK', 'GK', 'M', 'M', 'M', 'D', 'GK', 'D', 'A', 'A', 'A', 'A', 'A', 'D', 'M', 'D', 'D', 'M', 'D', 'A', 'A',
 'M', 'D', 'GK', 'D', 'M', 'A', 'D', 'D', 'A', 'M', 'M', 'D', 'D', 'A', 'D', 'M', 'D', 'A', 'A', 'D', 'M', 'M', 'GK',
 'D', 'A', 'A', 'A', 'D', 'D', 'GK', 'M', 'M', 'A', 'M', 'M', 'GK', 'D', 'D', 'D', 'A', 'GK', 'M', 'D', 'M', 'D', 'GK',
 'M', 'A', 'M', 'D', 'A', 'M', 'GK', 'D', 'D', 'A', 'M', 'D', 'M', 'GK', 'M', 'M', 'GK', 'A', 'M', 'D', 'D', 'A', 'D',
 'A', 'D', 'D', 'M', 'M', 'D', 'M', 'GK', 'D', 'M', 'M', 'D', 'GK', 'M', 'M', 'GK', 'D', 'D', 'M', 'M', 'D', 'D', 'A',
 'M', 'A', 'M', 'A', 'D', 'D', 'D', 'A', 'D', 'GK', 'A', 'M', 'D', 'D', 'D', 'GK', 'M', 'A', 'D', 'GK', 'M', 'D', 'A',
 'GK', 'GK', 'A', 'D', 'M', 'A', 'D', 'GK', 'D', 'D', 'A', 'D', 'D', 'A', 'M', 'M', 'GK', 'D', 'D', 'M', 'GK', 'D', 'D',
 'D', 'D', 'D', 'D', 'D', 'D', 'A', 'D', 'M', 'A', 'M', 'M', 'M', 'A', 'D', 'D', 'D', 'M', 'D', 'A', 'D', 'A', 'D', 'D',
 'D', 'D', 'D', 'M', 'D', 'GK', 'D', 'M', 'A', 'M', 'GK', 'M', 'M', 'M', 'D', 'M', 'M', 'M', 'M', 'A', 'D', 'M', 'A',
 'GK', 'M', 'M', 'D', 'D', 'M', 'A', 'A', 'A', 'GK', 'M', 'D', 'M', 'M', 'D', 'GK', 'D', 'GK', 'D', 'M', 'M', 'A', 'D',
 'GK', 'A', 'D', 'A', 'A', 'D', 'A', 'M', 'A', 'M', 'M', 'M', 'D', 'M', 'M', 'D', 'D', 'M', 'D', 'D', 'D', 'A', 'M',
 'D', 'M', 'A', 'A', 'GK', 'GK', 'M', 'A', 'M', 'D', 'D', 'D', 'GK', 'A', 'GK', 'D', 'M', 'D', 'M', 'D', 'A', 'M', 'D',
 'M', 'D', 'GK', 'M', 'D', 'D', 'M', 'D', 'GK', 'A', 'D', 'D', 'GK', 'GK', 'D', 'A', 'A', 'M', 'A', 'D', 'GK', 'A', 'M',
 'GK', 'GK', 'D', 'M', 'D', 'M', 'D', 'M', 'M', 'M', 'M', 'A', 'D', 'A', 'D', 'M', 'M', 'M', 'A', 'M', 'GK', 'M', 'A',
 'M', 'M', 'A', 'D', 'GK', 'M', 'M', 'D', 'D', 'M', 'M', 'M', 'D', 'D', 'M', 'A', 'M', 'D', 'GK', 'D', 'M', 'D', 'D',
 'M', 'A', 'GK', 'A', 'GK', 'GK', 'D', 'M', 'A', 'M', 'D', 'M', 'GK', 'D', 'M', 'D', 'A', 'D', 'D', 'D', 'GK', 'D',
 'GK', 'M', 'D', 'A', 'A', 'M', 'M', 'M', 'A', 'GK', 'M', 'D', 'A', 'A', 'GK', 'A', 'M', 'M', 'D', 'D', 'D', 'D', 'A',
 'D', 'GK', 'D', 'M', 'A', 'M', 'A', 'M', 'M', 'M', 'M', 'M', 'M', 'A', 'M', 'M', 'D', 'GK', 'M', 'A', 'GK', 'A', 'GK',
 'M', 'M', 'M', 'M', 'A', 'A', 'GK', 'GK', 'A', 'M', 'M', 'A', 'M', 'D', 'A', 'M', 'M', 'M', 'GK', 'M', 'M', 'A', 'D',
 'GK', 'D', 'GK', 'D', 'D', 'D', 'A', 'M', 'M', 'M', 'D', 'A', 'D', 'M', 'M', 'D', 'D', 'A', 'A', 'A', 'A', 'M', 'A',
 'GK', 'M', 'D', 'M', 'M', 'A', 'D', 'M', 'M', 'GK', 'M', 'A', 'M', 'D', 'M', 'A', 'M', 'M', 'GK', 'D', 'D', 'GK', 'D',
 'M', 'D', 'D', 'M', 'D', 'D', 'D', 'M', 'M', 'M', 'A', 'M', 'A', 'M', 'D', 'M', 'GK', 'D', 'A', 'M', 'A', 'M', 'GK',
 'A', 'D', 'D', 'D', 'GK', 'D', 'A', 'A', 'M', 'M', 'D', 'M', 'A', 'M', 'M', 'M', 'M', 'D', 'A', 'D', 'A', 'M', 'A',
 'M', 'M', 'M', 'M', 'M', 'GK', 'A', 'M', 'D', 'M', 'D', 'A', 'GK', 'D', 'M', 'A', 'A', 'A', 'A', 'M', 'D', 'GK', 'A',
 'M', 'A', 'GK', 'D', 'D', 'D', 'D', 'A', 'D', 'M', 'D', 'D', 'A', 'M', 'GK', 'D', 'M', 'M', 'GK', 'A', 'M', 'D', 'M',
 'M', 'M', 'A', 'A', 'A', 'D', 'M', 'A', 'D', 'M', 'A', 'D', 'A', 'GK', 'A', 'A', 'GK', 'GK', 'M', 'M', 'D', 'M', 'M',
 'D', 'M', 'D', 'GK', 'D', 'M', 'A', 'D', 'M', 'GK', 'D', 'M', 'GK', 'D', 'GK', 'A', 'D', 'M', 'A', 'A', 'M', 'M', 'D',
 'D', 'M', 'A', 'D', 'M', 'A', 'D', 'D', 'A', 'M', 'M', 'M', 'M', 'A', 'M', 'D', 'M', 'D', 'GK', 'GK', 'A', 'A', 'A',
 'A', 'D', 'D', 'A', 'D', 'M', 'M', 'A', 'A', 'D', 'D', 'M', 'GK', 'A', 'D', 'A', 'GK', 'GK', 'A', 'D', 'M', 'A', 'D',
 'M', 'M', 'A', 'D', 'M', 'M', 'D', 'D', 'M', 'D', 'GK', 'M', 'A', 'A', 'D', 'A', 'D', 'D', 'GK', 'D', 'D', 'GK', 'D',
 'A', 'D', 'D', 'D', 'M', 'D', 'M', 'M', 'GK', 'A', 'D', 'GK', 'D', 'M', 'A', 'M', 'M', 'GK', 'M', 'GK', 'D', 'D', 'D',
 'M', 'A', 'D', 'D', 'D', 'GK', 'M', 'A', 'D', 'M', 'GK', 'M', 'D', 'M', 'M', 'A', 'A', 'M', 'D', 'M', 'A', 'M', 'A',
 'M', 'D', 'M', 'D', 'GK', 'M', 'A', 'D', 'A', 'A', 'D', 'M', 'D', 'D', 'M', 'D', 'D', 'M', 'M', 'M', 'M', 'M', 'A',
 'D', 'A', 'D', 'M', 'A', 'M', 'M', 'M', 'D', 'M', 'D', 'M', 'M', 'M', 'A', 'D', 'M', 'M', 'M', 'M', 'D', 'D', 'GK',
 'D', 'M', 'D', 'M', 'A', 'D', 'GK', 'D', 'A', 'A', 'A', 'M', 'M', 'M', 'M', 'M', 'GK', 'D', 'D', 'A', 'M', 'D', 'D',
 'M', 'A', 'A', 'D', 'GK', 'GK', 'M', 'D', 'A', 'M', 'GK', 'GK', 'GK', 'D', 'M', 'M', 'A', 'D', 'D', 'M', 'M', 'D', 'A',
 'M', 'D', 'M', 'A', 'GK', 'GK', 'D', 'GK', 'M', 'M', 'M', 'M', 'D', 'M', 'D', 'A', 'D', 'M', 'D', 'D', 'GK', 'A', 'A',
 'M', 'D', 'D', 'A', 'M', 'M', 'D', 'A', 'M', 'M', 'M', 'D', 'A', 'M', 'GK', 'D', 'D', 'A', 'A', 'M', 'A', 'M', 'D',
 'D', 'GK', 'M', 'D', 'M', 'M', 'D', 'D', 'D', 'D', 'D', 'A', 'M', 'M', 'M', 'D', 'M', 'GK', 'A', 'D', 'D', 'GK', 'M',
 'M', 'A', 'A', 'M', 'M', 'A', 'D', 'A', 'D', 'M', 'GK', 'M', 'D', 'D', 'M', 'M', 'A', 'M', 'M', 'GK', 'A', 'A', 'GK',
 'D', 'D', 'M', 'D', 'D', 'D', 'A', 'D', 'GK', 'M', 'A', 'D', 'D', 'GK', 'GK', 'GK', 'D', 'M', 'GK', 'M', 'D', 'M', 'M',
 'A', 'GK', 'M', 'D', 'D', 'M', 'GK', 'A', 'GK', 'A', 'A', 'M', 'D', 'A', 'M', 'A', 'M', 'D', 'GK', 'D', 'M', 'A', 'A',
 'M', 'M', 'D', 'GK', 'D', 'D', 'A', 'A', 'A', 'GK', 'D', 'M', 'D', 'GK', 'D', 'D', 'D', 'GK', 'M', 'M', 'D', 'D', 'D',
 'A', 'A', 'D', 'A', 'A', 'D', 'D', 'M', 'GK', 'M', 'M', 'D', 'M', 'A', 'M', 'A', 'GK', 'D', 'D', 'M', 'M', 'A', 'GK',
 'D', 'GK', 'D', 'D', 'M', 'A', 'M', 'M', 'M', 'A', 'A', 'D', 'M', 'M', 'M', 'M', 'A', 'D', 'D', 'M', 'M', 'M', 'GK',
 'M', 'A', 'M', 'A', 'D', 'M', 'D', 'D', 'A', 'D', 'M', 'M', 'D', 'M', 'A', 'D', 'M', 'D', 'M', 'M', 'M', 'GK', 'A',
 'D', 'M', 'D', 'D', 'M', 'D', 'A', 'GK', 'D', 'D', 'A', 'D', 'D', 'GK', 'M', 'D', 'D', 'M', 'M', 'M', 'M', 'M', 'D',
 'A', 'A', 'A', 'A', 'M', 'M', 'A', 'A', 'A', 'D', 'M', 'M', 'A', 'A', 'A', 'D', 'M', 'M', 'M', 'GK', 'M', 'M', 'M',
 'M', 'A', 'M', 'D', 'D', 'D', 'D', 'A', 'M', 'M', 'M', 'A', 'M', 'D', 'M', 'D', 'M', 'M', 'M', 'M', 'M', 'D', 'A', 'M',
 'M', 'M', 'D', 'M', 'A', 'D', 'D', 'D', 'D', 'A', 'D', 'A', 'A', 'D', 'A', 'GK', 'M', 'M', 'A', 'D', 'D', 'M', 'A',
 'M', 'A', 'A', 'GK', 'A', 'D', 'D', 'M', 'A', 'M', 'D', 'A', 'GK', 'A', 'A', 'D', 'D', 'M', 'A', 'GK', 'A', 'D', 'M',
 'M', 'M', 'M', 'M', 'D', 'D', 'M', 'GK', 'D', 'M', 'M', 'A', 'D', 'M', 'D', 'GK', 'A', 'D', 'D', 'A', 'M', 'D', 'D',
 'M', 'M', 'A', 'M', 'D', 'M', 'D', 'D', 'D', 'M', 'M', 'M', 'D', 'GK', 'D', 'D', 'GK', 'D', 'D', 'A', 'A', 'D', 'A',
 'A', 'D', 'M', 'D', 'D', 'D', 'A', 'A', 'GK', 'M', 'A', 'D', 'M', 'M', 'M', 'D', 'M', 'GK', 'A', 'GK', 'M', 'M', 'GK',
 'D', 'D', 'M', 'GK', 'M', 'M', 'M', 'M', 'GK', 'D', 'GK', 'M', 'M', 'M', 'D', 'D', 'D', 'M', 'A', 'M', 'M', 'A', 'M',
 'M', 'A', 'M', 'D', 'A', 'D', 'A', 'D', 'D', 'M', 'A', 'GK', 'A', 'M', 'D', 'M', 'D', 'A', 'M', 'D', 'M', 'M', 'M',
 'M', 'GK', 'M', 'M', 'A', 'A', 'GK', 'M', 'D', 'M', 'A', 'M', 'M', 'D', 'D', 'M', 'GK', 'A', 'D', 'A', 'M', 'A', 'D',
 'D', 'M', 'A', 'M', 'M', 'D', 'M', 'D', 'D', 'D', 'M', 'A', 'M', 'D', 'A', 'D', 'A', 'D', 'GK', 'M', 'A', 'D', 'M',
 'M', 'M', 'GK', 'D', 'M', 'A', 'A', 'A', 'D', 'D', 'D', 'D', 'M', 'D', 'M', 'A', 'A', 'GK', 'D', 'D', 'GK', 'D', 'A',
 'D', 'M', 'A', 'D', 'A', 'A', 'D', 'GK', 'A', 'D', 'D', 'A', 'A', 'M', 'A', 'M', 'A', 'M', 'D', 'D', 'D', 'M', 'A',
 'GK', 'M', 'M', 'A', 'D', 'D', 'M', 'A', 'A', 'D', 'D', 'M', 'D', 'D', 'A', 'M', 'D', 'M', 'A', 'D', 'D', 'M', 'A',
 'D', 'M', 'A', 'D', 'D', 'GK', 'D', 'M', 'D', 'GK', 'A', 'M', 'D', 'D', 'M', 'A', 'M', 'M', 'M', 'M', 'M', 'M', 'A',
 'M', 'M', 'GK', 'M', 'M', 'M', 'A', 'A', 'A', 'D', 'M', 'GK', 'GK', 'A', 'M', 'D', 'GK', 'M', 'A', 'M', 'D', 'D', 'M',
 'D', 'A', 'D', 'D', 'GK', 'D', 'M', 'A', 'A', 'D', 'A', 'M', 'D', 'A', 'GK', 'A', 'D', 'A', 'D', 'GK', 'GK', 'GK', 'M',
 'D', 'D', 'M', 'GK', 'D', 'A', 'D', 'GK', 'D', 'M', 'M', 'D', 'M', 'M', 'M', 'A', 'D', 'M', 'GK', 'D', 'D', 'A', 'GK',
 'M', 'M', 'M', 'D', 'GK', 'D', 'D', 'M', 'D', 'D', 'GK', 'A', 'GK', 'D', 'A', 'D', 'M', 'D', 'A', 'A', 'M', 'D', 'D',
 'D', 'M', 'GK', 'M', 'D', 'D', 'GK', 'D', 'M', 'D', 'A', 'D', 'A', 'M', 'M', 'M', 'D', 'A', 'GK', 'M', 'M', 'D', 'D',
 'A', 'A', 'GK', 'GK', 'D', 'A', 'M', 'GK', 'M', 'M', 'A', 'D', 'M', 'A', 'A', 'GK', 'M', 'A', 'A', 'D', 'M', 'M', 'D',
 'A', 'D', 'A', 'A', 'D', 'M', 'D', 'A', 'D', 'D', 'M', 'M', 'M', 'M', 'M', 'A', 'D', 'D', 'M', 'D', 'D', 'GK', 'D',
 'M', 'D', 'M', 'GK', 'D', 'M', 'A', 'M', 'M', 'M', 'M', 'D', 'D', 'D', 'A', 'GK', 'A', 'GK', 'M', 'D', 'GK', 'GK', 'A',
 'M', 'A', 'D', 'D', 'D', 'M', 'M', 'D', 'D', 'A', 'M', 'A', 'M', 'M', 'GK', 'M', 'D', 'A', 'M', 'A', 'M', 'D', 'D',
 'D', 'D', 'D', 'D', 'A', 'D', 'GK', 'M', 'M', 'GK', 'GK', 'D', 'D', 'M', 'A', 'D', 'D', 'D', 'GK', 'GK', 'M', 'M', 'M',
 'GK', 'D', 'M', 'M', 'M', 'M', 'D', 'D', 'A', 'D', 'A', 'A', 'GK', 'M', 'D', 'D', 'M', 'M', 'M', 'D', 'A', 'M', 'GK',
 'M', 'GK', 'GK', 'D', 'M', 'GK', 'D', 'M', 'M', 'D', 'M', 'D', 'A', 'D', 'D', 'D', 'A', 'M', 'A', 'D', 'D', 'A', 'D',
 'D', 'M', 'M', 'D', 'A', 'D', 'A', 'D', 'A', 'A', 'M', 'A', 'D', 'M', 'M', 'M', 'GK', 'GK', 'M', 'M', 'D', 'A', 'D',
 'D', 'M', 'A', 'A', 'M', 'D', 'D', 'D', 'D', 'GK', 'M', 'M', 'D', 'D', 'D', 'D', 'M', 'D', 'D', 'D', 'M', 'D', 'M',
 'D', 'A', 'D', 'D', 'A', 'A', 'D', 'D', 'M', 'D', 'GK', 'D', 'M', 'A', 'M', 'GK', 'D', 'D', 'M', 'A', 'M', 'A', 'M',
 'A', 'A', 'A', 'M', 'D', 'M', 'D', 'M', 'D', 'A', 'M', 'D', 'M', 'A', 'M', 'M', 'D', 'A', 'A', 'A', 'D', 'A', 'M', 'D',
 'M', 'A', 'M', 'D', 'A', 'M', 'A', 'GK', 'D', 'M', 'D', 'M', 'D', 'A', 'M', 'A', 'D', 'M', 'M', 'D', 'GK', 'A', 'M',
 'M', 'M', 'M', 'D', 'D', 'M', 'A', 'M', 'M', 'D', 'M', 'M', 'D', 'GK', 'D', 'D', 'M', 'M', 'D', 'M', 'A', 'D', 'GK',
 'A', 'M', 'D', 'A', 'A', 'A', 'A', 'GK', 'M', 'D', 'M', 'M', 'D', 'A', 'M', 'GK', 'D', 'M', 'A', 'M', 'GK', 'M', 'A',
 'GK', 'A', 'D', 'A', 'M', 'M', 'D', 'M', 'D', 'M', 'D', 'A', 'M', 'A', 'D', 'D', 'M', 'GK', 'D', 'D', 'M', 'M', 'A',
 'M', 'D', 'A', 'A', 'D', 'GK', 'GK', 'D', 'A', 'M', 'D', 'D', 'M', 'GK', 'D', 'M', 'M', 'D', 'M', 'GK', 'D', 'A', 'M',
 'GK', 'M', 'M', 'M', 'A', 'M', 'M', 'GK', 'M', 'D', 'D', 'D', 'D', 'D', 'M', 'D', 'M', 'D', 'A', 'GK', 'M', 'D', 'D',
 'A', 'GK', 'D', 'M', 'A', 'M', 'D', 'M', 'D', 'GK', 'M', 'GK', 'A', 'D', 'D', 'A', 'D', 'A', 'M', 'M', 'M', 'D', 'D',
 'D', 'M', 'D', 'D', 'M', 'D', 'D', 'M', 'M', 'GK', 'M', 'GK', 'M', 'M', 'D', 'D', 'GK', 'D', 'M', 'D', 'D', 'A', 'M',
 'GK', 'D', 'M', 'D', 'D', 'D', 'M', 'M', 'M', 'D', 'A', 'A', 'A', 'A', 'GK', 'D', 'GK', 'A', 'A', 'D', 'M', 'M', 'A',
 'A', 'D', 'M', 'M', 'GK', 'M', 'D', 'D', 'M', 'D', 'GK', 'D', 'GK', 'M', 'D', 'D', 'GK', 'D', 'A', 'M', 'D', 'GK', 'D',
 'A', 'A', 'A', 'D', 'GK', 'D', 'D', 'GK', 'GK', 'A', 'A', 'M', 'D', 'D', 'D', 'GK', 'A', 'M', 'M', 'M', 'A', 'A', 'M',
 'D', 'D', 'D', 'D', 'M', 'D', 'A', 'A', 'D', 'D', 'D', 'D', 'M', 'M', 'M', 'D', 'D', 'M', 'A', 'M', 'D', 'D', 'A',
 'GK', 'D', 'D', 'GK', 'M', 'D', 'M', 'A', 'A', 'A', 'A', 'GK', 'A', 'D', 'D', 'M', 'M', 'A', 'A', 'A', 'D', 'M', 'A',
 'A', 'A', 'D', 'GK', 'D', 'M', 'D', 'M', 'M', 'M', 'A', 'A', 'A', 'D', 'A', 'A', 'D', 'A', 'A', 'M', 'D', 'M', 'A',
 'A', 'M', 'A', 'M', 'M', 'D', 'D', 'M', 'D', 'GK', 'D', 'A', 'D', 'M', 'D', 'A', 'A', 'D', 'M', 'A', 'D', 'M', 'D',
 'D', 'M', 'D', 'A', 'D', 'M', 'D', 'M', 'GK', 'A', 'D', 'GK', 'A', 'D', 'A', 'A', 'D', 'M', 'M', 'M', 'D', 'M', 'A',
 'D', 'M', 'D', 'D', 'M', 'D', 'M', 'D', 'D', 'M', 'D', 'M', 'D', 'M', 'GK', 'D', 'M', 'M', 'M', 'M', 'M', 'D', 'M',
 'GK', 'M', 'M', 'D', 'M', 'D', 'M', 'D', 'D', 'GK', 'A', 'D', 'A', 'A', 'M', 'D', 'M', 'M', 'GK', 'D', 'D', 'GK', 'A',
 'GK', 'D', 'A', 'A', 'A', 'D', 'GK', 'A', 'M', 'A', 'A', 'GK', 'M', 'A', 'D', 'GK', 'D', 'M', 'A', 'M', 'A', 'A', 'M',
 'D', 'M', 'GK', 'D', 'D', 'M', 'A', 'D', 'M', 'D', 'M', 'M', 'D', 'D', 'A', 'A', 'M', 'D', 'A', 'M', 'D', 'A', 'D',
 'D', 'M', 'D', 'M', 'M', 'A', 'M', 'A', 'D', 'M', 'D', 'A', 'D', 'D', 'A', 'A', 'GK', 'D', 'M', 'A', 'A', 'A', 'M',
 'D', 'D', 'GK', 'M', 'A', 'D', 'GK', 'M', 'D', 'A', 'M', 'M', 'A', 'D', 'M', 'D', 'A', 'M', 'M', 'D', 'D', 'M', 'M',
 'GK', 'D', 'A', 'M', 'A', 'D', 'M', 'M', 'M', 'M', 'M', 'D', 'M', 'D', 'A', 'A', 'D', 'D', 'A', 'GK', 'D', 'M', 'GK',
 'M', 'GK', 'D', 'D', 'A', 'A', 'D', 'D', 'A', 'M', 'D', 'M', 'M', 'M', 'D', 'M', 'D', 'A', 'M', 'M', 'A', 'A', 'M',
 'M', 'D', 'D', 'D', 'D', 'D', 'A', 'M', 'M', 'M', 'D', 'GK', 'GK', 'A', 'D', 'M', 'M', 'M', 'M', 'M', 'A', 'D', 'M',
 'D', 'D', 'A', 'D', 'D', 'M', 'D', 'A', 'D', 'D', 'D', 'A', 'M', 'M', 'D', 'A', 'A', 'D', 'A', 'A', 'D', 'D', 'D', 'M',
 'M', 'M', 'D', 'A', 'A', 'A', 'M', 'M', 'D', 'GK', 'M', 'A', 'A', 'D', 'D', 'D', 'A', 'A', 'A', 'M', 'D', 'A', 'GK',
 'A', 'M', 'A', 'D', 'A', 'D', 'D', 'M', 'A', 'M', 'M', 'M', 'M', 'M', 'A', 'M', 'A', 'A', 'D', 'GK', 'M', 'GK', 'D',
 'A', 'M', 'GK', 'D', 'M', 'D', 'M', 'A', 'A', 'D', 'D', 'M', 'D', 'M', 'M', 'D', 'M', 'GK', 'A', 'D', 'D', 'D', 'A',
 'D', 'M', 'D', 'D', 'A', 'M', 'D', 'A', 'D', 'M', 'D', 'A', 'GK', 'D', 'D', 'A', 'GK', 'M', 'M', 'GK', 'A', 'D', 'M',
 'M', 'A', 'D', 'M', 'A', 'M', 'D', 'M', 'M', 'A', 'M', 'D', 'D', 'M', 'D', 'A', 'D', 'D', 'D', 'D', 'M', 'M', 'D', 'M',
 'A', 'M', 'D', 'M', 'D', 'A', 'A', 'GK', 'M', 'D', 'D', 'M', 'D', 'M', 'A', 'A', 'D', 'GK', 'A', 'D', 'D', 'A', 'M',
 'M', 'M', 'A', 'M', 'M', 'M', 'M', 'M', 'A', 'D', 'D', 'D', 'D', 'D', 'M', 'D', 'D', 'M', 'D', 'M', 'D', 'D', 'M', 'D',
 'M', 'M', 'M', 'GK', 'D', 'GK', 'GK', 'GK', 'D', 'M', 'A', 'D', 'A', 'D', 'M', 'M', 'A', 'M', 'M', 'D', 'D', 'A', 'GK',
 'GK', 'M', 'D', 'M', 'GK', 'M', 'D', 'D', 'D', 'D', 'D', 'GK', 'M', 'D', 'M', 'A', 'D', 'M', 'A', 'M', 'GK', 'M', 'M',
 'D', 'D', 'D', 'M', 'M', 'D', 'M', 'GK', 'M', 'D', 'GK', 'A', 'M', 'A', 'D', 'D', 'D', 'A', 'A', 'GK', 'A', 'M', 'M',
 'D', 'M', 'M', 'D', 'A', 'GK', 'A', 'D', 'GK', 'M', 'A', 'M', 'GK', 'D', 'GK', 'M', 'A', 'M', 'M', 'A', 'D', 'M', 'D',
 'D', 'D', 'D', 'M', 'M', 'M', 'A', 'A', 'M', 'D', 'A', 'M', 'A', 'M', 'M', 'A', 'M', 'A', 'A', 'A', 'M', 'M', 'GK',
 'D', 'D', 'D', 'D', 'D', 'M', 'GK', 'A', 'D', 'D', 'D', 'M', 'GK', 'M', 'D', 'GK', 'A', 'D', 'D', 'M', 'M', 'M', 'M',
 'M', 'M', 'A', 'D', 'M', 'A', 'A', 'M', 'M', 'A', 'A', 'M', 'A', 'D', 'A', 'D', 'D', 'M', 'M', 'M', 'D', 'D', 'M',
 'GK', 'A', 'A', 'M', 'A', 'D', 'A', 'D', 'D', 'A', 'M', 'A', 'A', 'M', 'M', 'D', 'M', 'A', 'A', 'D', 'D', 'D', 'A',
 'D', 'M', 'A', 'D', 'D', 'D', 'M', 'M', 'D', 'D', 'D', 'GK', 'M', 'M', 'A', 'A', 'A', 'D', 'M', 'M', 'GK', 'GK', 'D',
 'D', 'A', 'D', 'D', 'M', 'D', 'A', 'D', 'A', 'M', 'M', 'D', 'M', 'GK', 'A', 'M', 'D', 'M', 'M', 'M', 'GK', 'D', 'A',
 'D', 'A', 'D', 'M', 'D', 'D', 'A', 'A', 'M', 'D', 'M', 'M', 'GK', 'M', 'D', 'M', 'D', 'M', 'GK', 'A', 'M', 'D', 'A',
 'D', 'M', 'D', 'M', 'A', 'M', 'M', 'M', 'D', 'GK', 'GK', 'D', 'GK', 'D', 'D', 'A', 'D', 'A', 'M', 'D', 'A', 'M', 'A',
 'A', 'GK', 'M', 'A', 'GK', 'M', 'M', 'A', 'M', 'A', 'GK', 'A', 'M', 'A', 'M', 'D', 'A', 'M', 'GK', 'M', 'M', 'A', 'GK',
 'A', 'D', 'M', 'M', 'A', 'M', 'D', 'D', 'A', 'D', 'D', 'A', 'GK', 'M', 'M', 'GK', 'M', 'M', 'A', 'A', 'D', 'A', 'M',
 'A', 'M', 'M', 'M', 'M', 'M', 'A', 'M', 'M', 'A', 'D', 'M', 'M', 'D', 'A', 'D', 'M', 'GK', 'D', 'M', 'A', 'D', 'M',
 'D', 'A', 'M', 'D', 'A', 'M', 'D', 'M', 'D', 'A', 'A', 'A', 'M', 'A', 'D', 'M', 'M', 'D', 'M', 'A', 'D', 'M', 'A', 'A',
 'D', 'D', 'D', 'M', 'D', 'M', 'M', 'A', 'M', 'M', 'M', 'A', 'A', 'M', 'M', 'GK', 'M', 'M', 'M', 'M', 'GK', 'D', 'D',
 'M', 'A', 'D', 'GK', 'D', 'A', 'GK', 'D', 'A', 'D', 'M', 'M', 'A', 'M', 'A', 'M', 'D', 'A', 'M', 'D', 'M', 'A', 'M',
 'D', 'M', 'D', 'D', 'M', 'D', 'D', 'D', 'A', 'D', 'M', 'A', 'A', 'M', 'A', 'M', 'A', 'M', 'D', 'A', 'D', 'A', 'M', 'M',
 'M', 'M', 'A', 'M', 'D', 'M', 'D', 'A', 'GK', 'D', 'GK', 'M', 'D', 'A', 'D', 'GK', 'GK', 'M', 'M', 'A', 'GK', 'M', 'D',
 'M', 'A', 'A', 'D', 'D', 'A', 'D', 'D', 'M', 'M', 'D', 'M', 'A', 'M', 'D', 'GK', 'A', 'M', 'GK', 'A', 'D', 'M', 'A',
 'M', 'M', 'D', 'A', 'A', 'D', 'D', 'M', 'M', 'D', 'M', 'M', 'A', 'M', 'A', 'D', 'M', 'A', 'M', 'M', 'D', 'M', 'A', 'A',
 'M', 'GK', 'M', 'M', 'D', 'M', 'D', 'D', 'M', 'M', 'D', 'M', 'M', 'M', 'A', 'M', 'A', 'A', 'D', 'M', 'GK', 'A', 'M',
 'GK', 'A', 'A', 'A', 'A', 'A', 'A', 'D', 'M', 'D', 'D', 'M', 'GK', 'D', 'A', 'M', 'D', 'M', 'A', 'M', 'D', 'D', 'A',
 'A', 'A', 'D', 'M', 'M', 'M', 'M', 'M', 'GK', 'M', 'A', 'A', 'D', 'D', 'D', 'M', 'A', 'M', 'D', 'A', 'D', 'D', 'A',
 'M', 'GK', 'M', 'GK', 'D', 'A', 'GK', 'A', 'A', 'D', 'M', 'D', 'A', 'GK', 'M', 'M', 'D', 'D', 'D', 'GK', 'GK', 'A',
 'D', 'D', 'M', 'A', 'D', 'D', 'D', 'M', 'D', 'GK', 'M', 'M', 'M', 'M', 'GK', 'D', 'GK', 'M', 'A', 'A', 'A', 'M', 'M',
 'M', 'M', 'A', 'A', 'A', 'GK', 'D', 'D', 'D', 'M', 'M', 'D', 'GK', 'D', 'A', 'A', 'M', 'M', 'D', 'M', 'M', 'M', 'A',
 'D', 'A', 'D', 'D', 'M', 'D', 'M', 'M', 'D', 'A', 'D', 'GK', 'A', 'GK', 'M', 'M', 'D', 'A', 'GK', 'A', 'A', 'M', 'M',
 'M', 'GK', 'A', 'M', 'M', 'GK', 'A', 'A', 'D', 'A', 'A', 'M', 'A', 'D', 'A', 'A', 'M', 'A', 'A', 'M', 'M', 'A', 'GK',
 'M', 'M', 'D', 'M', 'M', 'M', 'A', 'M', 'D', 'M', 'M', 'A', 'M', 'M', 'D', 'M', 'GK', 'GK', 'M', 'M', 'A', 'M', 'D',
 'D', 'D', 'M', 'M', 'M', 'A', 'M', 'D', 'M', 'A', 'A', 'A', 'D', 'GK', 'M', 'M', 'M', 'A', 'GK', 'D', 'M', 'A', 'D',
 'M', 'M', 'A', 'GK', 'A', 'D', 'A', 'M', 'D', 'A', 'M', 'A', 'D', 'A', 'D', 'A', 'D', 'A', 'D', 'A', 'D', 'M', 'A',
 'M', 'M', 'A', 'D', 'M', 'D', 'M', 'D', 'GK', 'A', 'M', 'D', 'A', 'A', 'GK', 'A', 'A', 'A', 'D', 'M', 'D', 'A', 'D',
 'A', 'M', 'D', 'M', 'M', 'D', 'M', 'A', 'M', 'D', 'A', 'D', 'A', 'M', 'M', 'M', 'A', 'A', 'M', 'A', 'M', 'D', 'A', 'A',
 'M', 'M', 'D', 'D', 'D', 'M', 'A', 'A', 'M', 'D', 'D', 'A', 'D', 'D', 'A', 'D', 'D', 'D', 'A', 'D', 'M', 'D', 'GK',
 'GK', 'D', 'M', 'D', 'D', 'GK', 'D', 'D', 'GK', 'D', 'M', 'D', 'M', 'M', 'A', 'GK', 'A', 'M', 'A', 'M', 'A', 'A', 'M',
 'D', 'D', 'A', 'D', 'M', 'A', 'M', 'M', 'M', 'M', 'D', 'M', 'A', 'A', 'D', 'D', 'GK', 'D', 'M', 'M', 'D', 'M', 'D',
 'D', 'M', 'D', 'M', 'M', 'M', 'D', 'M', 'M', 'A', 'M', 'M', 'D', 'A', 'A', 'A', 'M', 'D', 'M', 'M', 'M', 'D', 'A', 'D',
 'M', 'M', 'D', 'GK', 'D', 'D', 'M', 'D', 'M', 'M', 'D', 'A', 'M', 'D', 'M', 'D', 'D', 'A', 'A', 'GK', 'M', 'A', 'A',
 'D', 'A', 'M', 'D', 'GK', 'A', 'M', 'M', 'D', 'D', 'A', 'A', 'D', 'D', 'A', 'D', 'D', 'D', 'D', 'A', 'M', 'M', 'M',
 'D', 'GK', 'M', 'A', 'M', 'GK', 'M', 'GK', 'D', 'A', 'D', 'A', 'M', 'A', 'D', 'D', 'M', 'M', 'D', 'GK', 'M', 'M', 'D',
 'D', 'D', 'D', 'M', 'M', 'D', 'GK', 'D', 'A', 'M', 'GK', 'D', 'D', 'GK', 'A', 'M', 'A', 'D', 'D', 'D', 'M', 'GK', 'M',
 'D', 'A', 'D', 'M', 'A', 'A', 'M', 'M', 'D', 'M', 'M', 'M', 'M', 'M', 'D', 'A', 'M', 'D', 'A', 'M', 'D', 'D', 'GK',
 'D', 'D', 'A', 'D', 'A', 'GK', 'D', 'A', 'A', 'M', 'A', 'M', 'M', 'M', 'D', 'A', 'M', 'M', 'A', 'M', 'M', 'M', 'D',
 'M', 'M', 'M', 'A', 'A', 'GK', 'A', 'A', 'D', 'A', 'GK', 'D', 'A', 'D', 'M', 'D', 'GK', 'A', 'M', 'D', 'A', 'D', 'M',
 'M', 'M', 'M', 'A', 'M', 'D', 'GK', 'M', 'M', 'D', 'A', 'M', 'A', 'A', 'D', 'A', 'D', 'D', 'D', 'M', 'D', 'A', 'A',
 'GK', 'GK', 'D', 'D', 'M', 'D', 'M', 'D', 'M', 'M', 'D', 'M', 'D', 'D', 'M', 'D', 'D', 'A', 'D', 'A', 'M', 'M', 'GK',
 'A', 'A', 'M', 'D', 'GK', 'D', 'D', 'A', 'D', 'M', 'M', 'M', 'D', 'M', 'M', 'A', 'D', 'D', 'A', 'D', 'M', 'A', 'A',
 'A', 'M', 'A', 'M', 'M', 'GK', 'GK', 'D', 'D', 'M', 'A', 'D', 'D', 'GK', 'M', 'GK', 'D', 'D', 'A', 'M', 'M', 'D', 'M',
 'M', 'M', 'M', 'D', 'A', 'M', 'M', 'GK', 'M', 'D', 'A', 'D', 'D', 'D', 'D', 'D', 'A', 'M', 'M', 'D', 'A', 'GK', 'D',
 'M', 'D', 'D', 'D', 'D', 'M', 'M', 'D', 'GK', 'M', 'D', 'M', 'M', 'A', 'A', 'M', 'M', 'GK', 'A', 'D', 'M', 'M', 'M',
 'A', 'M', 'A', 'A', 'D', 'M', 'D', 'D', 'M', 'D', 'D', 'D', 'M', 'GK', 'D', 'D', 'GK', 'A', 'A', 'D', 'A', 'D', 'M',
 'D', 'A', 'D', 'D', 'A', 'A', 'M', 'A', 'M', 'M', 'M', 'A', 'A', 'M', 'A', 'A', 'D', 'M', 'M', 'D', 'A', 'A', 'M', 'M',
 'M', 'D', 'A', 'M', 'D', 'A', 'D', 'D', 'A', 'D', 'A', 'D', 'A', 'M', 'D', 'D', 'D', 'GK', 'M', 'M', 'M', 'A', 'M',
 'M', 'D', 'M', 'D', 'D', 'A', 'D', 'M', 'M', 'M', 'M', 'M', 'GK', 'GK', 'A', 'A', 'GK', 'GK', 'D', 'D', 'D', 'A', 'A',
 'M', 'GK', 'A', 'M', 'A', 'M', 'A', 'M', 'A', 'A', 'M', 'A', 'D', 'M', 'M', 'M', 'M', 'A', 'GK', 'D', 'M', 'M', 'D',
 'A', 'A', 'A', 'M', 'D', 'D', 'D', 'M', 'M', 'M', 'D', 'M', 'A', 'D', 'M', 'M', 'M', 'M', 'M', 'D', 'A', 'GK', 'M',
 'M', 'M', 'D', 'A', 'D', 'GK', 'M', 'D', 'A', 'D', 'D', 'A', 'A', 'D', 'M', 'M', 'D', 'D', 'M', 'D', 'A', 'M', 'M',
 'A', 'M', 'D', 'D', 'M', 'D', 'D', 'M', 'A', 'GK', 'A', 'A', 'D', 'M', 'A', 'A', 'A', 'D', 'GK', 'M', 'A', 'A', 'M',
 'A', 'GK', 'D', 'A', 'M', 'M', 'A', 'D', 'A', 'D', 'A', 'A', 'M', 'M', 'A', 'A', 'M', 'D', 'D', 'D', 'D', 'GK', 'A',
 'GK', 'A', 'D', 'D', 'D', 'A', 'D', 'A', 'M', 'M', 'M', 'M', 'M', 'A', 'M', 'D', 'D', 'D', 'A', 'D', 'M', 'GK', 'M',
 'D', 'D', 'M', 'D', 'GK', 'M', 'A', 'M', 'M', 'D', 'D', 'M', 'A', 'D', 'A', 'M', 'GK', 'M', 'D', 'A', 'D', 'A', 'D',
 'M', 'GK', 'D', 'M', 'A', 'A', 'A', 'A', 'D', 'A', 'D', 'D', 'D', 'D', 'GK', 'D', 'GK', 'D', 'D', 'A', 'A', 'A', 'GK',
 'D', 'M', 'GK', 'M', 'M', 'GK', 'D', 'A', 'A', 'D', 'M', 'M', 'M', 'A', 'D', 'M', 'D', 'M', 'A', 'D', 'M', 'D', 'A',
 'GK', 'D', 'M', 'D', 'GK', 'D', 'M', 'GK', 'M', 'D', 'A', 'A', 'D', 'A', 'D', 'A', 'D', 'A', 'D', 'M', 'M', 'D', 'M',
 'A', 'D', 'M', 'D', 'D', 'M', 'A', 'A', 'M', 'A', 'M', 'M', 'A', 'GK', 'GK', 'M', 'GK', 'D', 'D', 'A', 'M', 'D', 'GK',
 'D', 'GK', 'D', 'A', 'M', 'A', 'GK', 'D', 'GK', 'A', 'M', 'M', 'M', 'D', 'M', 'M', 'M', 'GK', 'D', 'D', 'M', 'M', 'D',
 'D', 'A', 'M', 'M', 'M', 'A', 'GK', 'D', 'A', 'M', 'M', 'GK', 'A', 'A', 'M', 'A', 'M', 'M', 'M', 'M', 'M', 'M', 'GK',
 'M', 'M', 'D', 'M', 'M', 'D', 'D', 'GK', 'M', 'D', 'GK', 'D', 'M', 'M', 'A', 'D', 'M', 'M', 'D', 'D', 'D', 'M', 'M',
 'M', 'A', 'D', 'A', 'GK', 'M', 'A', 'M', 'D', 'M', 'M', 'D', 'M', 'M', 'M', 'M', 'D', 'M', 'D', 'M', 'A', 'GK', 'A',
 'A', 'D', 'D', 'D', 'A', 'M', 'D', 'D', 'M', 'M', 'M', 'M', 'M', 'D', 'D', 'GK', 'GK', 'D', 'M', 'D', 'A', 'D', 'D',
 'M', 'D', 'M', 'M', 'A', 'A', 'D', 'D', 'D', 'M', 'D', 'D', 'A', 'D', 'M', 'A', 'A', 'D', 'D', 'A', 'A', 'D', 'GK',
 'M', 'M', 'A', 'A', 'M', 'A', 'A', 'M', 'GK', 'M', 'D', 'A', 'A', 'A', 'M', 'M', 'M', 'D', 'M', 'A', 'M', 'A', 'A',
 'M', 'D', 'A', 'GK', 'M', 'D', 'A', 'D', 'D', 'M', 'M', 'A', 'D', 'M', 'D', 'A', 'M', 'M', 'M', 'A', 'M', 'M', 'M',
 'M', 'A', 'A', 'M', 'A', 'A', 'D', 'D', 'GK', 'A', 'M', 'A', 'D', 'A', 'M', 'GK', 'D', 'M', 'M', 'D', 'M', 'D', 'D',
 'A', 'M', 'A', 'GK', 'A', 'A', 'D', 'M', 'D', 'A', 'D', 'M', 'D', 'M', 'A', 'GK', 'M', 'M', 'M', 'M', 'A', 'M', 'M',
 'D', 'M', 'M', 'D', 'M', 'M', 'A', 'M', 'M', 'M', 'M', 'D', 'M', 'M', 'D', 'A', 'A', 'D', 'D', 'M', 'M', 'M', 'M',
 'GK', 'GK', 'A', 'M', 'M', 'A', 'M', 'M', 'M', 'D', 'M', 'D', 'M', 'M', 'A', 'M', 'GK', 'A', 'A', 'A', 'GK', 'M', 'A',
 'M', 'D', 'M', 'M', 'A', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'GK', 'D', 'M', 'M', 'D', 'GK', 'GK', 'D', 'M',
 'A', 'A', 'M', 'A', 'M', 'M', 'M', 'A', 'GK', 'M', 'M', 'A', 'D', 'M', 'M', 'M', 'D', 'M', 'A', 'M', 'D', 'M', 'A',
 'A', 'A', 'D', 'D', 'D', 'D', 'A', 'D', 'M', 'D', 'M', 'D', 'A', 'M', 'D', 'A', 'D', 'A', 'GK', 'A', 'D', 'M', 'A',
 'M', 'D', 'M', 'D', 'M', 'M', 'D', 'A', 'M', 'A', 'D', 'M', 'D', 'D', 'A', 'GK', 'A', 'A', 'M', 'M', 'M', 'M', 'A',
 'M', 'A', 'A', 'D', 'M', 'GK', 'M', 'D', 'A', 'M', 'A', 'M', 'GK', 'A', 'M', 'D', 'M', 'D', 'A', 'A', 'D', 'M', 'A',
 'M', 'M', 'A', 'M', 'A', 'M', 'M', 'A', 'D', 'D', 'D', 'GK', 'D', 'A', 'D', 'D', 'M', 'D', 'A', 'D', 'D', 'D', 'M',
 'M', 'A', 'D', 'M', 'D', 'A', 'D', 'M', 'M', 'D', 'D', 'M', 'M', 'D', 'GK', 'D', 'D', 'D', 'M', 'D', 'A', 'D', 'A',
 'D', 'M', 'M', 'GK', 'A', 'A', 'M', 'D', 'GK', 'D', 'M', 'D', 'M', 'A', 'GK', 'GK', 'M', 'M', 'A', 'M', 'M', 'A', 'M',
 'GK', 'D', 'D', 'M', 'M', 'D', 'M', 'A', 'M', 'GK', 'D', 'D', 'D', 'A', 'A', 'GK', 'D', 'GK', 'D', 'D', 'GK', 'D', 'A',
 'A', 'M', 'D', 'A', 'D', 'D', 'M', 'D', 'A', 'A', 'M', 'M', 'A', 'D', 'M', 'M', 'A', 'D', 'M', 'M', 'A', 'A', 'M', 'M',
 'A', 'D', 'M', 'M', 'D', 'M', 'D', 'GK', 'A', 'M', 'A', 'A', 'D', 'A', 'M', 'M', 'M', 'D', 'D', 'D', 'M', 'D', 'A',
 'M', 'GK', 'M', 'A', 'GK', 'M', 'M', 'M', 'A', 'M', 'GK', 'D', 'A', 'D', 'D', 'D', 'D', 'D', 'M', 'M', 'M', 'GK', 'A',
 'D', 'A', 'M', 'A', 'A', 'M', 'A', 'D', 'M', 'M', 'A', 'M', 'A', 'D', 'M', 'D', 'A', 'D', 'M', 'M', 'M', 'A', 'D', 'A',
 'D', 'A', 'M', 'M', 'M', 'A', 'M', 'M', 'A', 'D', 'M', 'D', 'D', 'M', 'M', 'D', 'M', 'A', 'D', 'M', 'A', 'M', 'GK',
 'D', 'M', 'A', 'GK', 'M', 'A', 'A', 'D', 'M', 'A', 'D', 'A', 'GK', 'D', 'D', 'A', 'M', 'A', 'D', 'D', 'D', 'A', 'M',
 'D', 'GK', 'A', 'A', 'M', 'D', 'D', 'GK', 'D', 'M', 'M', 'D', 'M', 'A', 'A', 'M', 'M', 'A', 'D', 'M', 'M', 'M', 'D',
 'M', 'D', 'M', 'M', 'A', 'A', 'D', 'A', 'A', 'A', 'M', 'M', 'A', 'M', 'M', 'GK', 'M', 'D', 'D', 'M', 'A', 'M', 'M',
 'M', 'A', 'A', 'A', 'A', 'D', 'D', 'A', 'D', 'D', 'M', 'D', 'GK', 'GK', 'M', 'D', 'D', 'A', 'D', 'M', 'GK', 'A', 'M',
 'M', 'A', 'M', 'A', 'A', 'D', 'A', 'D', 'A', 'D', 'D', 'D', 'D', 'D', 'M', 'GK', 'M', 'A', 'M', 'M', 'M', 'D', 'M',
 'M', 'A', 'M', 'D', 'D', 'D', 'M', 'D', 'M', 'M', 'D', 'GK', 'GK', 'D', 'M', 'M', 'M', 'D', 'M', 'M', 'D', 'GK', 'A',
 'GK', 'D', 'M', 'A', 'M', 'M', 'M', 'A', 'A', 'A', 'M', 'M', 'A', 'D', 'A', 'A', 'D', 'M', 'D', 'D', 'M', 'A', 'D',
 'A', 'D', 'M', 'A', 'A', 'M', 'A', 'A', 'M', 'D', 'M', 'A', 'M', 'M', 'M', 'A', 'D', 'A', 'A', 'A', 'D', 'D', 'M', 'M',
 'M', 'D', 'D', 'M', 'A', 'M', 'M', 'A', 'M', 'D', 'D', 'A', 'M', 'A', 'M', 'D', 'D', 'M', 'M', 'GK', 'D', 'M', 'D',
 'M', 'D', 'D', 'D', 'A', 'A', 'M', 'M', 'M', 'A', 'D', 'A', 'D', 'M', 'D', 'M', 'A', 'A', 'D', 'M', 'A', 'A', 'D', 'A',
 'GK', 'D', 'M', 'M', 'M', 'A', 'M', 'A', 'A', 'GK', 'M', 'D', 'A', 'A', 'A', 'GK', 'GK', 'M', 'M', 'D', 'D', 'M', 'M',
 'D', 'GK', 'M', 'GK', 'M', 'M', 'A', 'M', 'A', 'M', 'D', 'M', 'M', 'D', 'A', 'GK', 'D', 'GK', 'M', 'D', 'A', 'M', 'D',
 'D', 'D', 'A', 'D', 'M', 'M', 'M', 'A', 'M', 'A', 'M', 'D', 'M', 'A', 'A', 'D', 'M', 'M', 'M', 'M', 'A', 'D', 'M', 'A',
 'D', 'D', 'A', 'D', 'M', 'M', 'D', 'M', 'A', 'M', 'M', 'A', 'A', 'M', 'A', 'GK', 'M', 'GK', 'A', 'A', 'A', 'M', 'A',
 'GK', 'M', 'A', 'D', 'M', 'D', 'M', 'D', 'A', 'A', 'D', 'M', 'M', 'D', 'D', 'D', 'D', 'M', 'M', 'A', 'D', 'GK', 'M',
 'M', 'A', 'GK', 'D', 'A', 'M', 'D', 'D', 'GK', 'A', 'D', 'D', 'M', 'M', 'A', 'D', 'GK', 'D', 'M', 'M', 'M', 'A', 'M',
 'M', 'A', 'D', 'GK', 'GK', 'D', 'D', 'M', 'D', 'M', 'D', 'M', 'GK', 'A', 'A', 'D', 'A', 'M', 'D', 'D', 'D', 'GK', 'D',
 'A', 'A', 'D', 'D', 'D', 'M', 'A', 'D', 'M', 'A', 'M', 'GK', 'A', 'M', 'A', 'D', 'D', 'M', 'D', 'D', 'A', 'M', 'M',
 'D', 'D', 'D', 'D', 'M', 'M', 'A', 'A', 'D', 'D', 'M', 'GK', 'A', 'A', 'A', 'M', 'D', 'M', 'D', 'M', 'M', 'M', 'D',
 'D', 'A', 'D', 'M', 'M', 'D', 'M', 'M', 'A', 'A', 'A', 'GK', 'M', 'D', 'D', 'M', 'M', 'D', 'M', 'D', 'D', 'M', 'D',
 'A', 'M', 'D', 'M', 'A', 'A', 'GK', 'D', 'M', 'M', 'A', 'A', 'A', 'GK', 'A', 'M', 'M', 'M', 'A', 'D', 'M', 'D', 'A',
 'A', 'A', 'M', 'A', 'A', 'M', 'GK', 'A', 'A', 'A', 'M', 'D', 'M', 'D', 'D', 'D', 'A', 'M', 'A', 'GK', 'M', 'D', 'D',
 'D', 'M', 'A', 'GK', 'M', 'D', 'M', 'M', 'M', 'M', 'GK', 'D', 'M', 'A', 'D', 'D', 'D', 'A', 'GK', 'M', 'D', 'M', 'M',
 'A', 'A', 'M', 'M', 'D', 'D', 'D', 'GK', 'GK', 'M', 'A', 'D', 'A', 'D', 'D', 'M', 'GK', 'D', 'M', 'A', 'M', 'A', 'M',
 'D', 'D', 'M', 'A', 'D', 'M', 'D', 'D', 'M', 'M', 'D', 'M', 'A', 'A', 'D', 'M', 'A', 'M', 'M', 'GK', 'M', 'M', 'M',
 'D', 'GK', 'D', 'A', 'M', 'M', 'GK', 'M', 'A', 'A', 'D', 'D', 'D', 'GK', 'M', 'M', 'A', 'M', 'M', 'M', 'D', 'M', 'A',
 'M', 'D', 'D', 'A', 'M', 'GK', 'D', 'D', 'M', 'D', 'A', 'GK', 'D', 'A', 'M', 'A', 'D', 'D', 'GK', 'A', 'D', 'M', 'M',
 'A', 'M', 'M', 'D', 'GK', 'M', 'M', 'D', 'GK', 'M', 'GK', 'A', 'D', 'M', 'M', 'A', 'A', 'M', 'A', 'M', 'GK', 'D', 'D',
 'M', 'M', 'M', 'M', 'A', 'D', 'A', 'GK', 'D', 'D', 'D', 'M', 'GK', 'D', 'GK', 'GK', 'A', 'D', 'GK', 'GK', 'A', 'GK',
 'M', 'A', 'M', 'M', 'M', 'M', 'M', 'D', 'GK', 'M', 'D', 'D', 'A', 'A', 'D', 'D', 'GK', 'M', 'A', 'M', 'M', 'D', 'M',
 'D', 'D', 'A', 'M', 'M', 'M', 'D', 'A', 'D', 'GK', 'M', 'D', 'M', 'A', 'A', 'D', 'A', 'M', 'A', 'D', 'M', 'A', 'M',
 'GK', 'D', 'A', 'A', 'M', 'A', 'D', 'A', 'A', 'M', 'D', 'M', 'D', 'D', 'M', 'GK', 'A', 'A', 'D', 'D', 'D', 'M', 'M',
 'M', 'A', 'M', 'D', 'A', 'M', 'D', 'M', 'M', 'A', 'D', 'GK', 'M', 'A', 'D', 'M', 'A', 'D', 'M', 'M', 'D', 'M', 'D',
 'A', 'M', 'A', 'M', 'GK', 'A', 'M', 'M', 'D', 'M', 'M', 'D', 'D', 'A', 'M', 'M', 'M', 'M', 'A', 'M', 'M', 'D', 'A',
 'D', 'A', 'M', 'A', 'D', 'GK', 'A', 'D', 'M', 'GK', 'D', 'D', 'D', 'A', 'D', 'M', 'M', 'A', 'M', 'A', 'M', 'M', 'D',
 'A', 'A', 'D', 'D', 'M', 'D', 'GK', 'A', 'D', 'A', 'D', 'M', 'D', 'D', 'D', 'GK', 'D', 'D', 'A', 'GK', 'D', 'D', 'D',
 'A', 'A', 'GK', 'D', 'D', 'D', 'A', 'A', 'M', 'M', 'D', 'D', 'D', 'GK', 'A', 'D', 'M', 'D', 'A', 'D', 'M', 'D', 'A',
 'D', 'M', 'A', 'A', 'D', 'A', 'M', 'M', 'A', 'D', 'A', 'A', 'M', 'D', 'GK', 'M', 'A', 'M', 'D', 'D', 'D', 'A', 'D',
 'M', 'D', 'A', 'M', 'D', 'D', 'D', 'D', 'M', 'A', 'M', 'M', 'GK', 'D', 'M', 'GK', 'A', 'A', 'D', 'M', 'M', 'A', 'D',
 'M', 'M', 'M', 'A', 'A', 'M', 'A', 'A', 'D', 'A', 'A', 'D', 'M', 'M', 'D', 'D', 'M', 'M', 'GK', 'M', 'D', 'D', 'M',
 'GK', 'A', 'D', 'D', 'A', 'A', 'D', 'A', 'M', 'GK', 'A', 'D', 'M', 'M', 'M', 'GK', 'A', 'M', 'A', 'A', 'A', 'A', 'M',
 'A', 'A', 'M', 'D', 'M', 'M', 'A', 'D', 'D', 'A', 'A', 'M', 'M', 'M', 'M', 'D', 'D', 'A', 'M', 'D', 'A', 'D', 'D', 'D',
 'A', 'M', 'M', 'M', 'D', 'M', 'M', 'M', 'M', 'M', 'M', 'A', 'A', 'A', 'D', 'GK', 'M', 'M', 'M', 'A', 'A', 'M', 'M',
 'M', 'A', 'M', 'M', 'GK', 'M', 'D', 'A', 'M', 'D', 'GK', 'M', 'GK', 'M', 'M', 'A', 'M', 'D', 'A', 'M', 'M', 'A', 'M',
 'M', 'A', 'M', 'M', 'A', 'D', 'M', 'M', 'D', 'D', 'M', 'D', 'A', 'D', 'A', 'A', 'D', 'A', 'M', 'A', 'M', 'GK', 'A',
 'M', 'M', 'A', 'D', 'D', 'A', 'A', 'A', 'A', 'A', 'D', 'M', 'D', 'M', 'M', 'GK', 'D', 'D', 'A', 'GK', 'M', 'D', 'D',
 'M', 'D', 'D', 'M', 'D', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'D', 'M', 'M', 'A', 'M', 'D', 'D', 'D', 'D', 'M', 'A', 'D',
 'D', 'D', 'A', 'D', 'A', 'A', 'D', 'D', 'D', 'A', 'D', 'M', 'M', 'D', 'M', 'A', 'D', 'M', 'D', 'A', 'D', 'A', 'D', 'A',
 'M', 'GK', 'D', 'GK', 'M', 'D', 'M', 'A', 'D', 'A', 'D', 'A', 'M', 'D', 'GK', 'A', 'A', 'M', 'M', 'M', 'M', 'M', 'M',
 'M', 'A', 'D', 'M', 'D', 'D', 'D', 'A', 'A', 'A', 'M', 'M', 'D', 'GK', 'A', 'A', 'M', 'A', 'A', 'M', 'D', 'M', 'M',
 'M', 'M', 'M', 'M', 'A', 'A', 'D', 'A', 'A', 'M', 'M', 'M', 'M', 'M', 'D', 'D', 'A', 'A', 'M', 'D', 'D', 'M', 'A', 'M',
 'D', 'M', 'M', 'D', 'D', 'M', 'D', 'M', 'M', 'A', 'A', 'D', 'A', 'A', 'D', 'A', 'A', 'M', 'D', 'M', 'GK', 'A', 'D',
 'D', 'GK', 'GK', 'D', 'D', 'M', 'M', 'A', 'A', 'A', 'D', 'M', 'D', 'M', 'D', 'D', 'A', 'A', 'A', 'A', 'D', 'A', 'A',
 'M', 'M', 'D', 'A', 'M', 'M', 'M', 'A', 'M', 'M', 'D', 'GK', 'A', 'M', 'GK', 'D', 'D', 'M', 'A', 'GK', 'M', 'M', 'M',
 'D', 'M', 'M', 'M', 'M', 'A', 'M', 'GK', 'M', 'A', 'M', 'M', 'M', 'M', 'A', 'A', 'A', 'M', 'D', 'M', 'D', 'D', 'M',
 'M', 'A', 'D', 'M', 'D', 'M', 'A', 'M', 'A', 'D', 'A', 'GK', 'M', 'M', 'D', 'M', 'A', 'M', 'M', 'M', 'D', 'GK', 'GK',
 'D', 'M', 'D', 'A', 'M', 'A', 'GK', 'D', 'D', 'M', 'GK', 'D', 'D', 'A', 'M', 'D', 'A', 'M', 'M', 'M', 'D', 'M', 'D',
 'A', 'M', 'A', 'A', 'M', 'M', 'A', 'M', 'M', 'A', 'GK', 'D', 'GK', 'D', 'A', 'D', 'M', 'GK', 'D', 'M', 'M', 'GK', 'M',
 'M', 'A', 'A', 'M', 'GK', 'D', 'GK', 'A', 'D', 'M', 'A', 'D', 'A', 'A', 'A', 'A', 'M', 'A', 'D', 'A', 'A', 'GK', 'M',
 'M', 'D', 'D', 'D', 'A', 'GK', 'GK', 'D', 'M', 'D', 'GK', 'M', 'GK', 'M', 'D', 'A', 'M', 'D', 'M', 'M', 'A', 'D', 'A',
 'A', 'M', 'D', 'A', 'GK', 'A', 'A', 'M', 'GK', 'M', 'M', 'A', 'D', 'M', 'M', 'GK', 'D', 'M', 'M', 'M', 'M', 'A', 'D',
 'GK', 'A', 'M', 'D', 'M', 'A', 'M', 'D', 'D', 'M', 'M', 'A', 'GK', 'GK', 'A', 'D', 'M', 'M', 'M', 'M', 'D', 'D', 'D',
 'M', 'M', 'D', 'D', 'D', 'GK', 'D', 'D', 'M', 'D', 'D', 'D', 'M', 'M', 'A', 'A', 'M', 'A', 'GK', 'D', 'D', 'M', 'M',
 'A', 'D', 'GK', 'A', 'M', 'D', 'A', 'D', 'GK', 'GK', 'M', 'D', 'A', 'M', 'D', 'A', 'A', 'M', 'M', 'D', 'D', 'D', 'A',
 'GK', 'A', 'A', 'M', 'M', 'M', 'M', 'D', 'A', 'M', 'A', 'A', 'D', 'D', 'D', 'A', 'M', 'D', 'D', 'D', 'D', 'D', 'A',
 'A', 'A', 'M', 'D', 'A', 'A', 'M', 'M', 'D', 'D', 'A', 'M', 'M', 'A', 'A', 'M', 'D', 'D', 'A', 'A', 'GK', 'A', 'A',
 'M', 'A', 'D', 'GK', 'D', 'M', 'A', 'M', 'A', 'M', 'D', 'M', 'D', 'D', 'GK', 'M', 'D', 'A', 'M', 'D', 'D', 'M', 'A',
 'D', 'M', 'M', 'D', 'D', 'D', 'A', 'D', 'D', 'M', 'M', 'M', 'A', 'GK', 'GK', 'M', 'D', 'M', 'A', 'D', 'A', 'GK', 'M',
 'A', 'A', 'A', 'GK', 'M', 'M', 'M', 'M', 'M', 'D', 'M', 'GK', 'A', 'A', 'M', 'A', 'A', 'A', 'M', 'D', 'M', 'D', 'A',
 'M', 'M', 'GK', 'M', 'D', 'GK', 'D', 'D', 'M', 'D', 'A', 'M', 'A', 'M', 'D', 'D', 'GK', 'D', 'D', 'M', 'D', 'M', 'A',
 'M', 'D', 'GK', 'A', 'M', 'GK', 'A', 'A', 'A', 'M', 'M', 'GK', 'M', 'D', 'M', 'D', 'GK', 'GK', 'D', 'D', 'M', 'A', 'M',
 'D', 'A', 'A', 'D', 'A', 'M', 'D', 'M', 'A', 'A', 'GK', 'M', 'D', 'M', 'A', 'M', 'A', 'A', 'A', 'D', 'D', 'M', 'M',
 'M', 'A', 'A', 'A', 'GK', 'M', 'A', 'D', 'D', 'M', 'D', 'M', 'A', 'M', 'M', 'A', 'A', 'D', 'D', 'D', 'A', 'D', 'A',
 'D', 'D', 'A', 'GK', 'D', 'M', 'M', 'GK', 'M', 'M', 'D', 'A', 'A', 'M', 'D', 'M', 'D', 'D', 'D', 'A', 'GK', 'D', 'GK',
 'M', 'D', 'M', 'A', 'A', 'D', 'M', 'D', 'D', 'A', 'A', 'M', 'M', 'D', 'D', 'D', 'D', 'M', 'M', 'D', 'A', 'M', 'D', 'D',
 'M', 'A', 'M', 'M', 'D', 'A', 'M', 'D', 'M', 'D', 'M', 'D', 'D', 'D', 'M', 'A', 'M', 'A', 'A', 'GK', 'A', 'D', 'M',
 'A', 'D', 'GK', 'D', 'A', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'A', 'D', 'A', 'D', 'M', 'M', 'A', 'D', 'D', 'D',
 'D', 'D', 'A', 'A', 'A', 'A', 'A', 'M', 'GK', 'M', 'M', 'D', 'M', 'M', 'M', 'M', 'M', 'M', 'D', 'D', 'M', 'M', 'M',
 'D', 'M', 'M', 'A', 'M', 'M', 'M', 'D', 'A', 'M', 'GK', 'A', 'D', 'A', 'M', 'M', 'D', 'M', 'A', 'M', 'A', 'A', 'M',
 'D', 'A', 'A', 'A', 'M', 'A', 'M', 'D', 'M', 'D', 'A', 'D', 'M', 'A', 'D', 'GK', 'D', 'D', 'A', 'A', 'A', 'M', 'M',
 'A', 'M', 'M', 'M', 'A', 'D', 'D', 'A', 'A', 'GK', 'A', 'D', 'GK', 'M', 'M', 'D', 'M', 'GK', 'D', 'GK', 'D', 'M', 'A',
 'M', 'A', 'M', 'A', 'D', 'D', 'D', 'D', 'D', 'GK', 'A', 'A', 'A', 'D', 'D', 'M', 'M', 'D', 'M', 'GK', 'M', 'A', 'GK',
 'M', 'M', 'D', 'A', 'A', 'M', 'GK', 'D', 'A', 'A', 'M', 'A', 'D', 'GK', 'M', 'GK', 'M', 'A', 'D', 'A', 'D', 'A', 'A',
 'M', 'A', 'A', 'GK', 'M', 'D', 'D', 'M', 'A', 'A', 'GK', 'D', 'M', 'M', 'M', 'A', 'A', 'A', 'D', 'GK', 'A', 'D', 'M',
 'A', 'GK', 'A', 'A', 'GK', 'D', 'M', 'A', 'A', 'D', 'M', 'D', 'D', 'A', 'M', 'M', 'GK', 'D', 'D', 'A', 'A', 'M', 'D',
 'A', 'A', 'M', 'D', 'M', 'A', 'D', 'D', 'D', 'M', 'M', 'D', 'D', 'M', 'M', 'A', 'D', 'A', 'M', 'D', 'D', 'M', 'M', 'A',
 'A', 'D', 'M', 'M', 'D', 'A', 'A', 'M', 'D', 'D', 'D', 'M', 'GK', 'D', 'A', 'M', 'D', 'A', 'M', 'M', 'A', 'M', 'A',
 'GK', 'A', 'D', 'D', 'M', 'A', 'A', 'A', 'D', 'D', 'A', 'D', 'D', 'M', 'GK', 'D', 'D', 'M', 'M', 'M', 'M', 'A', 'D',
 'M', 'D', 'D', 'M', 'A', 'D', 'M', 'D', 'A', 'A', 'A', 'A', 'M', 'GK', 'M', 'A', 'A', 'D', 'D', 'M', 'M', 'M', 'A',
 'D', 'A', 'GK', 'D', 'D', 'A', 'M', 'M', 'D', 'A', 'GK', 'D', 'M', 'M', 'M', 'A', 'M', 'D', 'D', 'M', 'D', 'GK', 'GK',
 'D', 'D', 'M', 'D', 'M', 'M', 'M', 'M', 'M', 'D', 'M', 'M', 'D', 'M', 'M', 'GK', 'D', 'GK', 'A', 'M', 'M', 'D', 'D',
 'M', 'M', 'D', 'M', 'D', 'D', 'M', 'D', 'D', 'A', 'GK', 'A', 'M', 'A', 'D', 'D', 'A', 'M', 'GK', 'D', 'A', 'D', 'A',
 'M', 'D', 'A', 'M', 'GK', 'M', 'A', 'A', 'GK', 'M', 'D', 'M', 'A', 'M', 'D', 'M', 'M', 'GK', 'D', 'M', 'A', 'A', 'A',
 'M', 'A', 'D', 'M', 'M', 'A', 'M', 'A', 'M', 'GK', 'M', 'A', 'D', 'M', 'A', 'M', 'D', 'GK', 'A', 'A', 'D', 'D', 'D',
 'M', 'D', 'A', 'A', 'A', 'M', 'M', 'D', 'A', 'A', 'A', 'M', 'A', 'M', 'A', 'D', 'GK', 'GK', 'M', 'D', 'GK', 'A', 'A',
 'M', 'M', 'D', 'D', 'M', 'M', 'GK', 'D', 'D', 'GK', 'M', 'M', 'M', 'A', 'GK', 'A', 'M', 'A', 'M', 'D', 'M', 'M', 'GK',
 'M', 'A', 'GK', 'D', 'GK', 'GK', 'A', 'D', 'A', 'GK', 'M', 'M', 'A', 'GK', 'A', 'M', 'M', 'A', 'M', 'D', 'D', 'M', 'M',
 'A', 'M', 'M', 'M', 'A', 'A', 'M', 'A', 'D', 'D', 'GK', 'A', 'D', 'D', 'D', 'D', 'M', 'D', 'M', 'A', 'GK', 'A', 'D',
 'A', 'A', 'A', 'A', 'D', 'GK', 'D', 'M', 'D', 'M', 'A', 'D', 'A', 'M', 'D', 'GK', 'A', 'M', 'D', 'D', 'GK', 'D', 'A',
 'M', 'M', 'D', 'M', 'A', 'M', 'M', 'M', 'M', 'M', 'D', 'M', 'A', 'D', 'M', 'D', 'A', 'GK', 'D', 'A', 'M', 'D', 'D',
 'GK', 'A', 'M', 'M', 'D', 'D', 'M', 'D', 'D', 'D', 'GK', 'A', 'M', 'M', 'D', 'M', 'D', 'M', 'D', 'A', 'A', 'M', 'D',
 'GK', 'D', 'D', 'A', 'D', 'GK', 'D', 'GK', 'M', 'M', 'GK', 'A', 'D', 'M', 'D', 'D', 'A', 'GK', 'GK', 'D', 'A', 'A',
 'D', 'D', 'M', 'M', 'D', 'M', 'M', 'D', 'M', 'D', 'M', 'M', 'D', 'D', 'D', 'M', 'D', 'D', 'GK', 'GK', 'M', 'GK', 'D',
 'A', 'M', 'D', 'GK', 'M', 'GK', 'D', 'M', 'D', 'M', 'D', 'D', 'A', 'D', 'M', 'M', 'M', 'D', 'M', 'M', 'D', 'D', 'A',
 'D', 'A', 'A', 'M', 'D', 'A', 'M', 'D', 'D', 'D', 'D', 'M', 'D', 'D', 'A', 'M', 'D', 'M', 'A', 'M', 'D', 'M', 'M', 'M',
 'A', 'M', 'D', 'GK', 'M', 'M', 'A', 'D', 'D', 'D', 'D', 'A', 'D', 'D', 'D', 'M', 'D', 'D', 'D', 'A', 'D', 'M', 'A',
 'D', 'M', 'M', 'GK', 'M', 'A', 'M', 'M', 'M', 'D', 'M', 'M', 'M', 'D', 'A', 'M', 'D', 'M', 'A', 'D', 'D', 'A', 'D',
 'M', 'M', 'M', 'GK', 'M', 'D', 'M', 'A', 'D', 'D', 'M', 'A', 'M', 'A', 'M', 'A', 'D', 'A', 'M', 'M', 'M', 'M', 'D',
 'A', 'A', 'M', 'GK', 'A', 'D', 'D', 'M', 'D', 'M', 'D', 'M', 'D', 'M', 'A', 'M', 'D', 'M', 'M', 'D', 'M', 'D', 'A',
 'A', 'D', 'A', 'D', 'GK', 'D', 'M', 'D', 'M', 'D', 'D', 'D', 'M', 'M', 'M', 'D', 'A', 'D', 'GK', 'D', 'M', 'D', 'A',
 'M', 'GK', 'D', 'M', 'D', 'M', 'D', 'M', 'GK', 'GK', 'D', 'M', 'A', 'D', 'GK', 'M', 'M', 'D', 'M', 'D', 'GK', 'GK',
 'D', 'A', 'M', 'GK', 'A', 'M', 'M', 'M', 'M', 'D', 'GK', 'D', 'M', 'D', 'M', 'D', 'A', 'A', 'GK', 'GK', 'A', 'D', 'A',
 'GK', 'M', 'A', 'A', 'M', 'GK', 'GK', 'D', 'M', 'D', 'M', 'A', 'D', 'D', 'M', 'GK', 'D', 'A', 'M', 'M', 'M', 'M', 'A',
 'D', 'GK', 'GK', 'D', 'M', 'D', 'M', 'A', 'D', 'A', 'M', 'D', 'M', 'M', 'D', 'A', 'M', 'D', 'M', 'M', 'D', 'A', 'GK',
 'M', 'GK', 'D', 'D', 'D', 'GK', 'D', 'M', 'M', 'M', 'D', 'GK', 'M', 'D', 'A', 'M', 'M', 'A', 'GK', 'M', 'D', 'D', 'M',
 'M', 'D', 'M', 'M', 'GK', 'A', 'M', 'A', 'A', 'A', 'GK', 'D', 'D', 'D', 'D', 'GK', 'D', 'GK', 'D', 'D', 'GK', 'M', 'D',
 'D', 'M', 'D', 'M', 'GK', 'A', 'M', 'M', 'A', 'D', 'D', 'D', 'D', 'GK', 'A', 'D', 'M', 'D', 'D', 'A', 'M', 'M', 'M',
 'A', 'GK', 'M', 'D', 'M', 'D', 'M', 'M', 'GK', 'D', 'GK', 'A', 'D', 'GK', 'M', 'M', 'M', 'M', 'M', 'A', 'M', 'D', 'M',
 'D', 'D', 'GK', 'M', 'D', 'GK', 'M', 'D', 'D', 'M', 'D', 'GK', 'A', 'A', 'D', 'D', 'M', 'M', 'M', 'M', 'D', 'A', 'M',
 'M', 'D', 'A', 'GK', 'D', 'D', 'D', 'M', 'GK', 'D', 'D', 'D', 'M', 'M', 'D', 'M', 'M', 'D', 'D', 'M', 'D', 'M', 'A',
 'M', 'M', 'D', 'M', 'D', 'D', 'GK', 'A', 'M', 'GK', 'M', 'M', 'D', 'M', 'GK', 'M', 'D', 'A', 'D', 'M', 'D', 'M', 'A',
 'A', 'M', 'M', 'M', 'M', 'D', 'D', 'D', 'A', 'D', 'A', 'D', 'A', 'A', 'D', 'GK', 'A', 'D', 'A', 'D', 'A', 'A', 'D',
 'M', 'M', 'D', 'M', 'A', 'M', 'D', 'M', 'M', 'A', 'A', 'D', 'GK', 'A', 'M', 'M', 'D', 'M', 'D', 'D', 'D', 'GK', 'D',
 'GK', 'A', 'M', 'M', 'D', 'A', 'D', 'M', 'D', 'D', 'D', 'A', 'D', 'M', 'M', 'M', 'D', 'GK', 'M', 'M', 'M', 'M', 'M',
 'D', 'D', 'GK', 'M', 'M', 'A', 'A', 'M', 'A', 'M', 'D', 'M', 'A', 'M', 'D', 'A', 'D', 'D', 'M', 'A', 'M', 'D', 'M',
 'M', 'GK', 'GK', 'GK', 'A', 'A', 'M', 'A', 'M', 'A', 'M', 'GK', 'D', 'GK', 'M', 'GK', 'M', 'D', 'D', 'A', 'GK', 'D',
 'M', 'D', 'M', 'A', 'A', 'D', 'D', 'A', 'D', 'M', 'A', 'M', 'M', 'D', 'M', 'M', 'M', 'A', 'M', 'GK', 'D', 'GK', 'M',
 'D', 'A', 'M', 'D', 'D', 'D', 'A', 'M', 'GK', 'A', 'A', 'D', 'M', 'A', 'GK', 'D', 'D', 'A', 'M', 'D', 'M', 'D', 'D',
 'D', 'D', 'D', 'A', 'M', 'M', 'M', 'M', 'GK', 'D', 'A', 'A', 'GK', 'A', 'M', 'D', 'D', 'D', 'GK', 'D', 'M', 'GK', 'M',
 'A', 'M', 'GK', 'M', 'A', 'M', 'A', 'D', 'M', 'D', 'A', 'D', 'A', 'GK', 'D', 'A', 'M', 'GK', 'M', 'GK', 'D', 'GK', 'D',
 'M', 'M', 'D', 'D', 'M', 'M', 'D', 'A', 'A', 'M', 'D', 'M', 'A', 'D', 'D', 'GK', 'M', 'D', 'A', 'D', 'M', 'GK', 'D',
 'GK', 'M', 'D', 'D', 'M', 'D', 'A', 'D', 'M', 'D', 'GK', 'M', 'GK', 'A', 'M', 'GK', 'GK', 'D', 'D', 'A', 'D', 'M',
 'GK', 'D', 'A', 'D', 'A', 'A', 'M', 'A', 'A', 'M', 'D', 'M', 'A', 'GK', 'D', 'M', 'D', 'M', 'GK', 'A', 'A', 'GK', 'A',
 'A', 'A', 'D', 'D', 'A', 'GK', 'M', 'A', 'M', 'M', 'D', 'D', 'M', 'M', 'M', 'D', 'D', 'M', 'M', 'D', 'M', 'M', 'D',
 'M', 'D', 'M', 'GK', 'GK', 'M', 'M', 'M', 'A', 'A', 'M', 'D', 'A', 'M', 'M', 'GK', 'M', 'A', 'A', 'A', 'D', 'D', 'M']

heights = [191, 184, 185, 180, 181, 187, 170, 179, 183, 186, 185, 170, 187, 183, 173, 188, 183, 180, 188, 175, 193, 180, 185, 170,
 183, 173, 185, 185, 168, 190, 178, 185, 185, 193, 183, 184, 178, 180, 177, 188, 177, 187, 186, 183, 189, 179, 196, 190,
 189, 188, 188, 188, 182, 185, 184, 178, 185, 193, 188, 179, 189, 188, 180, 178, 186, 188, 180, 185, 172, 179, 180, 174,
 183, 178, 187, 178, 193, 181, 180, 187, 179, 173, 175, 188, 187, 175, 171, 179, 180, 188, 185, 196, 183, 184, 186, 178,
 188, 168, 176, 178, 178, 192, 172, 170, 190, 175, 174, 179, 177, 187, 184, 185, 175, 193, 185, 191, 181, 183, 176, 176,
 182, 192, 187, 170, 189, 171, 181, 183, 178, 182, 186, 191, 175, 179, 180, 181, 178, 193, 179, 181, 186, 190, 190, 192,
 185, 178, 182, 171, 182, 173, 192, 175, 183, 183, 184, 176, 183, 186, 178, 185, 188, 193, 193, 170, 188, 196, 175, 180,
 184, 173, 180, 190, 186, 182, 183, 195, 188, 187, 190, 180, 194, 182, 182, 183, 178, 183, 171, 185, 177, 180, 195, 173,
 185, 186, 187, 178, 185, 174, 175, 176, 191, 170, 183, 180, 174, 191, 179, 178, 187, 191, 183, 180, 184, 183, 180, 185,
 184, 181, 186, 185, 182, 175, 173, 175, 176, 174, 184, 177, 185, 162, 180, 171, 183, 180, 180, 191, 196, 191, 176, 186,
 171, 190, 188, 180, 185, 176, 187, 188, 182, 178, 176, 175, 177, 191, 183, 189, 173, 180, 180, 185, 185, 180, 181, 183,
 180, 185, 175, 175, 177, 177, 182, 167, 176, 180, 194, 180, 187, 174, 182, 174, 181, 188, 188, 180, 183, 183, 184, 188,
 170, 182, 183, 170, 186, 191, 187, 188, 177, 180, 182, 174, 183, 178, 182, 190, 180, 182, 181, 180, 176, 172, 186, 180,
 185, 186, 179, 185, 180, 187, 181, 185, 181, 183, 181, 175, 187, 178, 182, 182, 183, 184, 170, 178, 175, 186, 175, 178,
 185, 178, 190, 187, 173, 186, 177, 193, 183, 175, 185, 179, 167, 175, 183, 188, 184, 191, 184, 170, 169, 175, 175, 185,
 193, 172, 179, 180, 179, 186, 180, 176, 190, 175, 175, 186, 196, 186, 187, 182, 178, 185, 183, 191, 183, 185, 186, 180,
 169, 185, 194, 186, 183, 183, 191, 189, 194, 174, 168, 185, 160, 191, 185, 186, 179, 188, 185, 189, 183, 183, 176, 183,
 180, 171, 187, 175, 190, 178, 175, 181, 185, 188, 180, 171, 184, 176, 181, 183, 178, 171, 187, 186, 186, 174, 174, 186,
 193, 191, 180, 181, 177, 195, 190, 185, 168, 183, 175, 191, 184, 182, 188, 182, 180, 192, 191, 185, 188, 180, 179, 183,
 192, 183, 183, 180, 173, 180, 190, 183, 182, 175, 180, 178, 181, 188, 175, 180, 183, 191, 183, 180, 182, 178, 189, 183,
 183, 178, 170, 178, 173, 180, 184, 180, 188, 180, 184, 191, 188, 195, 197, 186, 191, 189, 196, 185, 178, 200, 176, 184,
 189, 181, 185, 184, 191, 191, 184, 190, 190, 170, 183, 183, 169, 183, 185, 178, 183, 186, 190, 186, 188, 186, 183, 179,
 172, 185, 180, 183, 189, 180, 182, 185, 180, 193, 185, 175, 182, 182, 180, 185, 180, 188, 175, 183, 185, 185, 176, 189,
 186, 181, 181, 185, 188, 176, 179, 178, 178, 180, 185, 183, 183, 185, 186, 185, 188, 172, 175, 186, 181, 190, 177, 184,
 191, 173, 178, 180, 185, 183, 186, 175, 189, 189, 189, 189, 183, 166, 178, 175, 179, 185, 180, 190, 181, 185, 179, 185,
 188, 183, 173, 180, 181, 175, 182, 177, 182, 180, 182, 184, 181, 177, 178, 180, 183, 194, 185, 191, 180, 187, 181, 183,
 183, 180, 185, 178, 177, 183, 178, 173, 183, 191, 188, 188, 178, 175, 186, 183, 180, 184, 184, 194, 174, 178, 193, 175,
 190, 186, 186, 180, 186, 183, 177, 180, 175, 184, 184, 178, 166, 183, 186, 168, 178, 181, 188, 187, 180, 172, 185, 186,
 191, 172, 184, 186, 192, 180, 177, 183, 175, 180, 170, 180, 188, 180, 178, 196, 192, 186, 175, 184, 175, 171, 187, 170,
 183, 184, 178, 187, 179, 177, 172, 180, 170, 177, 184, 185, 191, 188, 193, 183, 188, 185, 183, 185, 187, 189, 188, 174,
 173, 172, 179, 171, 176, 173, 185, 183, 187, 178, 176, 187, 171, 185, 174, 186, 179, 192, 173, 183, 183, 183, 186, 184,
 185, 171, 184, 189, 183, 173, 184, 183, 184, 184, 179, 184, 185, 181, 170, 176, 191, 173, 183, 178, 189, 183, 187, 202,
 180, 183, 186, 182, 186, 182, 190, 178, 185, 181, 186, 171, 183, 185, 184, 190, 167, 175, 172, 190, 168, 180, 188, 191,
 178, 178, 175, 183, 191, 183, 182, 187, 181, 175, 186, 175, 189, 180, 188, 180, 183, 179, 184, 178, 185, 185, 182, 179,
 183, 170, 183, 178, 187, 184, 168, 186, 183, 179, 186, 170, 178, 184, 191, 187, 174, 178, 186, 184, 193, 188, 185, 188,
 173, 175, 195, 180, 187, 182, 183, 188, 173, 197, 173, 187, 184, 190, 188, 174, 190, 185, 182, 191, 187, 193, 173, 180,
 172, 176, 191, 187, 184, 184, 199, 175, 191, 190, 183, 192, 191, 189, 174, 185, 184, 185, 185, 193, 183, 189, 177, 183,
 188, 170, 185, 178, 188, 178, 170, 193, 173, 173, 180, 180, 175, 173, 185, 185, 189, 176, 173, 183, 175, 179, 193, 188,
 183, 183, 175, 183, 176, 180, 185, 180, 187, 180, 177, 196, 175, 176, 188, 187, 183, 173, 191, 183, 188, 186, 176, 173,
 171, 179, 173, 192, 182, 180, 191, 182, 192, 185, 192, 186, 179, 178, 186, 179, 176, 182, 184, 178, 182, 182, 190, 183,
 188, 187, 183, 172, 175, 182, 179, 174, 188, 186, 174, 191, 180, 188, 183, 183, 184, 180, 175, 188, 181, 188, 186, 188,
 175, 188, 178, 180, 175, 185, 185, 176, 184, 173, 182, 176, 185, 194, 185, 177, 184, 171, 186, 184, 178, 180, 187, 186,
 180, 190, 188, 182, 174, 193, 178, 184, 170, 166, 176, 168, 200, 180, 182, 192, 167, 186, 178, 175, 174, 188, 184, 189,
 174, 193, 182, 194, 183, 170, 170, 173, 184, 178, 177, 178, 172, 169, 191, 175, 176, 178, 183, 181, 175, 191, 181, 177,
 170, 180, 184, 186, 178, 191, 183, 178, 188, 180, 178, 178, 193, 177, 183, 179, 170, 183, 179, 184, 184, 174, 190, 191,
 188, 180, 185, 183, 194, 183, 178, 180, 183, 171, 178, 184, 190, 185, 185, 173, 188, 185, 178, 173, 189, 194, 169, 179,
 170, 183, 188, 173, 190, 182, 191, 176, 179, 192, 189, 183, 180, 178, 194, 178, 180, 185, 183, 184, 181, 184, 170, 183,
 179, 179, 172, 178, 188, 187, 170, 178, 186, 180, 185, 175, 173, 175, 173, 167, 173, 181, 188, 180, 180, 184, 164, 170,
 179, 179, 173, 178, 182, 187, 179, 175, 191, 180, 180, 183, 172, 187, 179, 184, 167, 182, 175, 193, 188, 189, 182, 165,
 173, 181, 183, 180, 180, 183, 183, 183, 180, 173, 180, 190, 185, 183, 167, 191, 185, 185, 182, 178, 183, 183, 184, 189,
 182, 186, 178, 187, 182, 185, 182, 191, 185, 185, 191, 173, 180, 168, 187, 182, 183, 183, 186, 174, 193, 188, 185, 199,
 186, 174, 170, 189, 186, 176, 178, 188, 175, 178, 173, 177, 189, 178, 183, 176, 185, 198, 175, 183, 180, 194, 175, 181,
 174, 183, 188, 185, 175, 174, 171, 175, 189, 182, 189, 177, 183, 185, 183, 178, 185, 177, 175, 172, 181, 170, 179, 170,
 164, 166, 176, 176, 191, 169, 175, 184, 184, 168, 178, 179, 177, 185, 171, 179, 173, 182, 183, 193, 191, 189, 176, 185,
 177, 172, 177, 188, 178, 185, 181, 175, 181, 183, 175, 177, 180, 181, 174, 182, 185, 173, 185, 173, 188, 189, 188, 173,
 180, 182, 190, 180, 181, 174, 184, 182, 177, 182, 188, 175, 176, 184, 187, 193, 175, 185, 181, 186, 182, 180, 178, 182,
 175, 184, 184, 182, 180, 182, 178, 183, 168, 183, 186, 191, 185, 177, 186, 172, 181, 176, 181, 185, 185, 182, 185, 177,
 177, 180, 175, 188, 174, 177, 179, 171, 170, 185, 186, 168, 180, 185, 176, 182, 188, 180, 179, 194, 181, 181, 181, 188,
 182, 177, 191, 176, 182, 183, 176, 184, 175, 196, 177, 175, 179, 187, 181, 175, 174, 178, 192, 178, 183, 182, 167, 187,
 185, 179, 166, 180, 190, 176, 177, 171, 181, 187, 185, 176, 174, 179, 188, 178, 173, 188, 180, 178, 185, 177, 172, 178,
 184, 193, 185, 187, 190, 188, 189, 177, 180, 175, 180, 178, 185, 194, 188, 182, 170, 176, 190, 168, 186, 172, 177, 176,
 181, 185, 175, 180, 185, 186, 193, 178, 185, 189, 190, 185, 182, 191, 178, 187, 175, 193, 178, 182, 179, 178, 187, 174,
 179, 191, 170, 178, 180, 193, 182, 176, 176, 176, 186, 187, 175, 187, 187, 176, 184, 173, 186, 190, 191, 187, 186, 196,
 186, 175, 194, 184, 193, 192, 172, 179, 190, 183, 192, 182, 184, 183, 186, 172, 172, 175, 192, 187, 198, 178, 172, 190,
 185, 182, 196, 185, 182, 183, 184, 188, 181, 175, 176, 175, 191, 190, 174, 184, 180, 181, 184, 177, 183, 174, 180, 175,
 179, 179, 177, 177, 175, 175, 182, 188, 172, 181, 185, 176, 180, 180, 195, 178, 180, 183, 186, 185, 175, 181, 180, 186,
 188, 189, 193, 190, 185, 189, 191, 187, 182, 192, 181, 170, 183, 176, 188, 191, 177, 172, 177, 188, 181, 178, 178, 168,
 178, 182, 189, 174, 185, 185, 183, 186, 188, 182, 186, 174, 179, 187, 185, 177, 188, 192, 183, 172, 191, 184, 168, 186,
 177, 180, 199, 189, 180, 189, 178, 172, 185, 180, 171, 190, 186, 185, 173, 178, 179, 182, 184, 182, 179, 196, 182, 185,
 184, 180, 179, 178, 185, 178, 184, 173, 171, 172, 185, 184, 178, 180, 175, 185, 188, 196, 180, 173, 178, 175, 182, 188,
 183, 185, 177, 183, 190, 184, 186, 175, 188, 188, 171, 183, 185, 196, 185, 170, 183, 183, 170, 173, 180, 180, 188, 185,
 178, 173, 185, 185, 180, 188, 185, 177, 182, 185, 184, 177, 168, 183, 188, 188, 171, 188, 191, 186, 183, 184, 180, 177,
 187, 178, 180, 179, 189, 192, 187, 186, 185, 193, 179, 185, 190, 182, 185, 180, 185, 191, 173, 191, 177, 183, 175, 198,
 185, 173, 178, 180, 193, 178, 176, 175, 180, 182, 191, 175, 177, 184, 185, 185, 198, 180, 188, 176, 185, 193, 173, 173,
 185, 191, 188, 178, 183, 191, 192, 178, 183, 192, 175, 180, 165, 180, 180, 178, 182, 181, 192, 186, 186, 170, 183, 186,
 185, 178, 189, 189, 181, 175, 172, 187, 185, 175, 180, 178, 191, 180, 188, 193, 169, 180, 170, 185, 185, 188, 180, 175,
 180, 183, 175, 177, 174, 182, 184, 180, 184, 180, 178, 183, 184, 193, 175, 174, 175, 188, 183, 185, 178, 188, 175, 172,
 185, 186, 186, 182, 177, 185, 176, 175, 180, 172, 175, 182, 186, 176, 182, 175, 183, 180, 184, 190, 188, 186, 185, 172,
 175, 172, 172, 182, 174, 188, 190, 194, 168, 185, 188, 183, 185, 185, 178, 171, 173, 180, 200, 178, 178, 164, 182, 186,
 195, 191, 186, 185, 173, 180, 185, 177, 178, 180, 184, 186, 183, 186, 183, 174, 178, 181, 183, 185, 174, 184, 192, 181,
 174, 186, 191, 180, 188, 188, 188, 182, 193, 193, 179, 183, 182, 182, 183, 184, 184, 185, 168, 175, 185, 173, 181, 184,
 186, 191, 179, 181, 183, 181, 196, 184, 186, 184, 181, 188, 180, 186, 180, 183, 184, 189, 182, 185, 183, 186, 193, 188,
 188, 188, 180, 193, 186, 185, 185, 183, 180, 198, 178, 178, 185, 180, 182, 182, 185, 173, 180, 185, 191, 175, 180, 174,
 183, 183, 181, 190, 169, 170, 182, 172, 180, 182, 186, 183, 191, 185, 185, 178, 188, 187, 175, 180, 198, 190, 192, 183,
 190, 181, 170, 189, 186, 188, 178, 186, 180, 175, 180, 163, 182, 177, 183, 177, 172, 173, 165, 172, 173, 177, 184, 183,
 179, 174, 170, 192, 188, 191, 191, 185, 191, 175, 185, 185, 178, 165, 163, 180, 178, 180, 175, 179, 176, 183, 186, 180,
 187, 171, 170, 177, 185, 176, 182, 176, 180, 170, 183, 183, 180, 192, 178, 178, 180, 180, 165, 168, 192, 178, 185, 179,
 181, 193, 186, 175, 175, 191, 190, 175, 172, 176, 189, 184, 166, 180, 183, 193, 187, 175, 190, 184, 184, 177, 178, 176,
 171, 183, 184, 176, 189, 180, 181, 170, 187, 185, 173, 183, 180, 172, 178, 183, 180, 180, 187, 178, 179, 187, 179, 181,
 182, 182, 187, 180, 190, 178, 174, 190, 173, 185, 173, 189, 193, 184, 185, 171, 192, 177, 180, 174, 179, 180, 172, 196,
 175, 185, 178, 175, 186, 178, 185, 188, 182, 188, 183, 189, 185, 193, 190, 177, 193, 184, 176, 181, 192, 185, 174, 193,
 176, 185, 188, 179, 187, 192, 183, 188, 178, 185, 178, 169, 184, 193, 173, 185, 177, 178, 185, 186, 183, 182, 183, 178,
 183, 165, 178, 177, 182, 180, 190, 179, 177, 184, 183, 183, 177, 179, 188, 186, 187, 175, 186, 182, 182, 189, 184, 176,
 180, 172, 189, 174, 185, 190, 186, 177, 183, 180, 178, 191, 185, 178, 189, 189, 190, 185, 187, 185, 178, 176, 176, 173,
 176, 188, 178, 193, 181, 197, 180, 186, 178, 184, 187, 184, 190, 185, 190, 187, 180, 184, 171, 196, 185, 176, 186, 193,
 173, 178, 183, 168, 186, 184, 189, 177, 170, 189, 188, 176, 183, 178, 183, 173, 180, 181, 178, 179, 190, 177, 187, 174,
 184, 179, 188, 190, 190, 176, 187, 173, 180, 168, 170, 188, 184, 180, 185, 176, 179, 180, 176, 185, 175, 170, 170, 180,
 187, 172, 178, 182, 180, 181, 180, 180, 200, 186, 178, 186, 191, 176, 178, 183, 184, 175, 181, 165, 173, 171, 180, 178,
 175, 185, 180, 177, 190, 178, 191, 185, 188, 173, 183, 184, 176, 177, 184, 178, 183, 180, 187, 182, 172, 166, 185, 185,
 180, 197, 181, 188, 181, 178, 183, 176, 185, 178, 190, 178, 196, 188, 187, 183, 172, 183, 198, 186, 191, 184, 189, 178,
 182, 182, 178, 180, 169, 177, 172, 175, 178, 187, 187, 185, 187, 173, 188, 176, 170, 185, 184, 173, 185, 180, 187, 180,
 190, 180, 183, 176, 167, 171, 185, 175, 182, 186, 178, 172, 177, 175, 181, 185, 189, 182, 182, 182, 178, 185, 183, 188,
 177, 178, 192, 182, 195, 183, 180, 177, 180, 178, 178, 182, 188, 182, 188, 188, 178, 178, 183, 175, 183, 179, 178, 191,
 197, 180, 178, 188, 187, 185, 188, 187, 184, 183, 171, 184, 188, 185, 175, 191, 185, 183, 173, 180, 191, 183, 186, 180,
 183, 193, 176, 185, 188, 188, 191, 185, 184, 176, 188, 187, 176, 193, 181, 177, 183, 184, 181, 185, 183, 192, 185, 175,
 180, 183, 182, 173, 196, 180, 188, 185, 194, 172, 175, 178, 182, 193, 188, 178, 178, 178, 180, 189, 177, 186, 185, 183,
 186, 176, 185, 183, 175, 178, 187, 190, 190, 184, 187, 173, 185, 173, 193, 188, 183, 185, 174, 183, 175, 180, 186, 180,
 185, 178, 188, 178, 186, 188, 180, 183, 192, 185, 188, 180, 183, 185, 183, 188, 180, 174, 175, 178, 185, 180, 188, 180,
 180, 185, 185, 173, 180, 183, 174, 186, 183, 180, 188, 176, 184, 180, 188, 176, 188, 173, 188, 180, 180, 178, 186, 187,
 188, 176, 182, 189, 187, 184, 188, 180, 197, 178, 174, 180, 175, 170, 180, 183, 185, 180, 185, 179, 183, 185, 193, 188,
 175, 190, 180, 170, 175, 185, 170, 187, 180, 179, 165, 184, 184, 183, 186, 174, 170, 180, 185, 172, 175, 175, 175, 173,
 185, 173, 185, 188, 188, 185, 180, 173, 183, 181, 174, 187, 179, 194, 183, 170, 170, 173, 180, 187, 187, 187, 185, 185,
 182, 170, 186, 178, 187, 180, 179, 178, 180, 180, 171, 188, 180, 186, 185, 178, 188, 187, 180, 175, 170, 183, 179, 186,
 191, 172, 193, 191, 186, 175, 187, 182, 181, 169, 188, 186, 183, 183, 180, 184, 183, 171, 183, 183, 174, 191, 193, 183,
 178, 167, 178, 183, 173, 180, 163, 188, 181, 188, 188, 188, 184, 191, 178, 175, 193, 185, 165, 175, 183, 191, 183, 185,
 183, 185, 180, 178, 180, 174, 180, 180, 191, 178, 185, 183, 178, 178, 183, 188, 183, 183, 180, 168, 183, 183, 191, 183,
 185, 182, 185, 173, 188, 178, 175, 188, 190, 182, 174, 175, 176, 188, 183, 185, 180, 182, 194, 175, 185, 176, 180, 192,
 184, 183, 173, 189, 190, 187, 179, 171, 185, 178, 189, 175, 181, 196, 176, 177, 184, 183, 184, 187, 188, 183, 183, 175,
 196, 188, 183, 185, 192, 191, 183, 185, 177, 174, 176, 182, 183, 181, 177, 176, 187, 180, 182, 168, 180, 183, 173, 185,
 178, 172, 178, 183, 180, 174, 185, 183, 174, 186, 183, 184, 178, 184, 188, 180, 162, 183, 183, 170, 177, 190, 175, 183,
 179, 175, 188, 176, 180, 188, 180, 190, 180, 175, 191, 196, 185, 175, 167, 186, 167, 185, 186, 186, 168, 165, 179, 170,
 189, 175, 184, 169, 186, 182, 175, 186, 172, 181, 177, 186, 176, 193, 175, 189, 180, 170, 184, 169, 178, 173, 186, 192,
 173, 184, 185, 188, 180, 175, 190, 175, 181, 166, 191, 174, 180, 185, 193, 180, 183, 176, 180, 178, 193, 185, 175, 185,
 190, 185, 188, 185, 188, 182, 176, 193, 180, 182, 183, 184, 185, 187, 185, 172, 188, 180, 174, 176, 181, 180, 179, 171,
 184, 187, 193, 193, 187, 183, 180, 184, 202, 182, 176, 175, 176, 180, 180, 185, 177, 185, 167, 178, 184, 183, 181, 190,
 184, 180, 180, 183, 178, 176, 187, 171, 185, 189, 193, 184, 174, 187, 192, 180, 178, 175, 188, 175, 177, 188, 185, 180,
 192, 182, 178, 185, 173, 180, 178, 170, 193, 178, 176, 181, 178, 180, 178, 178, 188, 178, 183, 188, 175, 180, 188, 189,
 195, 176, 178, 173, 182, 187, 183, 176, 187, 191, 180, 185, 189, 180, 186, 182, 188, 191, 195, 186, 191, 186, 177, 179,
 185, 179, 192, 180, 186, 171, 178, 178, 181, 175, 182, 185, 190, 183, 193, 182, 178, 179, 172, 185, 176, 183, 175, 185,
 184, 176, 180, 186, 185, 172, 186, 173, 184, 191, 196, 188, 188, 182, 186, 184, 176, 185, 178, 184, 181, 180, 180, 174,
 183, 182, 173, 175, 178, 185, 175, 190, 180, 188, 178, 182, 175, 170, 181, 186, 170, 169, 177, 180, 183, 178, 177, 172,
 175, 189, 180, 182, 179, 178, 188, 197, 168, 180, 187, 173, 180, 178, 175, 183, 198, 191, 191, 169, 179, 173, 178, 174,
 182, 176, 186, 178, 175, 174, 180, 185, 185, 177, 183, 187, 185, 183, 185, 178, 188, 189, 191, 178, 178, 185, 193, 178,
 180, 175, 178, 183, 172, 188, 183, 183, 185, 173, 191, 183, 174, 180, 178, 185, 185, 184, 184, 198, 178, 175, 180, 180,
 175, 178, 183, 186, 185, 180, 178, 179, 183, 194, 171, 183, 181, 192, 191, 176, 178, 183, 172, 174, 185, 176, 188, 193,
 175, 185, 180, 193, 191, 173, 175, 175, 181, 184, 176, 175, 185, 173, 193, 180, 180, 185, 185, 191, 180, 178, 178, 183,
 174, 180, 185, 175, 196, 188, 186, 180, 176, 188, 175, 185, 185, 178, 191, 185, 178, 178, 183, 175, 175, 185, 186, 181,
 185, 191, 186, 176, 178, 183, 171, 172, 190, 183, 184, 175, 185, 182, 188, 183, 187, 188, 181, 178, 174, 172, 178, 173,
 185, 187, 188, 174, 179, 185, 185, 175, 183, 178, 161, 172, 179, 187, 177, 184, 185, 168, 180, 178, 185, 179, 172, 185,
 190, 184, 174, 185, 193, 185, 175, 176, 173, 175, 181, 178, 185, 183, 170, 187, 182, 182, 185, 184, 189, 188, 178, 196,
 186, 183, 179, 169, 181, 186, 187, 158, 188, 180, 174, 178, 185, 178, 191, 180, 180, 173, 173, 173, 175, 173, 173, 171,
 169, 177, 178, 190, 181, 182, 180, 180, 190, 189, 181, 177, 183, 191, 181, 180, 185, 170, 185, 178, 187, 179, 172, 185,
 183, 170, 187, 175, 193, 192, 184, 188, 183, 183, 178, 178, 173, 186, 169, 188, 191, 198, 190, 178, 183, 178, 183, 179,
 183, 187, 181, 178, 181, 180, 178, 174, 167, 180, 170, 183, 177, 178, 187, 176, 186, 177, 191, 178, 175, 169, 188, 168,
 180, 179, 182, 180, 181, 171, 178, 176, 186, 178, 180, 178, 191, 186, 183, 179, 201, 188, 178, 176, 190, 177, 181, 180,
 188, 188, 186, 188, 189, 184, 188, 177, 176, 182, 188, 178, 170, 185, 190, 190, 187, 183, 176, 176, 181, 185, 173, 184,
 176, 180, 177, 184, 179, 182, 183, 181, 185, 190, 181, 172, 196, 184, 190, 178, 183, 183, 190, 185, 180, 183, 181, 188,
 185, 180, 170, 188, 186, 178, 180, 175, 182, 176, 189, 183, 174, 182, 192, 188, 180, 189, 193, 188, 188, 185, 173, 188,
 183, 187, 180, 188, 179, 173, 183, 178, 173, 190, 170, 181, 186, 180, 178, 178, 183, 180, 175, 183, 180, 181, 181, 180,
 187, 185, 188, 184, 183, 179, 177, 184, 180, 184, 188, 170, 178, 175, 188, 175, 183, 175, 192, 186, 185, 192, 193, 182,
 175, 165, 188, 182, 165, 172, 172, 185, 178, 183, 180, 187, 183, 193, 191, 182, 191, 181, 180, 176, 187, 167, 178, 186,
 185, 188, 182, 178, 175, 170, 170, 178, 184, 168, 183, 187, 183, 188, 175, 180, 175, 183, 184, 180, 188, 180, 188, 183,
 178, 193, 180, 186, 192, 180, 180, 175, 194, 170, 173, 178, 183, 185, 191, 176, 180, 185, 185, 193, 187, 177, 176, 180,
 184, 178, 184, 176, 172, 178, 175, 170, 175, 187, 171, 175, 181, 180, 178, 178, 171, 185, 180, 188, 170, 184, 180, 175,
 183, 178, 181, 172, 181, 174, 173, 182, 175, 196, 187, 185, 178, 173, 185, 178, 188, 192, 179, 177, 177, 185, 186, 188,
 186, 182, 169, 176, 188, 189, 175, 186, 173, 174, 176, 180, 179, 178, 188, 172, 175, 190, 185, 188, 186, 183, 180, 190,
 185, 185, 175, 184, 175, 178, 188, 178, 195, 192, 184, 184, 181, 185, 177, 178, 188, 173, 180, 183, 183, 183, 178, 188,
 180, 185, 186, 175, 183, 192, 190, 188, 179, 185, 190, 171, 182, 175, 180, 185, 180, 180, 185, 177, 168, 168, 190, 175,
 188, 182, 178, 183, 183, 173, 187, 182, 173, 186, 185, 188, 178, 178, 176, 180, 181, 185, 166, 189, 182, 179, 184, 173,
 174, 178, 185, 182, 169, 183, 192, 180, 179, 180, 183, 181, 168, 185, 182, 188, 172, 183, 191, 180, 176, 173, 181, 183,
 181, 179, 194, 172, 174, 173, 183, 181, 185, 181, 168, 181, 180, 193, 188, 172, 187, 180, 191, 175, 182, 172, 186, 186,
 184, 174, 189, 172, 185, 185, 181, 185, 173, 185, 190, 191, 180, 179, 193, 169, 185, 188, 180, 178, 170, 183, 172, 174,
 175, 187, 178, 189, 194, 170, 188, 179, 194, 187, 183, 183, 191, 170, 183, 173, 175, 185, 178, 180, 189, 168, 172, 184,
 192, 174, 184, 177, 176, 179, 187, 182, 188, 184, 189, 168, 183, 178, 180, 180, 176, 174, 189, 179, 183, 186, 183, 173,
 175, 183, 173, 187, 171, 178, 190, 183, 175, 191, 180, 178, 190, 167, 171, 181, 184, 173, 185, 182, 185, 175, 173, 184,
 166, 181, 192, 174, 178, 178, 189, 184, 193, 183, 186, 191, 180, 183, 180, 189, 184, 185, 172, 183, 180, 185, 176, 170,
 188, 187, 184, 184, 183, 185, 190, 182, 186, 190, 180, 182, 180, 183, 185, 191, 189, 178, 188, 180, 183, 173, 174, 173,
 169, 178, 173, 185, 180, 186, 190, 194, 178, 193, 179, 185, 178, 184, 188, 175, 166, 179, 178, 175, 190, 183, 174, 172,
 172, 187, 172, 180, 182, 193, 199, 192, 192, 167, 184, 185, 190, 184, 183, 189, 183, 183, 182, 168, 173, 184, 168, 183,
 183, 179, 187, 180, 189, 185, 178, 176, 179, 182, 178, 188, 187, 182, 183, 191, 179, 190, 169, 186, 172, 186, 186, 185,
 192, 186, 193, 174, 184, 187, 180, 180, 182, 172, 176, 183, 185, 179, 176, 182, 187, 184, 188, 184, 181, 190, 185, 180,
 182, 183, 184, 190, 186, 176, 182, 182, 170, 186, 168, 178, 183, 198, 189, 182, 192, 165, 179, 190, 178, 170, 177, 171,
 186, 183, 185, 186, 185, 187, 183, 190, 184, 181, 182, 185, 183, 184, 182, 188, 185, 184, 192, 191, 183, 173, 163, 183,
 170, 180, 186, 189, 176, 183, 174, 183, 178, 175, 175, 183, 175, 178, 184, 192, 183, 170, 186, 178, 186, 180, 178, 190,
 180, 180, 191, 176, 180, 170, 181, 180, 189, 188, 180, 196, 202, 195, 180, 187, 190, 178, 178, 191, 186, 175, 180, 184,
 185, 186, 174, 172, 176, 191, 178, 183, 178, 184, 168, 192, 177, 177, 184, 175, 180, 179, 182, 184, 173, 180, 180, 178,
 174, 186, 184, 188, 181, 173, 183, 175, 192, 183, 183, 183, 183, 196, 172, 191, 192, 170, 178, 187, 188, 185, 176, 184,
 189, 180, 194, 177, 168, 184, 174, 188, 180, 184, 184, 188, 180, 185, 180, 177, 170, 194, 202, 176, 180, 170, 175, 170,
 175, 188, 174, 173, 186, 178, 185, 180, 180, 174, 186, 183, 183, 177, 183, 183, 180, 180, 172, 189, 180, 178, 180, 180,
 183, 187, 182, 188, 193, 183, 179, 178, 180, 179, 182, 183, 178, 176, 170, 188, 178, 185, 180, 188, 185, 192, 183, 193,
 181, 175, 185, 178, 194, 187, 178, 188, 170, 170, 180, 184, 185, 175, 180, 186, 189, 195, 188, 168, 183, 193, 183, 185,
 188, 183, 186, 186, 174, 175, 180, 184, 175, 175, 175, 184, 170, 180, 176, 187, 193, 184, 183, 189, 191, 178, 185, 180,
 180, 191, 183, 178, 193, 178, 184, 179, 173, 188, 180, 178, 187, 179, 187, 178, 183, 175, 187, 171, 188, 171, 183, 187,
 188, 176, 169, 174, 191, 177, 168, 184, 183, 191, 191, 179, 170, 177, 191, 180, 186, 196, 171, 178, 185, 186, 180, 181,
 187, 179, 175, 172, 188, 191, 197, 193, 165, 186, 195, 186, 181, 186, 185, 182, 175, 180, 174, 180, 180, 185, 185, 173,
 178, 174, 193, 181, 172, 193, 187, 186, 168, 178, 183, 178, 169, 182, 176, 174, 179, 181, 179, 183, 188, 185, 193, 185,
 181, 185, 183, 183, 175, 181, 172, 181, 178, 172, 184, 188, 186, 175, 178, 160, 184, 174, 178, 191, 176, 188, 171, 177,
 181, 189, 175, 181, 183, 174, 186, 187, 181, 188, 187, 186, 173, 177, 187, 179, 188, 170, 178, 185, 175, 191, 185, 183,
 173, 175, 182, 184, 185, 180, 183, 188, 171, 176, 180, 186, 178, 188, 186, 186, 193, 185, 181, 178, 183, 177, 183, 183,
 176, 180, 183, 185, 172, 186, 177, 188, 168, 190, 188, 176, 195, 178, 181, 179, 187, 180, 179, 182, 184, 187, 180, 170,
 195, 181, 178, 190, 169, 173, 181, 191, 193, 187, 183, 191, 188, 175, 192, 181, 183, 180, 185, 182, 185, 188, 184, 182,
 191, 183, 190, 194, 177, 182, 184, 181, 175, 180, 178, 184, 175, 180, 181, 170, 183, 189, 176, 183, 174, 186, 194, 184,
 181, 187, 181, 180, 181, 184, 191, 180, 175, 185, 168, 176, 180, 173, 176, 179, 182, 173, 181, 188, 186, 174, 183, 175,
 183, 173, 181, 189, 188, 190, 174, 174, 186, 180, 180, 188, 175, 185, 190, 183, 183, 173, 180, 188, 183, 193, 178, 177,
 187, 179, 184, 187, 180, 182, 191, 180, 176, 175, 170, 190, 184, 188, 184, 187, 175, 185, 173, 183, 187, 194, 180, 183,
 175, 186, 184, 180, 183, 181, 173, 183, 190, 190, 182, 188, 173, 183, 190, 173, 183, 180, 184, 188, 188, 187, 183, 184,
 188, 192, 178, 190, 172, 180, 176, 186, 174, 190, 183, 186, 184, 182, 180, 173, 182, 184, 178, 188, 182, 178, 184, 193,
 186, 186, 191, 180, 188, 182, 191, 189, 184, 193, 177, 177, 183, 186, 173, 185, 171, 168, 184, 170, 175, 180, 173, 170,
 188, 185, 190, 179, 193, 178, 182, 180, 190, 189, 183, 181, 186, 188, 189, 188, 187, 193, 191, 186, 168, 183, 182, 192,
 193, 188, 191, 180, 188, 186, 176, 184, 182, 192, 184, 180, 175, 184, 173, 177, 182, 187, 192, 185, 170, 180, 171, 174,
 183, 186, 188, 182, 190, 186, 180, 190, 175, 185, 181, 172, 189, 165, 173, 170, 189, 183, 180, 174, 173, 170, 182, 181,
 160, 176, 178, 163, 179, 174, 191, 176, 171, 180, 173, 190, 193, 186, 183, 181, 178, 167, 179, 178, 180, 183, 182, 171,
 188, 175, 182, 180, 183, 191, 183, 188, 172, 176, 180, 194, 196, 170, 186, 175, 186, 180, 192, 169, 179, 183, 175, 183,
 173, 190, 191, 180, 174, 185, 184, 186, 173, 188, 192, 176, 181, 197, 169, 174, 171, 178, 175, 174, 188, 181, 180, 175,
 193, 186, 184, 175, 180, 171, 188, 180, 178, 171, 192, 194, 180, 183, 175, 180, 183, 185, 176, 185, 170, 185, 186, 183,
 190, 178, 183, 179, 174, 179, 182, 183, 183, 187, 181, 164, 178, 190, 183, 191, 172, 188, 190, 183, 180, 186, 186, 183,
 178, 170, 179, 175, 193, 183, 183, 175, 186, 178, 182, 183, 184, 170, 183, 182, 193, 188, 184, 187, 182, 178, 178, 183,
 183, 183, 188, 194, 182, 174, 185, 175, 185, 193, 182, 187, 180, 175, 182, 187, 168, 173, 178, 191, 168, 180, 172, 178,
 178, 178, 176, 183, 190, 187, 183, 185, 193, 178, 188, 170, 185, 187, 175, 175, 184, 176, 183, 185, 187, 174, 175, 190,
 173, 187, 186, 178, 189, 178, 182, 178, 182, 191, 197, 176, 168, 180, 173, 183, 177, 184, 180, 186, 191, 180, 194, 182,
 180, 182, 177, 178, 187, 184, 190, 185, 175, 175, 178, 184, 188, 184, 180, 187, 186, 193, 186, 195, 184, 191, 183, 168,
 178, 184, 170, 187, 180, 187, 190, 173, 181, 185, 183, 188, 189, 181, 184, 178, 187, 187, 184, 173, 186, 168, 184, 181,
 175, 185, 175, 208, 191, 176, 178, 192, 174, 181, 192, 176, 193, 185, 182, 179, 185, 178, 183, 180, 188, 180, 183, 184,
 191, 171, 183, 178, 178, 177, 183, 178, 174, 175, 178, 185, 175, 172, 185, 185, 188, 180, 195, 180, 194, 180, 170, 183,
 188, 175, 194, 180, 173, 175, 179, 184, 183, 185, 187, 182, 189, 190, 174, 170, 179, 174, 191, 179, 173, 172, 188, 188,
 198, 172, 175, 185, 185, 173, 183, 188, 194, 183, 176, 193, 175, 187, 182, 185, 176, 178, 191, 185, 178, 185, 191, 185,
 181, 178, 180, 182, 183, 177, 185, 175, 175, 185, 185, 183, 191, 184, 187, 180, 175, 180, 179, 167, 180, 180, 182, 188,
 179, 178, 192, 185, 178, 183, 180, 182, 178, 188, 179, 185, 186, 186, 174, 179, 180, 179, 170, 186, 186, 189, 191, 182,
 196, 185, 175, 178, 188, 180, 170, 188, 191, 179, 175, 185, 196, 181, 189, 185, 186, 178, 185, 185, 183, 193, 185, 178,
 177, 174, 188, 193, 183, 183, 180, 186, 180, 185, 183, 168, 187, 191, 172, 178, 185, 185, 193, 175, 191, 165, 179, 169,
 166, 180, 178, 188, 173, 179, 192, 178, 170, 176, 180, 180, 191, 185, 186, 180, 172, 170, 185, 187, 184, 190, 180, 180,
 183, 174, 177, 174, 171, 186, 183, 178, 185, 185, 180, 182, 183, 184, 187, 169, 180, 175, 178, 178, 170, 193, 183, 176,
 185, 188, 182, 177, 183, 191, 185, 183, 189, 177, 183, 194, 176, 171, 179, 186, 188, 165, 181, 186, 180, 183, 185, 184,
 185, 180, 174, 173, 194, 182, 176, 185, 177, 176, 183, 187, 183, 184, 183, 190, 190, 181, 182, 181, 171, 183, 177, 178,
 180, 180, 172, 176, 178, 179, 194, 191, 175, 188, 186, 183, 184, 186, 188, 193, 173, 181, 180, 178, 173, 183, 168, 182,
 190, 188, 180, 177, 182, 180, 195, 196, 176, 182, 196, 174, 173, 182, 176, 175, 186, 180, 173, 180, 190, 176, 182, 182,
 180, 162, 174, 192, 180, 183, 170, 185, 180, 187, 181, 188, 172, 172, 179, 182, 180, 181, 175, 169, 199, 180, 173, 181,
 192, 177, 178, 173, 185, 179, 196, 176, 185, 187, 184, 179, 183, 188, 192, 188, 190, 185, 180, 180, 187, 182, 194, 177,
 180, 183, 168, 186, 173, 197, 182, 179, 183, 194, 176, 181, 165, 186, 180, 186, 178, 187, 171, 180, 178, 177, 183, 179,
 192, 189, 180, 190, 180, 168, 183, 185, 186, 183, 178, 185, 185, 180, 183, 182, 185, 183, 178, 184, 183, 181, 168, 185,
 190, 165, 188, 185, 177, 192, 181, 182, 185, 190, 180, 185, 180, 185, 182, 185, 188, 182, 183, 191, 175, 172, 183, 193,
 178, 183, 186, 186, 176, 187, 181, 179, 183, 179, 179, 186, 178, 183, 184, 176, 181, 185, 178, 178, 180, 188, 190, 182,
 197, 172, 189, 178, 186, 192, 186, 180, 184, 185, 186, 186, 178, 190, 202, 183, 174, 166, 176, 178, 186, 189, 180, 176,
 168, 175, 174, 196, 185, 190, 182, 188, 178, 173, 190, 178, 180, 180, 188, 174, 180, 188, 192, 180, 188, 176, 193, 180,
 183, 187, 184, 170, 190, 173, 183, 175, 187, 182, 185, 178, 188, 170, 183, 177, 190, 173, 179, 169, 183, 191, 180, 183,
 195, 178, 182, 185, 174, 173, 183, 193, 189, 171, 189, 187, 186, 179, 180, 181, 174, 183, 188, 178, 177, 183, 190, 180,
 180, 175, 178, 183, 193, 170, 171, 192, 196, 179, 172, 180, 170, 186, 188, 176, 184, 192, 181, 191, 183, 189, 188, 180,
 186, 177, 186, 172, 183, 185, 178, 173, 187, 180, 177, 173, 172, 185, 177, 172, 175, 187, 172, 188, 174, 177, 173, 176,
 189, 167, 175, 169, 174, 178, 172, 176, 189, 180, 182, 177, 170, 173, 187, 178, 181, 187, 190, 186, 187, 187, 169, 185,
 196, 188, 180, 186, 195, 181, 186, 180, 170, 183, 180, 193, 181, 189, 189, 184, 184, 179, 176, 172, 172, 180, 177, 176,
 178, 190, 183, 183, 177, 188, 190, 186, 196, 186, 187, 192, 186, 180, 179, 175, 186, 176, 185, 185, 185, 181, 184, 180,
 195, 183, 179, 186, 188, 188, 183, 188, 183, 175, 180, 175, 181, 181, 193, 175, 185, 175, 180, 177, 178, 172, 179, 174,
 180, 176, 170, 192, 176, 177, 185, 180, 189, 188, 188, 183, 179, 189, 187, 179, 181, 180, 183, 201, 178, 180, 184, 175,
 176, 198, 190, 179, 181, 177, 178, 185, 187, 185, 180, 171, 188, 177, 176, 184, 185, 191, 192, 175, 185, 172, 183, 172,
 173, 182, 180, 189, 185, 183, 185, 192, 188, 183, 184, 173, 177, 176, 174, 178, 183, 192, 174, 191, 173, 173, 180, 174,
 174, 176, 188, 188, 188, 173, 185, 180, 191, 193, 185, 186, 182, 177, 178, 178, 178, 181, 188, 175, 177, 186, 180, 178,
 170, 186, 191, 174, 177, 183, 182, 183, 185, 180, 185, 175, 172, 184, 177, 187, 181, 167, 182, 182, 190, 187, 185, 183,
 178, 187, 178, 188, 196, 175, 183, 175, 175, 173, 180, 180, 185, 191, 179, 176, 182, 180, 175, 180, 180, 180, 181, 179,
 182, 178, 183, 173, 180, 180, 180, 190, 185, 197, 174, 187, 171, 186, 183, 183, 176, 183, 186, 180, 177, 173, 185, 177,
 175, 180, 193, 179, 178, 180, 177, 183, 193, 192, 180, 175, 195, 184, 180, 181, 183, 189, 176, 190, 187, 180, 188, 185,
 183, 178, 180, 188, 179, 188, 181, 198, 191, 193, 180, 180, 173, 186, 193, 173, 180, 170, 188, 180, 177, 186, 176, 178,
 175, 190, 188, 180, 173, 188, 179, 185, 187, 173, 180, 171, 173, 176, 174, 183, 178, 179, 186, 184, 175, 184, 174, 188,
 185, 184, 186, 191, 185, 178, 182, 186, 185, 185, 178, 193, 183, 182, 185, 185, 196, 180, 178, 191, 187, 177, 170, 190,
 181, 188, 194, 180, 175, 181, 188, 178, 192, 178, 185, 190, 183, 172, 181, 192, 190, 182, 185, 188, 181, 185, 168, 180,
 176, 180, 174, 178, 179, 187, 183, 180, 184, 173, 183, 177, 172, 171, 186, 190, 187, 191, 187, 189, 177, 182, 187, 178,
 184, 173, 188, 184, 175, 170, 186, 184, 189, 195, 182, 175, 175, 186, 174, 178, 174, 196, 192, 176, 182, 182, 194, 175,
 175, 182, 184, 177, 178, 177, 182, 175, 185, 170, 185, 173, 188, 185, 173, 179, 177, 183, 178, 182, 185, 197, 191, 173,
 171, 183, 181, 180, 181, 178, 189, 180, 172, 184, 188, 173, 183, 174, 190, 187, 182, 178, 174, 165, 187, 176, 176, 183,
 188, 175, 183, 182, 186, 180, 183, 192, 185, 168, 184, 174, 176, 184, 186, 193, 185, 180, 174, 191, 190, 189, 190, 183,
 177, 183, 183, 186, 180, 185, 185, 170, 176, 186, 175, 191, 173, 173, 176, 185, 176, 175, 183, 175, 189, 184, 181, 183,
 175, 184, 190, 179, 178, 192, 184, 173, 180, 188, 188, 190, 179, 177, 190, 182, 203, 190, 183, 180, 189, 194, 180, 184,
 185, 180, 187, 194, 173, 187, 173, 180, 185, 190, 179, 178, 194, 186, 180, 186, 176, 195, 182, 170, 163, 175, 178, 176,
 181, 178, 178, 180, 185, 179, 192, 190, 177, 185, 175, 178, 176, 175, 172, 187, 190, 167, 193, 183, 173, 183, 175, 196,
 180, 172, 187, 182, 180, 175, 171, 190, 180, 184, 177, 191, 186, 183, 185, 181, 192, 176, 166, 187, 180, 174, 181, 194,
 176, 184, 187, 183, 183, 184, 180, 191, 178, 172, 174, 185, 178, 185, 172, 181, 183, 170, 175, 189, 191, 180, 176, 177,
 184, 173, 178, 175, 194, 196, 184, 180, 181, 188, 180, 187, 175, 176, 179, 189, 177, 181, 177, 179, 193, 196, 187, 183,
 179, 183, 182, 173, 188, 188, 175, 191, 185, 186, 187, 174, 188, 184, 182, 193, 175, 191, 185, 183, 185, 192, 177, 181,
 182, 189, 184, 183, 169, 173, 197, 182, 178, 181, 185, 185, 173, 175, 181, 178, 179, 170, 180, 182, 169, 185, 185, 173,
 174, 186, 178, 190, 178, 194, 180, 180, 189, 172, 171, 173, 186, 178, 178, 190, 175, 178, 179, 185, 191, 172, 179, 178,
 172, 184, 183, 178, 178, 178, 186, 178, 185, 188, 186, 187, 188, 181, 193, 184, 187, 181, 181, 174, 175, 178, 178, 193,
 173, 188, 176, 178, 173, 178, 185, 178, 178, 175, 180, 169, 192, 181, 176, 193, 185, 176, 185, 176, 180, 179, 187, 184,
 178, 170, 175, 178, 178, 185, 180, 175, 185, 176, 175, 179, 177, 175, 180, 185, 191, 181, 171, 188, 188, 196, 187, 185,
 192, 169, 190, 196, 179, 182, 180, 192, 186, 180, 191, 179, 169, 167, 183, 175, 180, 193, 191, 187, 190, 180, 191, 188,
 181, 177, 173, 170, 184, 185, 175, 194, 180, 174, 180, 190, 191, 170, 182, 185, 174, 191, 181, 180, 188, 183, 183, 183,
 167, 191, 170, 191, 191, 180, 181, 165, 176, 191, 191, 170, 190, 185, 183, 186, 176, 181, 188, 170, 178, 178, 188, 188,
 183, 175, 175, 187, 191, 173, 184, 183, 191, 194, 184, 176, 180, 175, 181, 182, 178, 170, 183, 177, 191, 191, 176, 177,
 178, 181, 183, 173, 188, 173, 180, 191, 175, 185, 175, 188, 193, 176, 186, 178, 185, 183, 194, 183, 184, 188, 188, 180,
 188, 182, 188, 185, 168, 176, 196, 178, 185, 185, 172, 183, 188, 181, 184, 188, 183, 171, 184, 183, 193, 188, 168, 183,
 181, 178, 182, 178, 180, 188, 191, 168, 185, 190, 175, 181, 182, 180, 177, 181, 163, 183, 182, 180, 178, 178, 178, 171,
 182, 180, 193, 180, 178, 177, 175, 183, 193, 188, 180, 185, 190, 193, 190, 166, 182, 178, 167, 176, 173, 175, 185, 177,
 178, 186, 173, 180, 183, 191, 187, 183, 180, 183, 181, 177, 177, 190, 180, 185, 186, 187, 196, 189, 173, 185, 183, 175,
 188, 193, 180, 185, 170, 178, 182, 188, 175, 172, 183, 175, 181, 178, 182, 183, 175, 187, 170, 188, 178, 182, 188, 167,
 188, 185, 187, 184, 183, 180, 191, 183, 175, 182, 191, 178, 172, 185, 180, 190, 191, 180, 175, 173, 178, 185, 188, 179,
 177, 185, 193, 180, 183, 185, 188, 190, 187, 179, 189, 178, 182, 189, 184, 186, 178, 192, 184, 175, 187, 185, 180, 177,
 185, 183, 185, 175, 187, 188, 184, 183, 179, 182, 193, 189, 183, 180, 194, 187, 165, 177, 180, 190, 174, 178, 178, 185,
 185, 194, 185, 191, 193, 173, 185, 180, 178, 185, 188, 186, 180, 180, 180, 180, 190, 179, 179, 192, 197, 183, 168, 180,
 180, 188, 179, 178, 180, 183, 178, 185, 177, 185, 180, 179, 190, 180, 183, 192, 189, 178, 178, 174, 170, 176, 170, 195,
 178, 187, 178, 183, 167, 178, 178, 170, 180, 180, 180, 185, 175, 183, 180, 173, 185, 180, 175, 185, 178, 175, 184, 184,
 179, 174, 189, 176, 184, 180, 182, 188, 180, 173, 186, 179, 188, 184, 180, 178, 178, 181, 185, 182, 180, 180, 188, 172,
 183, 191, 181, 178, 191, 191, 178, 173, 188, 179, 180, 193, 179, 185, 178, 179, 183, 168, 183, 184, 180, 203, 173, 180,
 170, 193, 175, 175, 178, 191, 174, 188, 167, 173, 183, 184, 183, 187, 177, 176, 184, 185, 184, 180, 181, 193, 175, 177,
 184, 185, 189, 179, 182, 173, 165, 184, 191, 175, 185, 187, 170, 184, 178, 174, 179, 178, 181, 194, 179, 185, 180, 178,
 184, 178, 188, 176, 191, 174, 180, 180, 182, 180, 192, 188, 172, 168, 177, 165, 194, 174, 181, 177, 174, 180, 177, 191,
 179, 194, 185, 176, 194, 187, 187, 173, 188, 178, 185, 180, 177, 176, 185, 182, 182, 185, 169, 179, 179, 182, 176, 172,
 171, 190, 175, 178, 190, 180, 191, 179, 187, 189, 180, 188, 178, 187, 181, 189, 185, 178, 190, 189, 175, 185, 176, 180,
 185, 186, 188, 198, 182, 192, 182, 190, 182, 189, 191, 183, 192, 181, 180, 178, 181, 191, 182, 178, 173, 192, 188, 180,
 175, 187, 187, 182, 185, 182, 185, 180, 189, 177, 182, 172, 184, 174, 184, 168, 175, 180, 183, 175, 174, 185, 185, 195,
 178, 180, 180, 182, 179, 172, 187, 181, 165, 177, 198, 180, 179, 174, 180, 183, 191, 196, 182, 180, 185, 181, 178, 176,
 179, 191, 188, 176, 175, 178, 190, 192, 185, 180, 174, 175, 175, 178, 181, 193, 173, 185, 170, 190, 189, 182, 180, 180,
 175, 180, 179, 185, 182, 179, 182, 185, 174, 177, 173, 186, 182, 191, 171, 183, 192, 185, 184, 180, 183, 178, 170, 183,
 185, 190, 179, 191, 173, 182, 191, 171, 186, 173, 175, 183, 187, 180, 178, 197, 187, 171, 179, 186, 178, 180, 175, 177,
 176, 183, 183, 173, 180, 170, 178, 170, 176, 189, 185, 180, 180, 178, 176, 175, 180, 183, 170, 178, 180, 184, 181, 178,
 180, 177, 178, 178, 176, 179, 188, 184, 185, 179, 190, 170, 190, 187, 183, 185, 185, 187, 177, 185, 175, 179, 181, 180,
 176, 162, 179, 193, 185, 176, 178, 183, 177, 182, 177, 182, 174, 175, 180, 184, 178, 188, 180, 183, 185, 182, 177, 176,
 183, 187, 197, 187, 180, 182, 182, 182, 186, 185, 172, 174, 181, 186, 189, 175, 178, 193, 180, 174, 182, 180, 193, 180,
 181, 173, 188, 187, 174, 171, 180, 178, 180, 179, 191, 183, 185, 178, 183, 178, 191, 181, 184, 172, 187, 180, 180, 190,
 184, 188, 188, 188, 183, 179, 182, 176, 178, 173, 185, 185, 189, 178, 188, 178, 176, 181, 167, 180, 185, 180, 183, 189,
 194, 185, 190, 185, 179, 178, 173, 177, 180, 178, 175, 183, 170, 179, 186, 188, 186, 175, 179, 177, 186, 176, 173, 183,
 178, 178, 186, 180, 185, 173, 171, 172, 188, 183, 182, 187, 176, 173, 185, 180, 183, 170, 180, 193, 175, 174, 177, 188,
 180, 182, 186, 187, 186, 180, 184, 190, 165, 193, 189, 180, 175, 188, 180, 169, 183, 173, 183, 179, 189, 182, 186, 179,
 182, 179, 181, 182, 181, 175, 190, 184, 183, 183, 186, 186, 173, 180, 188, 175, 181, 179, 183, 186, 173, 168, 184, 183,
 178, 193, 178, 177, 189, 178, 176, 182, 174, 180, 179, 180, 183, 173, 183, 185, 185, 188, 188, 173, 160, 174, 182, 178,
 183, 178, 183, 193, 188, 175, 196, 175, 185, 185, 183, 185, 183, 180, 165, 175, 183, 183, 183, 178, 180, 178, 173, 179,
 186, 187, 185, 175, 173, 175, 191, 188, 195, 191, 185, 187, 178, 176, 184, 185, 177, 175, 170, 175, 181, 194, 186, 175,
 174, 176, 188, 174, 173, 191, 182, 176, 173, 190, 181, 173, 188, 170, 194, 178, 177, 181, 186, 180, 191, 179, 178, 180,
 178, 175, 181, 170, 182, 184, 182, 180, 175, 178, 168, 175, 188, 183, 184, 188, 185, 185, 190, 172, 183, 168, 180, 185,
 173, 184, 172, 164, 185, 183, 191, 181, 175, 191, 178, 180, 180, 180, 175, 182, 185, 191, 175, 185, 183, 176, 173, 182,
 183, 179, 192, 183, 182, 199, 188, 185, 196, 185, 178, 183, 188, 187, 183, 184, 184, 185, 188, 177, 180, 194, 187, 175,
 191, 186, 178, 178, 191, 185, 180, 173, 179, 170, 183, 196, 180, 193, 188, 178, 173, 178, 179, 181, 178, 179, 176, 181,
 194, 177, 184, 184, 179, 178, 180, 185, 178, 188, 174, 187, 177, 179, 170, 181, 186, 176, 180, 177, 190, 185, 180, 179,
 189, 185, 175, 182, 184, 180, 182, 180, 187, 184, 187, 177, 194, 186, 176, 179, 184, 170, 185, 175, 177, 178, 182, 174,
 180, 188, 175, 189, 180, 188, 183, 191, 172, 183, 189, 179, 188, 171, 180, 193, 183, 176, 182, 170, 183, 182, 178, 183,
 179, 179, 178, 178, 188, 186, 175, 193, 178, 180, 176, 180, 186, 170, 169, 180, 179, 178, 180, 186, 178, 180, 178, 185,
 178, 188, 193, 180, 178, 189, 180, 175, 192, 191, 183, 185, 180, 182, 183, 189, 176, 178, 183, 188, 170, 182, 183, 171,
 171, 180, 178, 178, 176, 174, 187, 180, 187, 175, 188, 184, 194, 175, 173, 193, 176, 174, 197, 191, 173, 177, 175, 182,
 181, 179, 189, 176, 172, 175, 186, 170, 178, 181, 180, 185, 178, 185, 185, 192, 187, 185, 185, 180, 182, 185, 180, 177,
 190, 179, 190, 192, 183, 179, 183, 193, 193, 187, 178, 183, 168, 182, 186, 177, 189, 175, 183, 172, 168, 180, 193, 193,
 193, 180, 181, 193, 175, 171, 183, 178, 183, 184, 178, 180, 180, 180, 180, 178, 177, 189, 175, 180, 183, 186, 178, 191,
 184, 190, 181, 177, 178, 172, 189, 193, 187, 193, 181, 185, 193, 183, 192, 175, 171, 190, 169, 181, 188, 187, 188, 183,
 182, 179, 178, 170, 190, 199, 180, 190, 186, 183, 190, 181, 180, 175, 177, 190, 178, 181, 182, 178, 191, 184, 181, 187,
 174, 178, 183, 184, 180, 185, 185, 199, 173, 180, 180, 172, 183, 175, 175, 181, 184, 182, 182, 184, 174, 180, 178, 186,
 187, 180, 183, 185, 183, 193, 185, 179, 197, 185, 171, 188, 183, 187, 188, 175, 186, 188, 188, 165, 184, 180, 191, 194,
 182, 169, 191, 176, 183, 173, 182, 184, 191, 173, 173, 180, 171, 174, 170, 191, 186, 190, 188, 180, 186, 182, 173, 180,
 175, 190, 183, 180, 195, 175, 182, 186, 172, 189, 170, 182, 185, 182, 170, 192, 175, 183, 187, 190, 175, 178, 191, 170,
 180, 183, 174, 186, 186, 185, 180, 180, 175, 182, 193, 177, 176, 178, 180, 170, 190, 183, 178, 185, 177, 180, 180, 190,
 185, 193, 180, 195, 182, 187, 189, 176, 179, 178, 180, 194, 194, 183, 171, 185, 189, 185, 183, 190, 181, 186, 175, 185,
 179, 178, 181, 182, 188, 176, 182, 175, 188, 188, 178, 196, 173, 180, 190, 166, 176, 180, 185, 188, 174, 185, 189, 188,
 176, 181, 190, 175, 180, 178, 188, 178, 178, 181, 189, 185, 178, 175, 183, 188, 186, 173, 191, 185, 195, 184, 175, 198,
 185, 185, 170, 180, 185, 175, 185, 179, 186, 183, 176, 183, 180, 177, 187, 171, 183, 183, 185, 170, 181, 188, 177, 181,
 183, 191, 195, 178, 194, 182, 174, 187, 182, 183, 193, 182, 185, 183, 176, 177, 178, 177, 179, 186, 185, 180, 184, 178,
 180, 178, 185, 183, 185, 178, 188, 178, 187, 187, 178, 170, 180, 181, 192, 173, 183, 183, 180, 185, 183, 175, 183, 187,
 171, 182, 185, 191, 179, 185, 183, 180, 190, 176, 175, 175, 182, 179, 175, 192, 179, 178, 182, 176, 180, 187, 185, 183,
 180, 186, 171, 189, 191, 184, 186, 189, 180, 180, 192, 188, 176, 190, 183, 181, 178, 183, 178, 180, 183, 184, 180, 177,
 193, 172, 191, 180, 184, 190, 178, 178, 182, 193, 184, 194, 180, 182, 186, 183, 166, 177, 190, 185, 187, 190, 178, 196,
 190, 182, 183, 183, 173, 185, 184, 195, 181, 183, 183, 191, 186, 182, 191, 175, 172, 190, 185, 183, 187, 185, 179, 186,
 184, 167, 184, 174, 184, 179, 185, 185, 180, 190, 191, 185, 185, 180, 191, 188, 190, 186, 173, 188, 193, 188, 179, 180,
 175, 186, 187, 186, 183, 175, 181, 179, 190, 169, 184, 196, 183, 190, 189, 194, 186, 170, 175, 180, 181, 187, 184, 187,
 166, 185, 183, 177, 184, 175, 178, 186, 186, 183, 187, 173, 180, 172, 185, 182, 184, 188, 175, 175, 182, 175, 188, 185,
 188, 183, 182, 180, 194, 186, 187, 173, 190, 182, 185, 187, 180, 177, 180, 196, 177, 191, 190, 193, 182, 169, 190, 175,
 182, 193, 170, 174, 174, 170, 181, 181, 191, 180, 183, 171, 180, 180, 191, 178, 178, 188, 180, 175, 169, 191, 180, 188,
 173, 188, 191, 189, 188, 185, 196, 188, 188, 188, 176, 191, 171, 180, 183, 180, 196, 183, 180, 170, 182, 181, 193, 172,
 175, 194, 178, 189, 184, 185, 185, 177, 163, 190, 175, 201, 191, 184, 193, 175, 183, 183, 178, 191, 193, 194, 178, 181,
 180, 183, 175, 182, 183, 178, 178, 178, 181, 173, 186, 184, 193, 175, 175, 185, 179, 175, 182, 178, 175, 187, 173, 180,
 180, 185, 178, 176, 179, 189, 183, 184, 173, 178, 178, 176, 193, 183, 182, 170, 185, 185, 198, 180, 173, 182, 187, 188,
 175, 168, 185, 182, 174, 190, 179, 181, 183, 185, 180, 185, 178, 188, 182, 179, 175, 189, 179, 179, 181, 193, 188, 186,
 188, 183, 183, 178, 182, 180, 177, 179, 181, 177, 181, 175, 175, 185, 191, 188, 181, 186, 194, 191, 179, 188, 193, 185,
 178, 185, 191, 180, 164, 186, 190, 174, 181, 173, 191, 182, 178, 178, 173, 178, 180, 177, 193, 168, 184, 185, 185, 175,
 191, 180, 184, 190, 188, 185, 188, 170, 180, 177, 188, 196, 168, 183, 191, 191, 185, 188, 174, 170, 178, 180, 193, 170,
 182, 176, 173, 170, 183, 180, 183, 173, 183, 185, 191, 179, 180, 173, 183, 173, 181, 185, 192, 191, 198, 185, 183, 178,
 191, 185, 174, 178, 180, 191, 181, 191, 178, 182, 178, 175, 174, 175, 190, 175, 183, 175, 193, 173, 184, 178, 183, 191,
 178, 174, 189, 174, 193, 180, 178, 189, 175, 185, 180, 185, 177, 173, 186, 173, 178, 175, 175, 183, 188, 188, 193, 188,
 170, 183, 175, 175, 183, 180, 185, 185, 185, 173, 180, 180, 178, 182, 183, 185, 180, 175, 178, 193, 183, 185, 183, 178,
 180, 187, 178, 180, 178, 191, 188, 185, 183, 177, 170, 188, 173, 182, 186, 185, 185, 186, 185, 184, 182, 188, 192, 183,
 185, 173, 196, 182, 176, 181, 185, 188, 185, 183, 184, 188, 173, 186, 178, 188, 179, 191, 191, 188, 183, 176, 186, 175,
 180, 183, 180, 185, 185, 187, 183, 180, 170, 181, 182, 181, 185, 168, 184, 191, 184, 183, 194, 190, 189, 181, 177, 190,
 179, 186, 178, 190, 175, 192, 191, 183, 191, 184, 174, 192, 187, 178, 176, 175, 191, 179, 188, 178, 171, 180, 182, 173,
 177, 192, 183, 175, 182, 178, 188, 192, 183, 186, 188, 180, 191, 180, 173, 191, 185, 181, 175, 180, 178, 175, 184, 179,
 171, 180, 182, 174, 190, 170, 179, 175, 178, 177, 178, 171, 188, 173, 179, 182, 183, 185, 165, 182, 194, 181, 176, 180,
 172, 187, 178, 187, 180, 182, 174, 196, 196, 175, 189, 175, 183, 179, 179]



# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)


# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != "GK"]

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
