from llistqueue import Queue
from simulation_class import TicketCounterSimulation

values = Queue()
for i in range(16):
    if i % 3 == 0:
        values.enqueue(i)