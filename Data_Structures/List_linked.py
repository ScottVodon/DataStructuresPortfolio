'''
------------------------------------------------------------------------
Linked version of the list ADT
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M02 25
------------------------------------------------------------------------
'''
from copy import deepcopy

class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """ 
        
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """

        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _List_Node(value, None)
        if self._front is None:
            #list is empty
            self._front = new_node
            self._rear = new_node
        else:
            old_node = self._front
            self._front = new_node
            self._front._next = old_node
        self._count += 1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _List_Node(value, None)
        
        if self._rear is None:
            #list is empty
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if i < 0:
            i = self._count + i
        if i <= 0:
            self.prepend(value)
        elif i > self._count:
            self.append(value)
        else:              
            current  = self._front
            count = 0
            
            while count < i:
                previous = current
                current = current._next
                count += 1
            
            new_node = _List_Node(value, current)    
            previous._next = new_node
            self._count += 1
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        current = self._front
        count = 0
        previous = None        
        
        while current is not None and current._value != key:
            previous = current
            current = current._next
            count += 1
            
        if current is None:
            count = -1
            
        return previous, current, count

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, _ = self._linear_search(key)
                
        if current is None:
            value = None
        else:
            value = current._value
            self._count -= 1
            if previous is None:
                self._front = self._front._next
                if self._front is None:
                    self._rear = None
            else:
                previous._next = current._next
                if previous._next is None:
                    self._rear = previous

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        hold = self._front._next
        result = self._front._value
        self._front._next = None
        self._front = hold
        if self._front is None:
            self._rear = None
        self._count -= 1
        
        return result

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        while current is not None:
            if current._value == key:
                if previous is None:
                    self._front = self._front._next
                    if self._front is None:
                        self._rear = None
                elif current._next is None:
                    previous._next = None
                else:
                    previous._next = current._next
                self._count -= 1 
            else:        
                previous = current
            current = current._next                
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, _ = self._linear_search(key)

        value = None

        if current is not None:
            value = current._value

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"


        value = deepcopy(self._front._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)
        
        return index

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        if i < 0:
            i = i + self._count
        count = 0
        target = self._front
        
        while count < i:
            target = target._next
            count += 1
        
        value = deepcopy(target._value)
        
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        if i < 0:
            i = i + self._count
        count = 0
        target = self._front
        
        while count < i:
            target = target._next
            count += 1
        
        target._value = deepcopy(value)
        
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, _, index = self._linear_search(key)
        return index != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        _max = deepcopy(current._value)
        count = 0
        
        
        while current is not None and count < self._count:
            if current._value > _max:
                _max = deepcopy(current._value)
            current = current._next
            
        return _max

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"


        current = self._front
        _min = deepcopy(current._value)
        count = 0
        
        
        while current is not None and count < self._count:
            if current._value < _min:
                _min = deepcopy(current._value)
            current = current._next
            
        return _min

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
       
        current = self._front
        count = 0
        
        
        while current is not None and count < self._count:
            if key == current._value:
                count += 1
            current = current._next
            
        return count

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        current = self._front
        self._rear = current
        previous = None
        while current is not None:
            hold = current._next
            current._next = previous
            previous = current
            current = hold
        self._rear = previous
        
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        temp = List()
        self._rear = self._front
        current = self._front
        
        
        
        self.reverse_r_aux(current, temp)
        
        self._front = temp._front
        if self._rear is not None:
            self._rear._next = None
        return
    
    def reverse_r_aux(self, current, temp):
        if current is not None:
            self.reverse_r_aux(current._next, temp)
            temp.append(current._value)
        
        return
    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: sl.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        archive = []
        current = self._front
        previous = None
        
        while current is not None:
            if current._value not in archive:
                archive.append(current._value)
                previous = current 
            else:
                if previous is not None:
                    previous._next = current._next
                    self._count -= 1
                else:
                    self._front = self._front._next
                    if self._front is None:
                        self._rear = None   
            current = current._next  
        return      

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if i[0] < 0:
                # index is negative
                n = self._count + i[0]
            else:
                n = i[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (iterative version)
        Use: b = lst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            other_node = other._front

            while source_node is not None and source_node._value == other_node._value:
                source_node = source_node._next
                other_node = other_node._next

            identical = source_node is None
        return identical

    def is_identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        identical = True
        if self._count != other._count:
            identical = False
        else:
            current = self._front
            othercurrent = other._front
            self.identical_r_aux(othercurrent, current, identical)
        
        return identical
    
    def identical_r_aux(self, othercurrent, current, identical):
        if current is not None and current._value == othercurrent._value:
            self.identical_r_aux(othercurrent._next, current._next, identical)
        else:
            identical = False
        
        return
        
    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        split = self._count // 2 + self._count % 2
        counter = 0

        while self._front is not None:

            if counter < split:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            counter += 1
        return target1, target2

    def split_alt(self):
        """

        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:
            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        
        even = List()
        odd = List()
                
        self.split_alt_r_aux(even, odd)

        return even, odd
    
    def split_alt_r_aux(self, even, odd):
        
        if self._front is not None:
            even._move_front_to_rear(self)
            self.split_alt_r_aux(odd, even)
        
        return
    
    def _move_front_to_rear(self, source):
        
        assert source._front is not None, "Cannot move the front of an empty List"
        
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
    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        current = self._front
        count = 0
        previous = None
        
        previous, current, index = self._linear_search_r_aux(current, key, count, previous)

        return previous, current, index
    
    def _linear_search_r_aux(self, current, key, count, previous):
            
        if current is not None and current._value != key:
            previous = current
            count += 1
            previous, current, index = self._linear_search_r_aux(current._next , key, count, previous)
        
        else:
            index = count  
            if current is None:
                index = -1
        return previous, current, index
    
    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self.append(value)

            source1_node = source1_node._next
        return
    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front
        
        if not source2.is_empty():
            self.intersection_r_aux(source1_node, source2)
        
        return
    
    def intersection_r_aux(self, source1_node, source2):
        if source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self.append(value)

            self.intersection_r_aux(source1_node._next, source2)
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        archive = []
        current = source1._front
        while current is not None:
            if current._value not in archive:
                archive.append(current._value)
                self.append(current._value)
            current = current._next
        current = source2._front
        while current is not None:
            if current._value not in archive:
                archive.append(current._value)
                self.append(current._value)
            current = current._next
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front
        self.union_r_aux(source1_node)
        
        source2_node = source2._front
        self.union_r_aux(source2_node)
        
        return

    def union_r_aux(self, source_node):
        
        if source_node is not None:
            value = source_node._value
            _, current, _ = self._linear_search(value)
            
            if current is None:
                self.append(value)
            source_node = source_node._next
            
            self.union_r_aux(source_node)
            
            
        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        
        while self._front is not None:
            if self._front._value < key:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
                
        return target1, target2
        return


    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = lst.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        
        while self._front is not None:
            if func(self._front._value) is True:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
                
        return target1, target2

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        new_list = List()
        current  = self._front
        while current is not None:
            new_list.append(current._value)
            current = current._next
                    
        return new_list

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        # your code here
        return

    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs List to the front
        of the current List. Private helper method.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the rs List and
            its count is updated. The rs List front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, \
            "Cannot move the front of an empty List"

        # your code here
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._front is not None or source2._front is not None:
            if source1._front is not None:
                source1_node = source1._front
                source1._count-=1
                value = source1_node._value
                self.append(value)
                source1._front = source1._front._next
                
                
            if source2._front is not None:
                source2_node = source2._front
                value = source2_node._value
                self.append(value)
                source2._count-=1
                source2._front = source2._front._next
                
            
        source1._rear = None
        source2._rear = None
        source1._front = None
        source2._front = None
        source1._count = 0
        source2._count = 0
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
            
    def print_list(self):
        current = self._front
        
        while current is not None:
            print(current._value, end=" ")
            current = current._next
        print()
        return