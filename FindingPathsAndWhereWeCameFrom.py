import Queues 

class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data
 

def generatePath(goal, cameFrom, start):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = cameFrom[current]
    path.append(start)
    return path

def main():
    frontier = Queues.Queue()
    cameFrom = {}
    start = Node(0)
    frontier.enqueue(start)
    cameFrom[start] = None

    while frontier.length() is not 0:
        current = frontier.dequeue()
        for next in graph.neighbors(current):
            #if visited[next] is not True:
            if next not in cameFrom:
                cameFrom[next] = current
                frontier.enqueue(next)
    
    goal = Node(1)
    generatePath(goal,cameFrom, start)


if __name__ == "__main__":
    main()


