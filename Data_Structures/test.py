'''
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M02 25
------------------------------------------------------------------------
'''
from BST_linked import *

tree = BST()
bank = [6,4,8,5,9,7]
for i in bank:
    tree.insert(i)
    print(tree._root._height)

print(tree.contains(8))
tree.remove(8)
print(tree.contains(8))
print(tree.contains(7))
