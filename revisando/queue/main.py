from sequential_queue import Queue as Seq_queue
from linked_queue import Queue as Linked_queue
from priority_queue_sequential import SequentialPriorityQueue
from priority_queue_linked import LinkedPriorityQueue

def Seq_and_linked_queue_test(queue_type):
    if queue_type == 'seq':
        queue = Seq_queue()
        print('Type of queue used: Sequential Queue')
    else:
        queue = Linked_queue()
        print('Type of queue used: Linked Queue')
    while True:
        value = int(input('integer Value (<0 to finish): '))
        if value < 0:
            break
        queue.enqueue(value)

        print(f'Queue has {queue.__len__()} items')

    print('Clearing Queue')
    while not queue.isEmpty():
        node = queue.dequeue()
        print(node)

    print(f'Queue has {queue.__len__()} items')


def Seq_and_linked_priority_queue_test(queue_type):
    if queue_type == 'seq':
        queue = SequentialPriorityQueue()
        print('Type of priority queue used: Sequential Priority Queue')
    else:
        queue = LinkedPriorityQueue()
        print('Type of priority queue used: Linked Priority Queue')
    while True:
        value = int(input('integer Value (<0 to finish): '))
        if value < 0:
            break
        priority = int(input('Priority: '))
        queue.enqueue(priority, value)
        queue.show()

    print(f'Priority Queue has {queue.__len__()} items')

    # print('Clearing Priority Queue')
    # while not queue.isEmpty():
    #     node = queue.dequeue()
    #     print(f'Removed node -> item: {node.item:>3} | Priority: {node.priority}')

    # print(f'Priority Queue has {queue.__len__()} items')
    


if __name__ == '__main__':
    print('What do you want to test?')
    print('1. Queue')
    print('2. Priority Queue')
    type = int(input('Your Choice: '))
    if type == 1:
        queue_type = str(input('Choose type of Queue ("seq" or "link"): '))
        Seq_and_linked_queue_test(queue_type)
    else:
        queue_type = str(input('Choose type of Priority Queue ("seq" or "link"): '))
        Seq_and_linked_priority_queue_test(queue_type)
