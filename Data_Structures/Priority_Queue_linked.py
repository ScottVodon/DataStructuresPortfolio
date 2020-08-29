'''
------------------------------------------------------------------------
linked version of the Priority Queue ADT.
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M03 14
------------------------------------------------------------------------
'''
from copy import deepcopy

class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        n = len(self)
        if n == 0:
            b = True
        else:
            b = False
            
        return b
        
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """

        return self._count

    def insert(self, value):
        """

        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        new_node = _PQ_Node(value,None)
        inserted = False

        if current is None:
            self._front = new_node
            self._rear = new_node

        while current is not None and not inserted:
            if current._value > value:
                if previous is not None:
                    previous._next = new_node
                else:
                    self._front = new_node
                new_node._next = current
                inserted = True
            elif current._next is None:
                current._next = new_node
                self._rear = new_node
                inserted = True
            previous = current
            current = current._next
        self._count+= 1
        
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"
        value = self._front
        self._front = value._next
        self._count -= 1
        return value._value


    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"
        value = deepcopy(self._front._value)
        return value


    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """
        left = True
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        while self._front is not None:
            hold = self._front
            self._front = self._front._next
            hold._next= None

            if left is True:
                if target1._rear is None:
                    target1._front = hold
                    target1._rear = hold
                else:
                    target1._rear._next = hold
                    target1._rear = target1._rear._next
                target1._count += 1

            else:
                if target2._rear is None:
                    target2._front = hold
                    target2._rear = hold
                else:
                    target2._rear._next = hold
                    target2._rear = target2._rear._next
                target2._count += 1
                
            left = not left
            self._count -= 1
        self._rear = None
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        while self._front is not None:
            hold = self._front
            self._front = self._front._next
            hold._next= None

            if hold._value < key:
                if target1._rear is None:
                    target1._front = hold
                    target1._rear = hold
                else:
                    target1._rear._next = hold
                    target1._rear = target1._rear._next
                target1._count += 1

            else:
                if target2._rear is None:
                    target2._front = hold
                    target2._rear = hold
                else:
                    target2._rear._next = hold
                    target2._rear = target2._rear._next
                target2._count += 1
                
            self._count -= 1
        self._rear = None
        
        return target1, target2
    def combine(self, source1, source2):
        """

        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        while source1._count > 0: 
            if self._front is None:
                self._front = source1._front
                self._rear = self._front
                source1._front = source1._front._next
                self._rear._next = None
                self._count += 1
            else: 
                self.insert(source1._front._value)
                source1._front = source1._front._next
                self._rear._next = None
            source1._count -= 1
            
        while source2._count > 0:
            if self._front is None:
                self._front = source2._front
                self._rear = self._front
                source2._front = source2._front._next
                self._rear._next = None
                self._count += 1
            else: 
                self.insert(source2._front._value)
                source2._front = source2._front._next
                self._rear._next = None
            source2._count -= 1

        if source1._front is None: 
            source1._rear = None
        if source2._front is None: 
            source2._rear = None
    
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"
        

        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"
        
        node = source._front
        source._count -= 1
        source._front = source._front._next
        
        if source._front is None:
            source._rear = None
        
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node
            
        node._next = None
        self._rear = node
        self._count += 1
        return
    
    
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next

