from numpy import insert
from del17 import BinarySearchTree



def test_me() :
    bst = BinarySearchTree()
    inserts = [12, 5, 15, 3, 7, 13, 17, 1, 9, 14, 20, 8, 11, 18]
    for i in inserts:
        bst.insert(i)
    
    assert bst.delete(15)
    assert bst.delete(12)  # Ultimate test: remove root node :-)
    assert not bst.delete(12)  # Should return False
