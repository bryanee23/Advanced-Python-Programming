from LinkedQueue import LinkedQueue
from Plane import Plane


class Tower:
   def __init__(self):
      self._total_plane_wait_time = 0
      self._planes_served = 0
      self._planes_crashed = 0
      self._longest_wait = 0
      self._current_plane = None
      self._queue = LinkedQueue()
      self._priority_queue = LinkedQueue()

   def add_to_Q(self, c):
      self._queue.add(c)

   def add_to_PriorityQ(self, c):
      self._priority_queue.add(c)


   def serve_plane(self, cur_time):
      """
      :param curr_time: int clock_tick
      """
      if self._current_plane is None:
         # No plane is being helped and queue is empty, do nothing
         if self._queue.is_empty() and self._priority_queue.is_empty():
            return

         else:
         # set the planes
            if len(self._priority_queue) > 0:
               self._current_plane = self._priority_queue.pop()
               self._current_plane.minus_fuel()

               # crashed plane
               if self._current_plane.fuel == 0:
                  self._current_plane = None
                  self._planes_crashed += 1
            else:
               self._current_plane = self._queue.pop()

         # Determine how many clock ticks this plane was in the queue
         wait_time = cur_time - self._current_plane.arrival_time
         self._total_plane_wait_time += wait_time
         if wait_time > self._longest_wait:
            self._longest_wait = wait_time

      self._current_plane.serve()

      # completed served plane
      if self._current_plane.transaction_time == 0:
         self._current_plane = None
         self._planes_served += 1




   def __str__(self):
      return_string = "\nPlanes Served: " + str(self._planes_served)
      return_string += "\nPlanes Crashed: " + str(self._planes_crashed)
      return_string += "\nLongest Wait Time: " + str(self._longest_wait)
      return_string += "\nTotal Wait Time: " + str(self._total_Plane_wait_time)
      return return_string