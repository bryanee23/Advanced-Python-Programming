from LinkedQueue import LinkedQueue
from Customer import Customer


class Cashier:
   def __init__(self):
      self._total_customer_wait_time = 0
      self._customers_served = 0
      self._longest_wait = 0
      self._current_customer = None
      self._queue = LinkedQueue()

   def add_customer(self, c):
      self._queue.add(c)

   def serve_customer(self, cur_time):
      if self._current_customer is None:
         # If no customer is being served, see if there is one in the queue to start serving
         if self._queue.is_empty():
            # No customer is being helped and queue is empty, do nothing
            return
         self._current_customer = self._queue.pop()

         # Determine how many clock ticks this customer was in the queue
         wait_time = cur_time - self._current_customer.arrival_time
         self._total_customer_wait_time += wait_time
         if wait_time > self._longest_wait:
            self._longest_wait = wait_time

      self._current_customer.serve()

      if self._current_customer.transaction_time == 0:
         # Current customer has finished buying their tickets
         self._current_customer = None
         self._customers_served += 1

   def __str__(self):
      return_string = "\nCustomers Served: " + str(self._customers_served)
      return_string += "\nLongest Wait Time: " + str(self._longest_wait)
      return_string += "\nTotal Wait Time: " + str(self._total_customer_wait_time)
      return return_string