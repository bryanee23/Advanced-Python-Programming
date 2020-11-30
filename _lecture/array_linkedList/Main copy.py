from ArrayStack import ArrayStack
from LinkedStack import LinkedStack


def is_balanced(expression):
  s = LinkedStack()
  # Scan each character in the incoming expression
  for c in expression:
    if c in "({[":
      s.push(c)
    elif c in ")}]":
      if s.is_empty():
        return False
      if c == ")":
        if s.peek() != "(":
          return False
        else:
          s.pop()
    elif c == "]":
      if s.peek() != "[":
        return False
      else:
        s.pop()
    elif c == "}":
      if s.peek() != "{":
        return False
      else:
        s.pop()
  return s.is_empty()


expression = input("Enter an expression: ")

if is_balanced(expression):
  print("Expression is balanced")
else:
  print("Expression is not balanced")

