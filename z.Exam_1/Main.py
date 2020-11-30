from LinkedList import LinkedList

def problem1_script():
  print('1a. - Edge Case 1 (if list is empty) \nList contains:')
  list1 = LinkedList()
  list1.add_to_back(300)
  list1.print_list() # output = 1

  print('\n\n1b. - Edge Case 2 (if list is not empty) \nList contains:')
  list2 = LinkedList()
  list2.add_to_front(2)
  list2.add_to_front(19)

  list2.add_to_back('almost-last')
  list2.add_to_back(5)

  list2.add_to_front('potato')
  list2.print_list()# prints potato 1 2 almost-last 5

def problem2_script():
  print("list 1 contains: ")
  list1 = LinkedList()
  list1.add_to_front('A')
  list1.add_to_front('B')
  list1.print_list() # prints B A

  print("\nlist 2 contains: ")
  list2 = LinkedList()
  list2.add_to_front(1)
  list2.add_to_front(2)
  list2.print_list() # prints 2 1


  print("\nCombined lists into list 3")
  list3 = list1 + list2
  list3.print_list() # prints B A 2 1

def problem3_script():
  print("list contains: ")
  list1 = LinkedList()
  list1.add_to_front('A')
  list1.add_to_front('A')
  list1.add_to_front('A')
  list1.print_list()
  print("\nList1 length = {}".format(len(list1))) # prints 3

if __name__ == "__main__":
  print("Problem 1 - Create an add_to_back method")
  problem1_script()

  print("\n\n\nProblem 2 - Overload the '+' operator")
  problem2_script()

  print("\n\n\nProblem 3 - Overload the __len__ method")
  problem3_script()

  """
  PRINT OUTPUTS
  Problem 1 - Create an add_to_back method
  1a. - Edge Case 1 (if list is empty)
  List contains:
  300

  1b. - Edge Case 2 (if list is not empty)
  List contains:
  potato 19 2 almost-last 5


  Problem 2 - Overload the '+' operator
  list 1 contains:
  B A
  list 2 contains:
  2 1
  Combined lists into list 3
  B A 2 1


  Problem 3 - Overload the __len__ method
  list contains:
  A A A
  List1 length = 3
  """