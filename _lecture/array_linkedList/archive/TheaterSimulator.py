from Cashier import Cashier
from Customer import Customer

class TheaterSimulator:
  def __init__(self, length, odds_customer_arrives):
    self._length = length
    self._odds_customer_arrives = odds_customer_arrives
    self._cashier = Cashier()

  def run_simulation(self):
    for i in range(self._length):
      #see if a new customer is created this clock tick
      new_customer = Customer.generate_customer(self._odds_customer_arrives, i)
      if new_customer is not None:
        self._cashier.add_customer(new_customer)

      self._cashier.serve_customer(i)
    print(self._cashier)