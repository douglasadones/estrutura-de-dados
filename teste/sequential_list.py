class _QueueNode:
    def __init__(self, info, priority):
        self.info = None
        self.priority = None
        self.next = None

class priority_queue:
    def __init__(self):
        self.qhead = None
        self.qtail = None
        self.count = 0