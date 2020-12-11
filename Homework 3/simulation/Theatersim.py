from Cashier import Cashier
from Customer import Customer


class TheaterSimulator:
   def __init__(self, length, odds_customer_arrives):
      self._length = length
      self._odds_customer_arrives = odds_customer_arrives
      self._cashier = Cashier()
      self._cashier2 = Cashier()

   def run_simulation(self):
      """ The following loop controls our entire simulation
      Each iteration represents a single clock tick (i.e. a minute) """
      for i in range(self._length):

         # See if a new customer is created this clock tick
         new_customer = Customer.generate_customer(self._odds_customer_arrives, i)

         # If it is, add it to the Cashier's queue
         if new_customer is not None:
            if i % 2 == 0:
               self._cashier.add_customer(new_customer)
            else:
               self._cashier2.add_customer(new_customer)

         # Tell the Cashier to give front Customer one clock tick of help
         self._cashier.serve_customer(i)
         self._cashier2.serve_customer(i)

      print(self._cashier)
      print(self._cashier2)