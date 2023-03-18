def count_trees(graph):
    visited = set()
    count = 0
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)
    
    return count
