# Write a function that takes an unknown number of arguments and returns their sum.
def sum_up(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_up(45,46,37))
# Write a function that takes a list of integers and an unknown number of additiona
# integers as arguments. The function should return the index of the first occurrence
#  of the sum of the list and the additional integers

# Write a function that takes an unknown number of keyword arguments and returns a 
# dictionary where the keys are the argument names and the values are the argument
#  values.
def three_items(a, b, c):
    print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))
#     mylist = ['aardvark', 'baboon', 'cat']
#     three_items(*mylist)
# a = aardvark, b = baboon, c = cat
# Write a function that takes a function and an unknown number of arguments, and 
# returns the result of calling the function with the arguments.
def call_function(func, *args):
    return func(*args)
# Write a function that takes a list of integers and an unknown number of keyword 
# arguments. The function should return a new list where each integer in the 
# original list has been multiplied by the value of the corresponding keyword 
# argument.
def multiply_list(lst, *args):
    for i in range(len(args)):
        lst[i] = lst[i] * args[i]

    return lst

# Write a function that takes a list of integers and an unknown number of additiona
# integers as arguments. The function should return the index of the first occurrence
#  of the sum of the list and the additional integers


  
# Write a function that takes an unknown number of keyword arguments, each with a 
# string value. The function should concatenate all the strings and return the 
# resulting string.
def concat(*args, **kwargs):
    result = ""
    for arg in args:
        result += str(arg)

    for key, value in kwargs.items():
        result += key + ":" + value

    return result
