from LinkedStack import LinkedStack

def check_palindrome(input_string):
  stack = LinkedStack()
  end = len(input_string)
  mid_point = len(input_string) // 2
  even_number = 0

  for i in range(0, mid_point):
    stack.push(input_string[i])

  if len(input_string)%2 == even_number:
    for i in range(mid_point, end):
      if input_string[i] != stack.pop():
        return False
  else:
    for i in range(mid_point + 1, end):
      if input_string[i] != stack.pop():
        return False

  return True


if __name__ == "__main__":
  while True:
    input_string = input("Enter a string or Enter 'q' to quit: ")
    if input_string == 'q':
      break

    if check_palindrome(input_string):
      print("{} is a palindrome".format(input_string))
    else:
      print("Invalid Entry, {} is not a palindrome".format(input_string))