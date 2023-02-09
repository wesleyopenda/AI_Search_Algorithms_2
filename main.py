class Environment():
    myGraph = {'1': set(['2','4']),
               '2': set(['1','5','3']),
               '3': set(['2','6']),
               '4': set(['1','5','7']),
               '5': set(['2', '4', '8','6']),
               '6': set(['3', '5', '9']),
               '7': set(['4', '8']),
               '8': set(['7', '5', '6']),
               '9': set(['8', '6']),}

    cost = {str(['1','2']): '3', str(['1','4']): '5',
            str(['2','1']): '3', str(['2','5']): '7', str(['2','3']): '5',
            str(['3','2']): '5', str(['3','6']): '9',
            str(['4','1']): '5', str(['4','5']): '9', str(['4','7']): '11',
            str(['5','2']): '7', str(['5','4']): '9', str(['5','6']): '11', str(['5','8']): '13',
            str(['6','3']): '9', str(['6','5']): '11', str(['6','9']): '15',
            str(['7','4']): '11', str(['7','8']): '15',
            str(['8','5']): '13', str(['8','7']): '15', str(['8','9']): '17',
            str(['9','6']): '15', str(['9','8']): '17'}

    start = '1'
    goal = '7'

class Agent(Environment):
    # depth first search
    def DFS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack: # if there are things in the stack...
            (vertex, path) = stack.pop() # remove things from the stack
            for next in graph[vertex] - set(path): # go to places not been in before
                if next == goal:
                    p.append(path + [next]) # keep a record of where been
                else:
                    stack.append((next, path + [next]))
        return p

    # breadth first search
    def BFS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack: # if there are things in the stack...
            (vertex, path) = stack.pop(0) # remove things from the stack
            for next in graph[vertex] - set(path): # go to places not been in before
                if next == goal:# if reached where you are going
                    p.append(path + [next]) # keep a record of where been
                    return p
                else:
                    stack.append((next, path + [next]))
        return p

    def get_cost(path_to_cost):
        path_cost = 0
        i = 0 # counter to manipulate a loop
        while i < len(path_to_cost) - 1: # -1 so it doesnt go out of bounds, while is to add up all the costs
            l = []
            l.append(path_to_cost[i]) # first node
            l.append(path_to_cost[i + 1]) # second node
            path_cost = path_cost + int(Environment.cost[str(l)]) # read cost between the nodes (1 and 2)
            i += 1
            return path_cost

    # uniform cost search
    def UCS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        least_cost = 1000 # goot to start high so you cut it down
        while stack: # if there are things in the stack...
            (vertex, path) = stack.pop() # remove things from the stack
            for next in graph[vertex] - set(path): # go to places not been in before
                if next == goal: # if reached where you are going, calculate cost
                    path_cost = Agent.get_cost(path + [next]) # to describe the journey covered
                    print('UCS path:', path + [next], 'Path cost:', path_cost)
                    print()
                    # out of all journeys cost, which is the best/ cheapest?
                    if path_cost < least_cost:
                        least_cost = path_cost
                        p = path + [next] # overides whatever was there
                   # p.append(path + [next]) # keep a record of where been
                else:
                    stack.append((next, path + [next]))
        return p

    def __init__(self, Environment):
        print('DFS', Agent.DFS(Environment.myGraph, Environment.start, Environment.goal)) # calling the function
        print('BFS', Agent.BFS(Environment.myGraph, Environment.start, Environment.goal))
        print('UCS', Agent.UCS(Environment.myGraph, Environment.start, Environment.goal))

theEnvironment = Environment()
theAgent = Agent(theEnvironment)
