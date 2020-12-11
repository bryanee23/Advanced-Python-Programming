import unittest, random
from Plane import Plane
from TowerSimulator import TowerSimulator

class Test_Cases_ArraySet(unittest.TestCase):
  """
  Advanced testing is near the title
  """

  def test_takeoff(self):
    """
    Test odds of a plane that needs to takeoff
    """
    i = random.randrange(0, 20)
    odds_to_takeoff_arrival = 0.25
    random_gen = random.uniform(0, odds_to_takeoff_arrival)

    if  random_gen < odds_to_takeoff_arrival:
      status = "to_takeoff"
      new_plane = Plane.generate_Plane(status,i)

      self.assertEqual(new_plane.status, "to_takeoff")
      self.assertEqual(type(new_plane.arrival_time), int)
      self.assertEqual(type(new_plane.transaction_time), int)
      self.assertEqual(type(new_plane.fuel), int)

  def test_landing(self):
    """
    Test odds of a plane that needs to land
    """
    i = random.randrange(0, 20)
    odds_to_land_arrival = 0.75
    random_gen = random.uniform(0, odds_to_land_arrival)

    if  random_gen < odds_to_land_arrival:
      status = "to_land"
      new_plane = Plane.generate_Plane(status,i)

      self.assertEqual(new_plane.status, "to_land")
      self.assertEqual(type(new_plane.arrival_time), int)
      self.assertEqual(type(new_plane.transaction_time), int)
      self.assertEqual(type(new_plane.fuel), int)

  # def test_combo(self):
  #   """
  #   Test odds of a plane that needs to land
  #   add to queue
  #   """
  #   clock_tick = random.randrange(1, 7)
  #   odds_to_land_arrival = 0.45
  #   odds_to_takeoff_arrival = 0.5

  #   q = []
  #   for i in range(0, clock_tick):
  #     #there lies a possiblity where a random number adds both a landing and take off to the queu
  #     random_gen = random.random()
  #     if  random_gen > odds_to_takeoff_arrival and random_gen > odds_to_land_arrival:
  #       status = "None"
  #       new_plane = Plane.generate_Plane(status,i)
  #       q.append(new_plane)

  #     else:
  #       if  random_gen < odds_to_land_arrival:
  #         status = "to_land"
  #         new_plane = Plane.generate_Plane(status,i)
  #         q.append(new_plane)

  #       if  random_gen < odds_to_takeoff_arrival:
  #         status = "to_takeoff"
  #         new_plane = Plane.generate_Plane(status,i)
  #         q.append(new_plane)

  def test_tower(self):
    clock_tick = random.randrange(2, 7)
    odds_to_takeoff_arrival = 0.6
    odds_to_land_arrival = 0.75

    sim = TowerSimulator(clock_tick, odds_to_takeoff_arrival, odds_to_land_arrival)
    sim.run_simulation()


if __name__ == '__main__':
  unittest.main()