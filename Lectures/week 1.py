def function_1():
  print(5)

x = function_1

# print(x())

def function_1(the_function):
  x = the_function(5)
  return x

def function_2(x):
  return x * x

y = function_1(function_2)

def double(x):
   return x*2

old_list = [5, 10, 15, 20, 25]
# new_list = list(map(double, old_list))
new_list = list(map(lambda x: x*2, old_list))

# anonymous functions

# filter functions
old_list = [0, 100, 90, None, 0, 40, 0]
new_list = list(filter(lambda x: x, old_list))

# print('new_list' * 10)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello ", name, ". You have been alive approximately ", age * 365, " days ", sep="")

class counter
print()