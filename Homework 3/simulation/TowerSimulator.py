from Tower import Tower
from Plane import Plane


class TowerSimulator:
   def __init__(self, length, odds_to_land_arrival, odds_to_takeoff_arrival):
      self._length = length
      self._odds_to_land_arrival = odds_Plane_arrives
      self._odds_to_takeoff_arrival = odds_to_takeoff_arrival
      self._Tower = Tower()

   def run_simulation(self):
      """ The following loop controls our entire simulation
      Each iteration represents a single clock tick (i.e. a minute) """
      for i in range(self._length):
         random_gen = random.random()

         if random_gen > odds_to_takeoff_arrival and random_gen > odds_to_land_arrival:
            pass

         else:

            if random_gen < odds_to_land_arrival:
               new_plane = Plane.generate_Plane(status,i)
               self._Tower.add_to_PriorityQ(new_Plane)(new_plane)

            if random_gen < odds_to_takeoff_arrival:
            status = "to_takeoff"
            new_plane = Plane.generate_Plane(status,i)
            q.append(new_plane)


         # See if a new Plane is created this clock tick
         new_Plane = Plane.generate_Plane(self._odds_to_land_arrival, self._odds_to_takeoff_arrival, i)

         # If it is, add it to the Tower's queue
         if new_Plane is not None:
            if i % 2 == 0:
               self._Tower.add_Plane(new_Plane)
            else:
               self._Tower2.add_Plane(new_Plane)

         # Tell the Tower to give front Plane one clock tick of help
         self._Tower.serve_Plane(i)
         self._Tower2.serve_Plane(i)

      print(self._Tower)
      print(self._Tower2)