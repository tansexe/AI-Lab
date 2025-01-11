from collections import deque

# defining bfs
def bfs_shortest_path(maze, start, goal):
    queue = deque([(start, 0)])
    seen = set([start])
    parent = {}
    
    while queue:
        (x, y), distance = queue.popleft()
        if (x, y) == goal:
            path = []
            while (x, y) in parent:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return distance, path[::-1]
        
        # path finding
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and 
                maze[ny][nx] != 0 and (nx, ny) not in seen):
                queue.append(((nx, ny), distance + 1))
                seen.add((nx, ny))
                parent[(nx, ny)] = (x, y)
    
    return -1, []

width, height = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(height)]

start = (0, 0)
goal = (width - 1, height - 1)

if maze[start[1]][start[0]] == 0 or maze[goal[1]][goal[0]] == 0:
    print(-1)
else:
    shortest_path_length, path = bfs_shortest_path(maze, start, goal)
    if shortest_path_length == -1:
        print("No path exists.")
    else:
        print(shortest_path_length)
        print(path)
