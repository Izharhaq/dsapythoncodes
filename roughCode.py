"""
1. Define a class Node to describe a node of a singly linked list.
2. Define a class SLL to implement Singly Linked List with __init__() method 
   to create and initialise start reference variable.
3. Define a method is_empty() to check if the linked list is empty in SLL class.
4. In class SLL, define a method insert_at_start() to insert a element at the starting of the list.
5. In class SLL, define a method insert_at_last() to insert a element at the end of the list.
6. In class SLL, define a method search() to find the node with the specified element value.
7. In class SLL, define a insert_after() to insert a new node after a given node of the list.
8. In class SLL, define a print_list() method to print all the elelemt of the list.
9. In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
10. In class SLL, define a method delete_first() to delete first element from the list.
11. In class SLL, define a method delete_last() to delete last element from the list.  
12. In class SLL, define a method delete_item() to delete sepcified element from the list.
"""

class Node:
    def __init__(self, start=None,next=None):
        self.start=start
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None     #self.next=None,    #self.count_item=None
    def insert_at_start(self,data):
        n=Node(data,self.start)


#****** Driver Code *********

mylist=SLL()
mylist.insert_at_start(10)
print()