"""
This file contains function headers for various pathfinding algorithms.
Students are responsible for implementing these algorithms.

IMPORTANT:
- Do NOT include any graphical elements in this file.
- Use `update_visualization function` to update the visualization.
"""

# imports are here 


def heuristic(cell, goal):
    """
    Computes the heuristic distance between two points.
    """
    pass

def A_star(graph, start, goal, pathMap, ax2, ax3):
    """
    Arguments:
    - graph: The adjacency list representing the maze.
    - start: The starting position 
    - goal: The goal position 
    - pathMap: The matrix representation of the maze.
    - ax2: The visualization axis for search progress.
    - ax3: The visualization axis for the final path.
    """
    pass

def bfs(graph, start, goal, pathMap, ax2, ax3):
    """
    Arguments:
    - graph: The adjacency list representing the maze.
    - start: The starting position 
    - goal: The goal position
    - pathMap: The matrix representation of the maze.
    - ax2: The visualization axis for search progress.
    - ax3: The visualization axis for the final path.
    """
    pass

def dfs(graph, start, goal, pathMap, ax2, ax3):
    """
    Arguments:
    - graph: The adjacency list representing the maze.
    - start: The starting position 
    - goal: The goal position 
    - pathMap: The matrix representation of the maze.
    - ax2: The visualization axis for search progress.
    - ax3: The visualization axis for the final path.
    """
    pass

def greedy(graph, start, goal, pathMap, ax2, ax3):
    """
    Arguments:
    - graph: The adjacency list representing the maze.
    - start: The starting position 
    - goal: The goal position 
    - pathMap: The matrix representation of the maze.
    - ax2: The visualization axis for search progress.
    - ax3: The visualization axis for the final path.
    """
    pass

def depth_limited_search(graph, current, goal, depth, came_from, pathMap, ax2, expanded_nodes):
    """
    Arguments:
    - graph: The adjacency list representing the maze.
    - current: The current position
    - goal: The goal position 
    - depth: The current depth limit
    - came_from: Dictionary tracking visited nodes.
    - pathMap: The matrix representation of the maze.
    - ax2: The visualization axis for search progress.
    - expanded_nodes: The count of expanded nodes.
    """
    pass

def iterative_deepening_search(graph, start, goal, pathMap, ax2, ax3):
    """
    Arguments:
    - graph: The adjacency list representing the maze.
    - start: The starting position 
    - goal: The goal position 
    - pathMap: The matrix representation of the maze.
    - ax2: The visualization axis for search progress.
    - ax3: The visualization axis for the final path.
    """
    pass