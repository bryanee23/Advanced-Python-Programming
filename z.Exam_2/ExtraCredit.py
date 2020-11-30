from ArrayStack import ArrayStack

def check_binaryString(input_string):
  stack = ArrayStack()
  if len(input_string)%2 != 0:
    return False

  for i in input_string:
    if i == "1":
      stack.push(i)

  for i in input_string:
    if i == "0":
      try:
        stack.pop()
      except:
        return False

  return stack._size == 0


if __name__ == "__main__":
  while True:
    input_string = input("Enter a binary string or Enter 'q' to quit: ")
    if input_string == 'q':
      break

    if check_binaryString(input_string):
      print("Accepted! {} has the same number of 1's and 0's \n".format(input_string))
    else:
      print("Invalid Entry, {} does not the same 1's and 0's \n".format(input_string))