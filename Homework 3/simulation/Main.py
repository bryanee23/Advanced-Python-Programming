from TowerSimulator import TowerSimulator
import random

if __name__ == "__main__":
  length = int(input("Enter Number of clock ticks: "))
  landing_odds = float(input("Enter probability of planes arriving to the runway land: "))
  takeoff_odds = float(input("Enter probability of planes arriving to the runway takeoff "))
  sim = TowerSimulator(length, landing_odds, takeoff_odds)
  sim.run_simulation()

