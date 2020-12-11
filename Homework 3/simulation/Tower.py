from ArrayQueue import ArrayQueue
from LinkedPriorityQueue import LinkedPriorityQueue
from LinkedQueue import LinkedQueue
from Plane import Plane


class Tower:
   def __init__(self):
      self._priority_queue = LinkedQueue()
      self._queue = ArrayQueue()
      self._current_plane = None
      self._total_plane_wait_time = 0
      self._planes_served = 0
      self._planes_crashed = 0
      self._metrics = {
         "longest_wait_takeoff": 0,
         "longest_wait_landing": 0,
         "served_takeoff": 0,
         "served_landing": 0
      }


   def add_to_Q(self, c):
      self._queue.add(c)

   def add_to_PriorityQ(self, c):
      self._priority_queue.add(c)


   def set_metrics(self, plane, cur_time):
      """
      set class' metrics
      :param plane:
      :param cur_time:
      """
      if plane is not None:
         #check takeoff metrics
         if plane.status == "Takeoff":
            wait_time = cur_time - self._current_plane.arrival_time
            self._metrics["longest_wait_takeoff"] += wait_time

            if wait_time > self._metrics["longest_wait_takeoff"]:
               self._metrics["longest_wait_takeoff"] = wait_time

         #check landing metrics
         if plane.status == "Landing":
            wait_time = cur_time - self._current_plane.arrival_time
            self._metrics["longest_wait_landing"] += wait_time

            if wait_time > self._metrics["longest_wait_landing"]:
               self._metrics["longest_wait_landing"] = wait_time


   def check_if_complete(self, plane):
      if plane is not None:
         #if plane is complete
         if plane.transaction_time == 0:

            if plane.status == "Takeoff":
               self._metrics["served_takeoff"] += 1
            else:
               self._metrics["served_landing"] += 1

            self._current_plane = None
            self._planes_served += 1


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
            try:
               if len(self._priority_queue) > 0:
                  self._current_plane = self._priority_queue.pop()
                  self._current_plane.minus_fuel()

                  # crashed plane
                  if self._current_plane.fuel == 0:
                     self._current_plane = None
                     self._planes_crashed += 1
               else:
                  if self._queue.peek() is not None:
                     self._current_plane = self._queue.pop()
            except:
               pass

         self.set_metrics(self._current_plane, cur_time)

      if self._current_plane is not None:
         self._current_plane.serve()

      self.check_if_complete(self._current_plane)



   @property
   def queue(self):
      return self._queue

   @property
   def priority_queue(self):
      return self._priority_queue

   def __str__(self):
      return_string = "\naverage time spent waiting for take off: " + str(self._metrics["longest_wait_takeoff"]/(round(self._metrics["served_takeoff"]+1, 3)))


      return_string += "\naverage time spent waiting for to land: " + str(self._metrics["longest_wait_landing"]/ round(self._metrics["served_landing"]+1, 3) )
      return_string += "\nlongest time spent waiting for take off: " + str(self._metrics["longest_wait_takeoff"])
      return_string += "\nlongest time spent waiting for to land: " + str(self._metrics["longest_wait_landing"])
      return_string += "\nPlanes Crashed: " + str(self._planes_crashed)
      return_string += "\nPlanes served: " + str(self._planes_served)
      return_string += f"\nPlanes in queues {len(self._priority_queue) + len(self._queue)}"
      return return_string



# What is the average time spent waiting for take off?
# What is the average time spent waiting to land?
# What is the longest time spent waiting for take off?
# What is the longest time spent waiting to land?
# How many planes crashed?
#   print(f"{len(tower.priority_queue)} {len(tower.queue)}")
# How many planes total took off and landed during the simulation?