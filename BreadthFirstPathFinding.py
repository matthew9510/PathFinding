import Queues 

"""
Resources: 
    - https://www.redblobgames.com/pathfinding/a-star/introduction.html
"""

class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data
 
def main():
    frontier = Queues.Queue()
    visited = {}
    start = Node(0)
    frontier.enqueue(start)
    visited[start] = True
    goal = Node(2)

    while frontier.length() is not 0:
        current = frontier.dequeue()
    
        # We can stop expanding the frontier as soon as we’ve found our goal. 
        if current == goal:
            break

        for next in graph.neighbors(current):
            # if visited[next] is not True:
            if next not in visited:
                visited[next] = True
                frontier.enqueue(next)
            

if __name__ == "__main__":
    main()


