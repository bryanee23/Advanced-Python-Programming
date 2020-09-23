from Node import Node

def is_in_list(list_pointer, target):
  probe2 = list_pointer
  while probe2 is not None:
    if probe2.data == target:
      return True
    probe2 = probe2.next
  return 'Target not in list'


def add_to_list(list_pointer, item):
  """ adds item to the front of linked list pointed by list_pointer"""
  list_pointer = Node(item, list_pointer)
  return list_pointer


def add_to_end(list_pointer, item):
  new_node = Node(item)
  if list_pointer is None: # empty list
    list_pointer = add_to_list(list_pointer, item)

  else:

    probe = list_pointer
    while probe.next is not None:
      probe = probe.next
    probe.next = new_node

  return list_pointer



def print_list(head):
  probe = head
  print('List contains: ')
  while probe is not None:
    print(probe.data, end=' ')
    probe = probe.next


def get_length(list_pointer):
  probe = list_pointer
  counter = 0
  while probe is not None:
    counter+=1
    probe = probe.next
  return counter


################
""""
Create a function named add_to_position which takes three arguments:
The head pointer, an item to add to the list, and a number to represent the position.

The item should be added to the list at the given position (if possible). You can use the array numbering scheme, where the first item in the linked list is item 0, the second is item 1, etc. Note:

If the position is past the end of the list, raise an error (for example if the linked list is empty and they try to add to position 1, or if the linked list has 5 items and they try to add to position 7)

If the item being added goes in the middle of the list, you need to be careful to not break the chain! In other words, you need to update more than just the new Node's pointer.

"""
################

def add_to_position(list_pointer, item, position):
  list_length = get_length(list_pointer)
  probe = list_pointer
  previous = None

  # Edge Cases
  if position == 0 and list_pointer == None: # add to empty list
    list_pointer = add_to_list(list_pointer, item)
    return list_pointer

  if position == 0: # add to front
    list_pointer = add_to_list(list_pointer, item)
    return list_pointer

  if position == list_length: # add to end
    list_pointer = add_to_end(list_pointer, item)

  if position > list_length: # position outside of range
    raise IndexError("Index out of range")

  if position < list_length:
    counter = 0
    while probe != None and counter < position:
      counter += 1
      previous = probe
      probe = probe.next
    previous.next = Node(item, probe)

  return list_pointer


################
# test cases
################
head = None
head = Node('E', head)
head = Node('D', head)
head = Node('C', head)
head = Node('B', head)
head = Node('A', head)
# A B C D E
# 0 1 2 3 4

################
# uncomment to test
################
# head = add_to_position(head, 99, 0) # 99 A B C D E
# head = add_to_position(head, 99, 1) # A 99 B C D E
# head = add_to_position(head, 99, 2) # A B 99 C D E
# head = add_to_position(head, 99, 3) # A B C 99 D E
# head = add_to_position(head, 99, 4) # A B C 99 D E
# head = add_to_position(head, 99, 5) # A B C D E 99
# head = add_to_position(head, 99, 6) # index error raised
print_list(head)
print('\nList Length: {}'.format(get_length(head))) #prints 3


head_none = None
# head_none = add_to_position(head_none, 99, 0) # 99
head_none = add_to_position(head_none, 99, 1) # # index error raised
print_list(head_none)
print('\nList Length: {}'.format(get_length(head_none))) #prints 3