"""
Implement a queue:
1. Using an Array
2. with a Queue class using a Linked list
One should be able to add to the queue and remove from the queue following 
the FIFO property
"""
class QueueArray:
    """FIFO queue implementation using a Python list as underlying storage"""
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * QueueArray.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        """Remove and return the first element of the queue i.e FIFO
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None          # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # shrink the list when elements stored falls below 1/4 of its capacity
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def enqueue(self, value):
        """Add a value/element to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))   # double the array size
        avail = (self._front + self._size) % len(self._data) #compute location of next opening
        self._data[avail] = value
    
    def _resize(self, cap):             # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)"""
        old = self._data                # keep track of exisiting list
        self._data = [None] * cap       # allocate list with new capacity
        walk = self._front
        for k in range(self._size):     # only consider existing elements
            self._data[k] = old[walk]     # intentionally shift indices
            walk = (1 + walk) % len(old) # use old size as modulus
        self._front = 0                 # front realigned

