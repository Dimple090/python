# Basic Questions
# How do you create a tuple containing the elements `1`, `2`, and `3` in Python?
tuple=(1,2,3)
print(tuple)
print(len(tuple))
print(type(tuple))



#Given a tuple my_tuple = (10, 20, 30, 40), how do you access the second element?
my_tuple = (10, 20, 30, 40)
print(my_tuple[1])



#How do you find the length of the tuple `my_tuple = (1, 2, 3, 4, 5)`?
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))




#How do you concatenate two tuples, `tuple1 = (1, 2)` and `tuple2 = (3, 4)`?
tuple1 = (1, 2)
tuple2 = (3, 4)
new_tuple=tuple1 + tuple2
print(new_tuple)



#How can you reverse a tuple `my_tuple = (1, 2, 3)`?
my_tuple = (1, 2, 3)
print(my_tuple[::-1])



#How do you unpack a tuple `my_tuple = (1, 2, 3)` into three variables?
my_tuple = (1, 2, 3)
x,y,z=my_tuple
print(x)
print(y)
print(z)





#How can you find the maximum and minimum values in a tuple `my_tuple = (5, 3, 8, 1)`?
my_tuple=(5,3,8,1)
max_values=max(my_tuple)
print("max value is=",max_values)
min_values=min(my_tuple)
print("min value is=",min_values)





#Given a tuple `my_tuple = (1, 2, 3, 1, 2, 1)`, how do you count the number of occurrences of the element `1`?
my_tuple=(1,2,3,1,2,1)
new_tuple=my_tuple.count(1)
print(new_tuple)


#How do you access the element `4` from a nested tuple `nested_tuple = ((1, 2), (3, 4))`?
nested_tuple = ((1, 2), (3, 4))
new_tuple=nested_tuple[1][1]
print(new_tuple)






#How do you find the index of the first occurrence of the element `2` in the tuple `my_tuple = (1, 2, 3, 2, 4)`?
my_tuple = (1, 2, 3, 2, 4)
# Finding the index of the first occurrence of the element '2'
index_of_two = my_tuple.index(2)
print("Index of the first occurrence of 2:", index_of_two)  



#How do you convert a list `my_list = [1, 2, 3]` into a tuple?
my_list = [1, 2, 3]
# Converting the list to a tuple
my_tuple = tuple(my_list)  # This line is correct
print(my_tuple)  # Output: (1, 2, 3)




