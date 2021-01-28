'''
------------------------------------------------------------------------
utilities
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M01 21
------------------------------------------------------------------------
'''
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from List_linked import List
from Sorted_List_linked import Sorted_List

def array_to_stack(s, a):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack, 
    first value in source is on top of stack.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Parameters:
        s - a Stack object (Stack)
        a - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for i in range(len(a)):
        popped = a.pop()
        s.push(popped)

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        popped =  stack.pop()
        target.append(popped)
    
    target.reverse()
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and 
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    
    for i in source:
        s.push(i)
        
    print(s.is_empty())
    print(s.peek())
    print(s.pop())
    
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue, 
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for i in range(len(source)):
        popped = source.pop(0)
        queue.insert(popped)
        
def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        popped =  queue.remove()
        target.append(popped)
    
    
def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq, 
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        pq.insert(source.pop(0))
        
    return
def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        popped =  pq.remove()
        target.append(popped)
        
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    -------------------------------------------------------
    """
    q = Queue()
    
    print(Queue.is_empty(q))
    
    array_to_queue(q, a)
    
    print(Queue.is_empty(q))
    
    Queue.insert(q, 99)
    
    x = Queue.remove(q)
    print(x)
    
    print(Queue.peek(q))
    print(len(q))
    
    

    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
    a - list of data (list of ?)
    Returns:
    the methods of Priority_Queue are tested for both empty and 
    non-empty priority queues using the data in a:
    is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("Is empty?: " + Priority_Queue.is_empty(pq))
    
    array_to_pq(pq, a)
    
    print("Is empty?: " + Priority_Queue.is_empty(pq))
    
    Priority_Queue.insert(pq, 99)
    
    x = Priority_Queue.remove(pq)
    print("Removed MOvie:" + x)
    
    print(Priority_Queue.peek(pq))
    print(len(pq))

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist, 
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        llist.append(source.pop(0))
        
    return
def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        target.insert(0,llist.pop())
    
    return
def list_to_linked_list(llist, linked):
    
    """
    -------------------------------------------------------
    takes a standard list and turns it into a linked list
    -------------------------------------------------------
    Parameters:
        llist - list of data (list of ?)
    Returns:
        linked - a linked list of data
    -------------------------------------------------------
    """
    for i in llist:
        linked.append(i)
    
    return 
def list_to_s_linked_list(llist, s_linked):
    
    """
    -------------------------------------------------------
    takes a standard list and turns it into a linked list
    -------------------------------------------------------
    Parameters:
        llist - list of data (list of ?)
    Returns:
        linked - a linked list of data
    -------------------------------------------------------
    """
    for i in llist:
        s_linked.insert(i)
    
    return 

def list_to_sorted_list(llist, target):
    for i in llist:
        target.insert(i)
    return
        
        
    

