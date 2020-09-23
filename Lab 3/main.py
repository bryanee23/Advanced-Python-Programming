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


################
""" The function 'length' should return the number of items in a given linked list. """
################
def get_length(list_pointer):
  probe = list_pointer
  counter = 0
  while probe is not None:
    counter+=1
    probe = probe.next
  return counter



head = None
while True:
  val = input("enter a value or q to stop: ")
  if val == 'q':
    break
  head = add_to_end(head, val)

#input(a, b, c)
print_list(head) #prints a b c
print('\nList Length: {}'.format(get_length(head))) #prints 3