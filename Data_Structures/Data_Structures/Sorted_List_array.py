'''
------------------------------------------------------------------------
Array version of the Sorted_List_linked ADT.
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M02 28
------------------------------------------------------------------------
'''
from copy import deepcopy


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List_linked.
        Use: target = Sorted_List_linked()
        -------------------------------------------------------
        Returns:
            a Sorted_List_linked object (Sorted_List_linked)
        -------------------------------------------------------
        """
        self._values = []

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        Flag = False
        i = 0
        while Flag is False and i < len(self._values):
            if self._values[i] == key:
                Flag = True
            else:
                i += 1  

        return Flag

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        return deepcopy(self._values[i])

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        # Your code here

        return

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # Your Code Here
        return

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List_linked) to len(Sorted_List_linked) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        archive = []
        
        for i in self._values:
            if i not in archive:
                archive.append(deepcopy(i))
                
        self._values = deepcopy(archive)

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List_linked)
            source2 - an array-based list (Sorted_List_linked)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here

        return

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents 
                of source (Sorted_List_linked)
        -------------------------------------------------------
        """
        # Your code here

        return

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        count = 0
        Done = False
        
        i = 0
        while i < len(self._values) and Done is False:
            if self._values[i] == key:
                while i < len(self._values) and self._values[i] == key:
                    count += 1
                    i += 1
                Done = True
            else:
                i += 1

        return count


    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = 0
        Flag = False
        while Flag is False and i < len(self._values):
            if self._values[i] == key:
                Flag = True
            else:
                i += 1
        if Flag is False:
            i = -1

        return deepcopy(self._values[i])

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        i = 0
        Flag = False
        while Flag is False and i < len(self._values):
            if self._values[i] == key:
                Flag = True
            else:
                i += 1
        if Flag is False:
            i = -1
        
        return i
    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        l = 0
        h = len(self._values) - 1
        while l <= h:
            m = (h - l)//2 + l
            if self._values[m] > value:
                h = m - 1
            else:
                l = m + 1
        self._values.insert(l, deepcopy(value))

        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List_linked)
            source2 - an array-based list (Sorted_List_linked)
        Returns:
            None
        -------------------------------------------------------
        """
        source1.clean()
        source2.clean()
        
        for i in source1._values:
            if i in source2._values:
                self.insert(deepcopy(i))

        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """

        return not len(self._values)

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are is_identical, i.e. same values appear
        in the same locations in both lists. (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (Sorted_List_linked)
        Returns:
            identical - True if source contains the same values as target
                in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        
        return self._values == target._values

    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'

        return deepcopy(self._values[-1])

    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'

        return deepcopy(self._values[0])

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'



        return deepcopy(self._values[0])

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise 
                the last value in source, value is removed from source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = 0
        Flag = False
        while Flag is False and i < len(self._values):
            if self._values[i] == key:
                Flag = True
            else:
                i += 1
        if Flag is False:
            value = -1
        else:
            value = deepcopy(self._values.pop(i))

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'

        return deepcopy(self._values.pop(0))

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        Done = False
        
        i = 0
        while i < len(self._values) and Done is False:
            if self._values[i] == key:
                while i < len(self._values) and self._values[i] == key:
                    self._values.pop(i)
                Done = True
            else:
                i += 1
        return

    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List_linked)
            target2 - a new List with <= 50% of the original List (Sorted_List_linked)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        split = len(self._values) // 2
        count = 0
        while not self.is_empty():
            if count < split:
                target1.insert(deepcopy(self.pop(0)))
            else:
                target2.insert(deepcopy(self.pop(0)))
            count += 1
        return target1, target2


    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        Order of target1 and target2 is not significant. 
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List_linked)
            target2 - the odd indexed elements of the list (Sorted_List_linked)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        
        while not self.is_empty():
            target1.insert(deepcopy(self.pop(0)))
            if not self.is_empty():
                target2.insert(deepcopy(self.pop(0)))
        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # Your code here

        return

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Returns:
            target1 - a new List with values < key (Sorted_List_linked)
            target2 - a new List with values >= key (Sorted_List_linked)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        Flag = False
        while not self.is_empty() and Flag is False:
            if self.peek() < key:
                target1.insert(deepcopy(self.pop(0)))
            else:
                target2._values = self._values
                self._values = []
            
        return target1, target2

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List_linked)
            source2 - an array-based list (Sorted_List_linked)
        Returns:
            None
        -------------------------------------------------------
        """
        source1.clean()
        self._values = source1._values
        source2.clean()
        for i in source2._values:
            if i not in self._values:
                self.insert(deepcopy(i))

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
