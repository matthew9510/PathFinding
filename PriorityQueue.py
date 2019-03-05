"""
Resources:
    - https://www.geeksforgeeks.org/priority-queue-in-python/
"""

class PriorityQueue(object):
    """
    Priority Queue is an extension of the queue with following properties.
    - An element with high priority is dequeued before an element with low priority.
    - If two elements have the same priority, they are served according to their order in the queue.
    """    

    def __init__(self):
        self.queue = []

    def __str__(self):
        """ To string operation """
        return " ".join([str(i) for i in self.queue])

    def isEmpty(self): 
        """ Method checking if the queue is empty """
        return len(self.queue) == len([])
    
    def insert(self, data):
        """ Method to Insert data into the priority queue """ 
        self.queue.append(data)
    
    def delete(self):
        """ Method to pop the element of the queue with the highest priority"""
        try:
            """ Find max priority """
            maxIndex = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[maxIndex]:
                    maxIndex = i
                itemToRemove = self.queue[maxIndex]
                del self.queue[maxIndex]
                return itemToRemove
        except IndexError:
            print() # prints error
            exit()
  
          
if __name__ == '__main__': 
    myQueue = PriorityQueue() 
    var = 12
    myQueue.insert(var) 
    myQueue.insert(1) 
    myQueue.insert(14) 
    myQueue.insert(7) 
    print(myQueue) # __str__ method handles this          
    while not myQueue.isEmpty(): 
        print(myQueue.delete()) 
