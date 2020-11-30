from LinkedQueue import LinkedQueue
from TheaterSimulator import TheaterSimulator


print("Welcome to the Jungle(simulation)!")
length = input("Enter the number of clock ticks to perform: ")
odds = float(input("what are the odds a customer will show up each clock tick? "))
simulator = TheaterSimulator(length, odds)
simulator.run_simulation()
