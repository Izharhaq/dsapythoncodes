'''
1. 1. Define a class Queue to implement queue data structure using singly linked list concept. 
    Define __init__() method to initialise front and rear reference vaiable; and item_count variable
    to keep track of number of element of the queue.
2. Define a method is_empty() to check if the queue is empty in Queue class.
3. In Queue class, define enqueue() method to add data at the rear end of the queue.
4. In Queue class, define dequeue() method to remove front element from the queue.
5. In Queue class, define get_front() method to return front element of the queue.
6. In Queue class, define get_rear() ,method to return rear element of the queue.
7. In queue class, define size() method to return size of the queue that is number of items presents in the queue.

'''
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front==None
    def enqueue(self, data):
        n=Node(data)
        if self.is_empty:
            self.front=n
            self.rear=n
        self.item_count+=1
