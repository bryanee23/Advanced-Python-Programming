from ArrayStack import ArrayStack
from LinkedStack import LinkedStack

def perform_operation(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  if operator == "-":
    return num1 - num2
  if operator == "/":
    return num1 / num2
  if operator == "*":
    return num1 * num2
  raise ValueError("Operator is not validg")

def evaluate_postfix(expression):
  s = LinkedStack()
  for token in expression.split():
    if token.isdigit():
      s.push(token)
      #skip if don't need to do it
    elif token in ['+', '-', '/', '*']:
      try:
        num2 = s.pop()
        num1 = s.pop()
        result = perform_operation(int(num1),int(num2), token)
        s.push(result)
      except KeyError:
        raise ValueError("invalid postfix expression: not enough operands")
    else:
      raise ValueError("invalid post expression: Invalid token", token)
  if len(s) != 1:
    raise ValueError("invalid post expression")
  return s.pop()


while True:
  expression = input("enter a postfix expression or q to quit: ")
  if expression == 'q':
    break
  try:
    result = evaluate_postfix(expression)
    print(result)
  except:
    print("invalid expression")

    odd numbers
    2 stacks
    if stack1 == stack2
