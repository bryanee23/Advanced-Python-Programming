from ArrayStack import ArrayStack

class MathOps(ArrayStack):
  def __init__(self):
    self.current_value = ArrayStack()
    self.current_value.push(0)
    self.redo_stack = ArrayStack()
    self.undo_stack = ArrayStack()
    ArrayStack.__init__(self)


  def evaluate_expression(self, right_operand, operator):
    """evaluate using inputed operater from current value w/ inputed right_operand and operator"""
    left_operand = self.current_value.peek()

    if operator == "+":
      evaluated_value = left_operand + right_operand
    if operator == "-":
      evaluated_value = left_operand - right_operand
    if operator == "/":
      evaluated_value = left_operand / right_operand
    if operator == "*":
      evaluated_value = left_operand * right_operand

    print("{} {} {} = {}\n".format(left_operand, operator, right_operand, evaluated_value))
    self.current_value.push(evaluated_value)



  def check_if_valid_operator(self, operater):
      valid_operators = ['+', '*', '/', '-']
      if operater not in valid_operators:
        raise TypeError("This message won't show up, will go straight to except block")
      else:
        return operater



  def parse_input(self, _input):
      valid_strings = ['u', 'r', 'q']

      if _input not in valid_strings:
        try:
          _input = int(_input)
          operator = input("Enter an operation: ")
          operator = self.check_if_valid_operator(operator)
          self.evaluate_expression(_input, operator)
        except:
          print("Invalid Input. Try Again\n")
          pass

      if _input == 'u':
        if self.current_value._size >= 2:
          self.redo_stack.push(self.current_value.pop())
          print("\n")
        else:
          print("No more actions to undo!\n")

      if _input == 'r':
        if self.redo_stack._size > 0:
          self.current_value.push(self.redo_stack.pop())
          print("\n")
        else:
          print("No more actions to undo!\n")

      if _input == 'q':
        print("Stopping Program\n")
        return True



  def run_script(self):
    stop = False
    while stop is not True:
      print("Current value is {}".format(self.current_value.peek()))
      input_string = input("Enter a number, 'u' to undo, 'r' to redo, 'q' to quit: ")
      return_string = self.parse_input(input_string)

      if return_string:
        stop = True



if __name__ == "__main__":
  run = MathOps()
  run.run_script()
