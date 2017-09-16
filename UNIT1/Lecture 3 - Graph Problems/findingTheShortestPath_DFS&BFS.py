# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:02:31 2017

@author: Administrator
"""

def printPath(path):
    '''Assumes path is a list of nodes'''
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += ' --> '
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    '''
    Assumes graph si a Digraph; start and end are nodes; path and shortest are 
        list of nodes
    Returns a shortest path from start to end in graph
    '''
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path    
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest

def BFS(graph, start, end, toPrint = False):
    """
    Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph
    """
    pathQueue = [[start]]
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None
    
def shortestPath(graph, start, end, searchType, toPrint = False):
    '''
    Assumes graph is a Digraoh; start and end are nodes
    Returns a shortest path from start to end in graph
    '''
    try:
        return searchType(graph, start, end, [], None, toPrint)
    except TypeError:
        return searchType(graph, start, end, toPrint)

def testSP(source, destination, searchType):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), 
                      searchType, toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to', destination,
              'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


    
testSP('Chicago', 'Boston', BFS)
#testSP('Boston', 'Phoenix', BFS)