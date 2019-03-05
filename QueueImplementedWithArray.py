"""
Resources: 
    - https://www.pythoncentral.io/use-queue-beginners-guide/
"""
class Queue:
    def __init__(self, maxSize):
        """
        Queue is implemented using a list data structure
        
        Class Variables:
        -   Tail pointer will always point to the next available space
        -   When the queue is full, the tail pointer will be greater than the declared size.
        -   Head pointer will point to the element to be dequeued next.
        
        Note: 
            When dequeuing no element will be actually removed from the queue
            This is because once an element is removed, the list automatically shifts all the other elements by one position to the left.
            This means that the position 0 will always contain an element, which is not how an actual queue works.
        """
        self.queue = list()
        self.maxSize = maxSize
        self.tail = 0  
        self.head = 0 

    def size(self):
        return self.tail - self.head
    
    def resetQueue(self):
        self.head = self.tail = 0
        self.queue = list()

    def enqueue(self, data):
        if self.size() < self.maxSize:
            self.queue.append(data)
            self.tail += 1
            return True
        return "Queue is full"

    def dequeue(self):
        if self.size() > 0:
            dataToReturn = self.queue[self.head]
            self.head += 1
            return dataToReturn
        else:
            self.resetQueue()
            return "Empty queue"

def main():
    testQueue = Queue(10)
    testQueue.enqueue(1)
    testQueue.enqueue(2)
    testQueue.enqueue(3)
    print(testQueue.dequeue())
    print(testQueue.dequeue())
    print(testQueue.size())  
    print(testQueue.dequeue()) 
    print(testQueue.size()) 

if __name__ == "__main__":
    main()