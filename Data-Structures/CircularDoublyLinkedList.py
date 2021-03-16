# Author: Daniel Brown
# Date: February 15, 2020
#
# This is an implementation of a circular doubly linked list

class CircularDoublyLinkedList:
  # nested _Node class
  class _Node:
    #Lightweight, nonpublic class for storing a doubly linked node.
    __slots__ = '_element', '_prev', '_next'            

    def __init__(self, element, prev, next):            
      self._element = element                           
      self._prev = prev                                 
      self._next = next                                 

  # list constructor
  def __init__(self):
    """Create an empty list."""
    self._start = None
    self._size = 0                                      

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  def _insert_between(self, e, predecessor, successor):
    # Add element between two existing nodes and return new node
    newest = self._Node(e, predecessor, successor)      
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             
    node._prev = node._next = node._element = None      
    return element                                      
 
  def insertBeforeHeader(self, e):
    if self._start == None:
      head = self._Node(0, None, None)
      head._element = e
      head._prev = head
      head._next = head
      self._start = head
    else:
      last = self._start._prev
      head = self._Node(0, None, None)
      head._element = e
      head._next = self._start
      head._prev = last
      last._next = head
      self._start._prev = head
    self._size += 1
    

  def insertAtEnd(self, e):
    if self._start == None:
      head = self._Node(0, None, None)
      head._element = e
      head._prev = head
      head._next = head
      self._start = head
    else:
      last = self._start._prev
      new = self._Node(0, None, None)
      new._element = e
      new._next = self._start
      self._start._prev = new
      new.prev = last
    self._size += 1

  def displayForward(self):
    walker = self._start
    while walker._next != self._start:
      print(walker._element, end=" ")
      walker = walker._next
    print(walker._element)
    
  def displayBackward(self):
    walker = self._start._prev
    while walker._prev != self._start._prev:
      print(walker._element, end=" ")
      walker = walker._prev
    print(walker._element)

# test the program
if __name__ == '__main__':
  cirLink = CircularDoublyLinkedList()
  cirLink.insertBeforeHeader(1)
  cirLink.insertBeforeHeader(2)
  cirLink.insertBeforeHeader(3)
  cirLink.insertBeforeHeader(4)
  cirLink.insertBeforeHeader(5)
  cirLink.displayForward()
  cirLink.displayBackward()
