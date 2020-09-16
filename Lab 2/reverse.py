# my reverse_list function runs on O(n), maybe a merge sort type of algo can get it to O(logn)?
# number of operations within the while loop equals the number of elements in the list + 2

def reverse_list(input_list):
  result = []
  list_length = len(input_list)

  while len(result) < list_length:
    result.append(input_list.pop())

  return result

#### test cases ####
print('Input:{},  Output:{}\n'.format([1, 2, 3, 4], reverse_list([1, 2, 3, 4])))
# Input:[1, 2, 3, 4],  Output:[4, 3, 2, 1]

print('Input:{},  Output:{}\n'.format(["cats", 3, "dogs", 7, -7], reverse_list(["cats", 3, "dogs", 7, -7])))
# Input:['cats', 3, 'dogs', 7, -7],  Output:[-7, 7, 'dogs', 3, 'cats']

#### prompt ####
"""
Define a function named 'reverse' which takes a list as an argument. This function should reverse the elements in the list (note: do not use the built-in reverse method included with list!).

If you pass the list { 1, 2, 3, 4 } to your function it should be changed to { 4, 3, 2, 1 } and {5, 4, 2, 3, 1 } should be changed to {1, 3, 2, 4, 5}, etc.

You are free to write your function however you like (other than using list's reverse method!) After you have run and tested your function, write a comment at the top of your file analyzing your function's performance. What is its time complexity and how did you determine this?
"""
