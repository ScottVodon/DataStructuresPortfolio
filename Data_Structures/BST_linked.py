'''
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M03 11
------------------------------------------------------------------------
'''
# Imports
from copy import deepcopy
from Queue_array import Queue

class _BST_Node:
    def __init__(self, value):
        self._value = deepcopy(value)
        self._left = None #Left child
        self._right = None  #Right Child
        self._height = 1

    def _update_height(self):
        if self._left is None:      #Find height of left child
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:     #Find height of right child
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1   #Height is the greatest child height +1
        return

    def __str__(self):

        return "h: {}, v: {}".format(self._height, self._value)


class BST:
    def __init__(self):
        self._root = None
        self._count = 0

    def is_empty(self):
        return self._root is None

    def __len__(self):
        return self._count

    def insert(self, value):
        node = _BST_Node(value)
        if self._root == None:
            self._root = node
            inserted = True
        else:
            inserted = self._insert_aux(self._root, node,value)
        return inserted

    def insert_node(self, node):
        if self._root == None:
            self._root = node
        inserted = self._insert_aux(self._root, node, value)
        return inserted


    def _insert_aux(self, pointer, node, value):
        #Resursive cases
        if pointer._value > value: # check the left subtree.
            if pointer._left == None:  # end case
                pointer._left = node
                inserted = True
            else:
                inserted = self._insert_aux(pointer._left, node, value)
        elif pointer._value < value: # check the right subtree.
            if pointer._right == None: # end case
                pointer.right = node
                inserted = True
            else:
                inserted = self._insert_aux(pointer._right, node, value)
        else: #Catch case: value is already in the BST.
            inserted = False

        pointer._update_height()
        return inserted

    def retrieve(self, key):
        node = self._root
        value = None

        while node is not None and value is None:
            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                value = deepcopy(node._value)
        return value

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """

        # your code here

    def remove(self, key):
        assert self._root is not None, "Cannot remove from an empty BST"
        parent = None
        dir = None
        if self._root._value == key:
            value = self._root._value
            self._root = None
            return true
        else:
            return self._remove_aux(self._root, key)

    def _remove_aux(self, head, key):
        if key < head._value:
            #Search the left child
            if head._left == None:
                return False    # key not found
            elif head._left._value == key:
                self._delete_node_left(head)
                self._count -= 1
            else:
                value = self._remove_aux(node, node._left, key)
        elif key > head._value:
            #Search the right child
            if head._right == None:
                return False    # key not found
            elif head._left._value == key:
                self._delete_node_right(head)
                self._count -= 1
            else:
                value = self._remove_aux(node, node._left, key)
        else:
            return False

        head._update_height()
        return False

    def _delete_node_left(self, head):
        target = head._left
        head._left = target._left
        if target._right is not None:
            insert_node(target._right)
        self.mem_dump(target)
        return

    def _delete_node_right(self, head):
        target = head._right
        head._right = target._right
        if target._left is not None:
            insert_node(target._left)
        self.mem_dump(target)
        return


    def mem_dump(self, node):
        node._value = None
        node._left = None
        node._right = None
        node._height = None

    def contains(self, key):

        value = self.retrieve(key)
        return value is not None

    def is_identical(self, other):

        if self._count != other._count:
            identical = False
        else:
            identical = self._is_identical_aux(self._root, other._root)

        return identical


    def _is_identical_aux(self, node1, node2):

        if node1 is None and node2 is None:
            result = True
        elif node1 is not None and node2 is not None and node1._value == node2._value and node1._height == node2._height:
            result = self._is_identical_aux(node1._left, node2._left) and self._is_identical_aux(node1._right, node2._right)
        else:
            result = False

        return result

    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        # your code here

    def parent_i(self, key):
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        node = self._root
        parent = None
        found = False

        while node is not None and found is False:

            if key < node._value:
                parent = node
                node = node._left
            elif key > node._value:
                parent = node
                node = node._right
            else:
                found = True

        if parent is None or not found:
            value = None
        else:
            value = deepcopy(parent._value)
        return value

    def parent_r(self, key):
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        return self._parent_aux(self._root, key, None)

    def _parent_aux(self, node, key, parent):

        if node is None:
            value = None
        elif key < node._value:
            value = self._parent_aux(node._left, key, node)
        elif key > node._value:
            value = self._parent_aux(node._right, key, node)
        elif parent is None:
            value = None
        else:
            value = deepcopy(parent._value)
        return value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        node = self._root

        while node._right is not None:
            node = node._right

        value = deepcopy(node._value)
        return value


    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"


        # your code here

    def min(self):
        assert self._root is not None, "Cannot find minimum of an empty BST"

        node = self._root

        while node._left is not None:
            node = node._left

        value = deepcopy(node._value)
        return value

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here


    def leaf_count(self):
        node = self._root

        if node is None:
            count = 0
        else:
            count = self._leaf_count_aux(node)

        return count

    def _leaf_count_aux(self, node):

        if node._left is None and node._right is None:
            count = 1
        else:
            count = self._leaf_count_aux(node._left) + self._leaf_count_aux(node._right)

        return count


    def two_child_count(self):
        node = self._root

        count = self._two_child_count_aux(node)

        return count

    def _two_child_count_aux(self, node):
        count = 0
        if node is not None:
            if not node._right and node._left:
                count = 3
        else:
            count = 0
        return count

    def one_child_count(self):

        node = self._root
        if node is None:
            count = 0
        else:
            count = self._one_child_count_aux(node, 0)
        return count

    def _one_child_count_aux(self, node, count):
        if node._left is not None and node._right is None:
            # General case: node has a single left child.
            count += 1
            count = self._one_child_count_aux(node._left, count)
        elif node._left is None and node._right is not None:
            # General case: node has a single right child.
            count += 1
            count = self._one_child_count_aux(node._right, count)

        return count

    def node_counts(self):
        node = self._root
        zero, one, two = self.node_counts_aux(node)
        return zero, one, two

    def node_counts_aux(self, node):
        zero = one = two = 0

        if node is not None:
            zero = (
                1
                + self.node_counts_aux(node._left)[0]
                + self.node_counts_aux(node._right)[0]
            )
            if not node._right and node._left:
                two = (
                    1
                    + self.node_counts_aux(node._left)[2]
                    + self.node_counts_aux(node._right)[2]
                )
            if node._left or node._right:
                one = (
                    1
                    + self.node_counts_aux(node._left)[1]
                    + self.node_counts_aux(node._right)[1]
                )
        return zero, one, two

    def is_balanced(self):

        node = self._root

        balanced = False

        if node is None:
            balanced = True
        elif node._left is None and node._right is None:
            balanced = True
        elif node._left is None or node._right is None:
            balanced = False
        elif node._left._height - node._right._height <= 1:
            balanced = True

        return balanced

    def _is_balanced_aux(self, node):

        if node is not None:
            if node._left is not None and node._right is not None:
                if (
                    node._left._height == node._right._height
                    or node._left._height + 1 == node._right._height
                    or node._left._height - 1 == node._right._height
                ):
                    balanced = self._is_balanced_aux(
                        node._left
                    ) and self._is_balanced_aux(node._right)
            else:
                balanced = False
        return balanced

    def height(self):

        node = self._root

        if node is None:
            height = 0
        else:
            height = node._height
        return height


    def is_valid(self):

        node = self._root
        valid = True

        if node is not None:
            valid = self._is_valid_aux(node)

        return valid

    def _is_valid_aux(self, node):

        valid = True

        if node is None:
            valid = True

        if node._left is not None and node._left._value <= node._value:
            valid = self._is_valid_aux(node._left)

        if node._right is not None and node._right._value >= node._value:
            valid = self._is_valid_aux(node._right)

        return valid


    def inorder(self):

        node = self._root

        a = []

        self._inorder_aux(node, a)

        return a

    def _inorder_aux(self, node, a):

        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(node._value)
            self._inorder_aux(node._right, a)

        return a

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """

        a = []

        if self._root is not None:
            a = self._preorder_aux(self._root)

        return a

    def _preorder_aux(self,parent):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = [parent._value]

        if parent._left is not None:
            list_left = self._preorder_aux(parent._left)
            a = a + list_left
        if parent._right is not None:
            list_right = self._preorder_aux(parent._right)
            a = a + list_right
        return a


    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """

        a = []

        if self._root is not None:
            a = self._postorder_aux(self._root)

        return a

    def _postorder_aux(self,parent):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []


        if parent._left is not None:
            list_left = self._postorder_aux(parent._left)
            a = list_left
        if parent._right is not None:
            list_right = self._postorder_aux(parent._right)
            a = a + list_right
        a.append(parent._value)

        return a


    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        values = []
        q = Queue()

        if self._root is not None:
            q.insert(self._root)

        while not q.is_empty():
            node = q.remove()
            values.append(deepcopy(node._value))
            if node._left is not None:
                q.insert(node._left)
            if node._right is not None:
                q.insert(node._right)

        return values

    def total_depth(self):
        """
        ---------------------------------------------------------
        Returns the total depth of a bst.
        ---------------------------------------------------------
        Returns:
            the total depth count - i.e. the sum of all the node depths
            in the tree (int)
        ---------------------------------------------------------
        """

        # your code here

    def __iter__(self):
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
