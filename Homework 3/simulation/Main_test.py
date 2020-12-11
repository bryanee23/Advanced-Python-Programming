import unittest, random
from Plane import Plane
from Tower import Tower
from TowerSimulator import TowerSimulator

class Test_Cases_ArraySet(unittest.TestCase):
  """
  Advanced testing is near the title
  """

  def test_Tower(self):
    """
    Test odds of a plane that needs to land
    add to queue
    """
    print('here')
    tower = Tower()
    ran_num = random.randrange(3, 7)
    for i in range(0, ran_num):
      if (i % 2 ) == 0:
        new_plane = Plane("Takeoff", i)
        tower.add_to_Q(new_plane)
      else:
        new_plane = Plane("landing", i)
        tower.add_to_PriorityQ(new_plane)

      tower.serve_plane(i)
    print(self._Tower)
    print('here')

  def test_sim(self):
    """
    Test odds of a plane that needs to land
    add to queue
    """
    clock_tick = random.randrange(1, 7)
    odds_to_land_arrival = 0.75
    odds_to_takeoff_arrival = 0.89

    sim = TowerSimulator(clock_tick, odds_to_land_arrival, odds_to_takeoff_arrival)
    sim.run_simulation()


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

  def test_combo(self):
    """
    Test odds of a plane that needs to land
    add to queue
    """
    i = random.randrange(1, 7)
    odds_to_land_arrival = 0.75
    odds_to_takeoff_arrival = 0.89


    q = []
    for clock_tick in range(0, i):
      #there lies a possiblity where a random number adds both a landing and take off to the queu
      random_gen = random.random()

      if  random_gen < odds_to_land_arrival:
        status = "to_land"
        new_plane = Plane.generate_Plane(status,i)
        q.append(new_plane)

      if  random_gen < odds_to_takeoff_arrival:
        status = "to_takeoff"
        new_plane = Plane.generate_Plane(status,i)
        q.append(new_plane)

      if  random_gen > odds_to_takeoff_arrival and random_gen > odds_to_land_arrival:
        status = "None"
        new_plane = Plane.generate_Plane(status,i)
        q.append(new_plane)




if __name__ == '__main__':
  unittest.main()