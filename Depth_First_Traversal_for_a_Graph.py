def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            print(current)
            
            for neighbor in graph[current]:
                stack.append(neighbor)
