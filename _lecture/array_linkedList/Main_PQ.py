# from ArrayQueue import ArrayQueue
from LinkedPriorityQueue import LinkedPriorityQueue

q = LinkedPriorityQueue()
q.add(1)
q.add(2)
q.add(4)
q.add(17)
q.add(3)
q.add(6)
q.add(0)

for i in q:
  print(i, end=" ")