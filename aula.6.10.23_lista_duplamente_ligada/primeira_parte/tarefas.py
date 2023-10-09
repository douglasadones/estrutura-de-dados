from random import randint
from priority_linked_queue import LinkedPriorityQueue

queue = LinkedPriorityQueue()

for i in range(5):
    priority = randint(0, 9)
    task = randint(101, 999)
    task = f'Task {task}'
    queue.enqueue(priority, task)
    print(f'{task}: {priority}')

queue.show()
