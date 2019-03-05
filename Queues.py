"""
Python Refresh:
    - python uses self. not this.
    - python uses Capital T and F for boolean
    - you can return more than one data type in a function; not strictly typed?
    - use \"\"\" comment \"\"\" so that when you invoke a function the description of the function will show  ; Code definition (Peek and hover definition, View signatures)
    - add if __name__ == "__main__": main() so that when you import this file in another module the code from this file won't run there in that new module using this module
"""
"""
Resources:
    - https://developers.google.com/edu/python/lists
    - https://www.pythoncentral.io/use-queue-beginners-guide/
    -https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it
"""
class Queue:
    
    def __init__(self):
        """ Constructor sets up a list """
        self.queue = list()
    
    
    def enqueue(self, data):
        """ A function to add data to the queue to maintain FIFO (First in First out) order """
        # Check to see if you want to add duplicates 
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False

    
    def dequeue(self):
        """ A function to remove data from the queue maintaining Fifo Order """
        if len(self.queue) > 0:
            return self.queue.pop()
        return "Queue is Empty"
    
    
    def printQueue(self):
        """ Prints / Returns the queue """
        return self.queue

    def length(self):
        return len(self.queue)

def main():
    queue = Queue()
    queue.enqueue("David")
    queue.enqueue("Marc")
    queue.enqueue("Matt")
    print(queue.length())
    firstInLine = queue.dequeue()
    print(queue.length())
    print(firstInLine)
    print(queue.printQueue())
    print("From Queues.py")
   
if __name__ == "__main__":
    main()
