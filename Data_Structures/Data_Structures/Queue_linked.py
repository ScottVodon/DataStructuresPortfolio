'''
------------------------------------------------------------------------
Linked version of the Queue ADT.
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M03 14
------------------------------------------------------------------------
'''
from copy import deepcopy

class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue.
        Use: queue = Queue()
        -------------------------------------------------------
        Aspects:
            front - Start of the current chain, next node to be removed
            rear - End of the current chain
            count - Number of nodes in the chain
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        new_node = _Queue_Node(value,None)

        if self._rear is None: #If the chain is empty
            self._front = new_node #New node is the front
            self._rear = new_node  #and the rear
        else:   #If chain is not empty
            self._rear._next = new_node #Append the node to the end
            self._rear = new_node   #Make the new node the rear
        self._count += 1
        return deepcopy(new_node._value)

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        result = self._front._value

        self._front = self._front._next
        self._count-=1

        return result

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        return deepcopy(self._front._value)

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Equivalent of:
        self.insert(source.remove()), but moves nodes not data.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        if self._front != self._rear:
            hold = self._front
            self._front = self._front._next
            hold._next = None
            self._rear._next = hold

        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"


        while source._count > 0:
            current_sor = source._front
            source._front = source._front._next
            if source._front is None:
                source._rear = None
            source._count-=1
            self._rear._next = current_sor
            self._rear = current_sor

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        size = source1.__len__() + source2.__len__()
        
        while !source1.is_empty() or !source2.is_empty():
            if !source1.is_empty():
                self.insert(source1.remove())
            if !source2.is_empty():
                self.insert(source2.remove())

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains remaining values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()

        left = True

        while self._count > 0:
            if left == True:
                if target1._front is None:
                    target1._front = self._front
                    self._front = self._front._next
                    target1._rear = target1._front
                else:
                    target1._rear._next = self._front
                    target1._rear = self._front
                    self._front=self._front._next
                target1._count += 1
            else:
                if target2._front is None:
                    target2._front = self._front
                    self._front = self._front._next
                    target2._rear = target2._front
                else:
                    target2._rear._next = self._front
                    target2._rear = self._front
                    self._front=self._front._next
                target2._count += 1

            left = not left
            self._count -= 1

        if target1._rear is not None:
            target1._rear._next = None
        if target2._rear is not None:
            target2._rear._next = None

        return target1, target2

    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents
        are identical and in the same order, returns True, otherwise
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False
                otherwise. (boolean)
        -------------------------------------------------------
        """
        current = self._front
        current2 = target._front
        identical = True
        while current is not None and current2 is not None and identical is True:
            if current._value != current2._value:
                identical = False
            current = current._next
            current2 = current2._next

        if current2 is not None or current is not None:
            identical = False


        return identical
