from collections import deque

def count_nodes_at_level(root, level):
    queue = deque([(root, 0)])
    count = 0
    
    while queue:
        node, node_level = queue.popleft()
        
        if node_level == level:
            count += 1
        
        for neighbor in node.children:
            queue.append((neighbor, node_level + 1))
    
    return count
