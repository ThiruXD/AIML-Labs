from collections import deque

# Define the undirected graph
graph = {
    "Alice": ["Charlie", "David"],
    "Bob": ["Emma", "Fred"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"]
}

def bfs(graph, start, goal):
    """Breadth-First Search to find the shortest path."""
    if start == goal:
        return [start]
    
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    found = False
    while queue:
        current = queue.popleft()
        if current == goal:
            found = True
            break
        # Visit neighbors in alphabetical order
        for neighbor in sorted(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current
    
    if not found:
        return None
    
    # Reconstruct path
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent.get(curr)
    path.reverse()
    return path

def dfs(graph, start, goal):
    """Depth-First Search (with alphabetical neighbor ordering)."""
    if start == goal:
        return [start]
    
    stack = [start]
    visited = set()
    parent = {start: None}
    
    found = False
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        
        if current == goal:
            found = True
            break
        
        # Neighbors in alphabetical order (reverse push so first alpha explored first)
        neighbors = sorted(n for n in graph.get(current, []) if n not in visited)
        for neighbor in neighbors[::-1]:  # Ensures alphabetical exploration priority
            stack.append(neighbor)
            parent[neighbor] = current
    
    if not found:
        return None
    
    # Reconstruct path
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent.get(curr)
    path.reverse()
    return path

# Run the simulations
bfs_path = bfs(graph, "Alice", "Bob")
dfs_path = dfs(graph, "Alice", "Bob")

print("BFS Path from Alice to Bob:", " -> ".join(bfs_path) if bfs_path else "No path found")
print("DFS Path from Alice to Bob:", " -> ".join(dfs_path) if dfs_path else "No path found")
