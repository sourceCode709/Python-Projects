# Author: Daniel Brown
# Date: February 8, 2020

# Array based binary tree implementation


class ArrayBinaryTree:
  def _parentIdex(self, j):
    return (j-1) // 2

  def _leftIdex(self, j):
    return 2*j
  
  def _rightIdex(self, j):
    return 2*j + 1

  def _hasLeft(self, j):
    return self._leftIdex(j) <= self._size    
  
  def _hasRight(self, j):
    return self._rightIdex(j) <= self._size   

  def _childrenIdex(self,idx):
    return [self._leftIdex(idx),self._rightIdex(idx)]
    
  def __init__(self):
    self._data = [None] * 10
    self._size = 0                        
    self._root = 1                         
    self._left = None
    self._right = None
  
  def size(self):
    return self._size

  def isEmpty(self):
    return self._size == 0
  
  def root(self):
    return self._data[self._root]

  def parent(self,idx):
    return None if idx == 1 else self._data[int(idx/2)]

  def children(self,idx):
    return [self.left(idx),self.right(idx)]

  def left(self,idx):
    if self._hasLeft():
      return self._left

  def right(self,idx):
    if self._hasRight():
      return self._right

  def isInternal(self,idx):
    if self._hasLeft() or self._hasRight():
      return True
    else:
      return False
      
  def isExternal(self,idx):
    if not self._hasLeft() and not self._hasRight():
      return True
    else:
      return False
  
  def setRoot(self,cur, v):
    if self._data[cur] == None:
      print("The root node does not exist")
      return None
    self._data[cur] = v
    return cur


  def setLeft(self,cur,v):
    if self._data[cur] == None:
      return None
    else:
      self._data[cur] = v
      self._left = curr
    return self._left
    

  def setRight(self,cur,v):
    if self._data[cur] == None:
      return None
    else:
      self._data[cur] = v
      self._right = cur
    return self._right

  def insertRoot(self, v):
    if not self._data[self._root] == None:
      print("The root node already exists")
      return None
    self._data[self._root] = v
    self._size += 1
    return 1

  # recursively insert to the left node.
  def insertLeft(self,cur,v):
    if not self._data[self._left] == None:
      self._left = self._left._left
      insertLeft(self._left,v)
    return setLeft(self._left,v)
      
      
  # insert to the right node.
  def insertRight(self,cur,v):
    if not self._data[self._right] == None:
      self._right = self._right._right
      insertRight(self._right,v)
    return setRight(self._right,v)

  # print an inorder iteration of nodes in the tree
  def inOrder(self):
    if not self.isEmpty():
      for p in self._subtree_inorder(self._root):
        print(p)
  
  # generate an inorder iteration of nodes in subtree rooted at p
  def _subtree_inorder(self, p):
    if self._hasLeft(p):         
      for other in self._subtree_inorder(self._leftIdex(p)):
        yield other
    yield self._data[p]            
    if self._hasRight(p):         
      for other in self._subtree_inorder(self._rightIdex(p)):
        yield other

  # print a preorder of nodes in the tree
  def preOrder(self):
    if not self.isEmpty():
      for p in self._subtree_preorder(self._root):  
        print(p)

  # generate a preorder iteration of positions in subtree rooted at p
  def _subtree_preorder(self, p):
    if p:
      print(self._data[p])
      _subtree_preorder(p._left())
      _subtree_preorder(p._right())
    
  # print a postorder of nodes in the tree
  def postOrder(self):
    if not self.isEmpty():
      for p in self._subtree_postorder(self._root):  # start recursion
        print(p)
 
  # generate a postorder iteration of node in subtree rooted at p
  def _subtree_postorder(self, p):
    if p:
      _subtree_postorder(p._left())
      _subtree_postorder(p._right())
      print(self._data[p])
  
  def printTreeArray(self):
    print(self._data)

  def _resize(self, cap):                  
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                      
    self._data = [None] * cap             
    for k in range(self._size):           
      self._data[k] = old[k]              

# testing code
if __name__ == '__main__':
  bt = ArrayBinaryTree()
  bt.insertRoot(1)
  bt.insertLeft(1,2)
  bt.insertRight(1,3)
  bt.insertLeft(1,4)
  bt.insertRight(2,5)
  bt.insertLeft(3,6)
  bt.insertRight(1,7)
  bt.printTreeArray()
  bt.inOrder()
  bt.postOrder()
  bt.preOrder()
  
