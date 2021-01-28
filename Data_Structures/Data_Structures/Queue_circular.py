'''
------------------------------------------------------------------------
Circular array version of the Queue ADT.
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M02 10
------------------------------------------------------------------------
'''
from copy import deepcopy


class Queue:

    def __init__(self, max_size):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: cq = Queue(max_size)
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the queue (int > 0)
        Aspects:
            values - array of stored values
            front - index where the next value will be inserted
            rear - index of the oldest value, next to be removed
            count - number of stored values
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert max_size > 0, "Queue size must be > 0"

        self._max_size = max_size
        self._values = [None] * self._max_size
        self._front = 0
        self._rear = 0
        self._count = 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(cq)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: cq.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert (self._count < self._max_size), 'queue is full'

        self._values[self._front] = deepcopy(value)

        self._count += 1    #increments _count
        self._front = (self._front+1) % self._max_size #Inrements front by 1 then resets to size
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = cq.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = cq.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """

        return self._count == self._max_size

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = cq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert (self._count > 0), 'Cannot peek at an empty queue'

        return self._values[self._rear]

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = cq.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert (self._count > 0), 'Cannot remove from an empty queue'

        value = deepcopy(self._values[self._rear])
        self._values[self._rear] = None

        self._count -= 1
        self._rear = (self._rear + 1) % self._max_size

        return value
