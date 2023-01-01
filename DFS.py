def solve_maze_DFS(maze, start, finish):
    # Set up the stack and visited set
    stack = [start]
    visited = set()
    path = []
    # Set up the direction vectors
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    parent = {start: None}
    # Loop until the stack is empty
    while stack:
        # Get the current position
        x, y = stack.pop()
        # Check if we have reached the finish
        if (x, y) == finish:
            # Trace the path from the finish to the start using the parent dictionary
            curr = finish
            while curr != start:
                path.append(curr)
                curr = parent[curr]
            # Reverse the path and return it
            path.reverse()
            return path
        # Loop through the directions
        for dx, dy in dirs:
            # Calculate the new position
            nx, ny = x + dx, y + dy
            # Check if the new position is valid and not visited
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#' and (nx, ny) not in visited:
                # Add the new position to the stack and visited set
                stack.append((nx, ny))
                visited.add((nx, ny))
                # change the curr point in dic
                parent[(nx, ny)] = (x, y)
    # If we reach here, there is no solution
    return "NO Solution Found"


def Display(maze, path, lines):
    # Mark the path on the maze
    for i, line in enumerate(lines):
        for j, ch in enumerate(line.strip()):
            if (i, j) in path and (i, j) != path[-1]:
                maze[i][j] = "+"

    # Convert the maze to a string for display
    maze_str = "\n".join(" ".join(str(x) for x in row) for row in maze)

    return maze_str
