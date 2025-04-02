def iddfs(grid, start, target):
    max_depth = len(grid) * len(grid[0])
    
    def dfs(x, y, depth, path, visited, limit):
        if (x, y) == target:
            return True
        if depth >= limit:
            return False
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                path.append((nx, ny))
                if dfs(nx, ny, depth + 1, path, visited, limit):
                    return True
                path.pop()
                visited.remove((nx, ny))
        return False
    
    for depth in range(1, max_depth + 1):
        visited = set([start])
        path = [start]
        if dfs(start[0], start[1], 0, path, visited, depth):
            return True, path
    return False, []

def solve_maze(grid, start, target):
    found, path = iddfs(grid, start, target)
    if found:
        print(f"Path found at depth {len(path)-1} ")
        print("Traversal Order:", path)
    else:
        print(f"Path not found at max depth {len(grid) * len(grid[0])} ")

grid1 = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 1]
]
start1 = (0, 0)
target1 = (2, 3)

grid2 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
start2 = (0, 0)
target2 = (2, 2)

solve_maze(grid1, start1, target1)
solve_maze(grid2, start2, target2)
