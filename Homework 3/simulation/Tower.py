from LinkedQueue import LinkedQueue
from Plane import Plane


class Tower:
   def __init__(self):
      self._total_Plane_wait_time = 0
      self._Planes_served = 0
      self._longest_wait = 0
      self._current_Plane = None
      self._queue = LinkedQueue()
      self._priority_queue = LinkedQueue()

   def add_to_Q(self, c):
      self._queue.add(c)

   def add_to_PriorityQ(self, c):
      self._priority_queue.add(c)

   def serve_Plane(self, cur_time):
      if self._current_Plane is None:
         # If no Plane is being served, see if there is one in the queue to start serving
         if self._queue.is_empty():
            # No Plane is being helped and queue is empty, do nothing
            return
         self._current_Plane = self._queue.pop()

         # Determine how many clock ticks this Plane was in the queue
         wait_time = cur_time - self._current_Plane.arrival_time
         self._total_Plane_wait_time += wait_time
         if wait_time > self._longest_wait:
            self._longest_wait = wait_time

      self._current_Plane.serve()

      if self._current_Plane.transaction_time == 0:
         # Current Plane has finished buying their tickets
         self._current_Plane = None
         self._Planes_served += 1

   def __str__(self):
      return_string = "\nPlanes Served: " + str(self._Planes_served)
      return_string += "\nLongest Wait Time: " + str(self._longest_wait)
      return_string += "\nTotal Wait Time: " + str(self._total_Plane_wait_time)
      return return_string