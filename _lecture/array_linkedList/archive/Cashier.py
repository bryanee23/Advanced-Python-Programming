from LinkedQueue import LinkedQueue
from Customer import Customer

class Cashier:
  def __init__(self):
  # """arrival time represents which clock-tick this customer has"""
    self._total_customer_wait_time = 0
    self._customers_served = 0
    self._longest_wait = 0
    self._current_customer = None
    self._queue = LinkedQueue()

  def add_customer(self, customer):
    self._queue.add(customer)

  def serve_customer(self, cur_time):
    if self._current_customer is None:
      #if no customer is being served, see if there is one in teh queue to start
      if self._queue.is_empty():
        #no customer being helped, empty queue, do nothing
        return
      self._current_customer = self._queue.pop()

      wait_time = curr_time - self._current_customer.arrival_time
      self._total_customer_wait_time += wait_time
      if wait_time > self._longest_wait:
        self._longest_wait = wait_time

    self._current_customer.serve()

    if self._current_customer.transaction_time == 0:
      self._current_customer = None

  def __str__(self):
    return_string = "\nCustomers Served: " + (self._customers_served)
    return_string += "\nLongest Wait Time" + (self._longest_wait)
    return_string += "\nTotal wait time" + (self._total_customer_wait_time)
    return return_string