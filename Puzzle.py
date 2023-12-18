# Author: Chukwuhalim Uzodike
# GitHub username: HalimUzodike
# Course: CS325 - Analysis of Algorithms
# Assignment: Graph Algorithms II
# Date: 05/29/2023
# Description: This program contains a function solve_puzzle, which implements Prim's algorithm for finding the minimum spanning tree of a graph.

from collections import deque

def solve_puzzle(puzzle, source, destination):
    """
    This function solves a 2-D puzzle of size M x N using BFS.
    The time complexity of this algorithm is O(M x N).
    """
    M, N = len(puzzle), len(puzzle[0])
    directions = [(0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]  # (dx, dy, direction)

    visited = [[False]*N for _ in range(M)]     # visited[i][j] is True if (i, j) has been visited
    prev = [[None]*N for _ in range(M)]         # prev[i][j] stores the previous cell in the path to (i, j)
    
    queue = deque([source])                 # queue of cells to visit
    visited[source[0]][source[1]] = True    # mark source as visited

    while queue:
        x, y = queue.popleft()          # pop the next cell to visit
        if (x, y) == destination:       # destination reached
            path = [(x, y)]
            dirs = []        
            while prev[x][y] is not None:       # follow the path backwards from destination to source
                x, y, d = prev[x][y]
                path.append((x, y))
                dirs.append(d)
            path.reverse()
            dirs.reverse()          
            return path, ''.join(dirs)      # return the path and the directions taken to get to the destination
        
        for dx, dy, d in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and puzzle[nx][ny] == '-':       # if the cell is valid
                queue.append((nx, ny))
                visited[nx][ny] = True          # mark the cell as visited  
                prev[nx][ny] = (x, y, d)        # store the previous cell in the path to (nx, ny)
    return None, None

