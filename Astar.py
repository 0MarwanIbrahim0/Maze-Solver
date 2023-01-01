import heapq


def way(a, b):
    # Return the Manhattan distance between two points
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_maze_Astar(maze, start, finish):
    # Set up the open set (priority queue) and closed set
    Frontier = []
    heapq.heappush(Frontier, (0, start))
    Explored = set()
    # Set up the direction vectors
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Set up the came_from dictionary to store the path
    came_from = {}
    # Set up the cost dictionary to store the cost of each node
    cost = {start: 0}
    # Loop until the open set is empty
    while Frontier:
        # Get the node with the lowest cost
        current = heapq.heappop(Frontier)[1]
        # Check if we have reached the finish
        if current == finish:
            curr = finish
            path = [curr]
            while curr != start:
                curr = came_from[curr]
                path.append(curr)
            # Reverse the path list to get the path from the start to the finish
            path = path[::-1]
            return path

        # Add the current node to the closed set
        Explored.add(current)
        # Loop through the directions
        for dx, dy in dirs:
            # Calculate the new position
            x, y = current
            nx, ny = x + dx, y + dy
            # Check if the new position is valid and not in the closed set
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#' and (nx, ny) not in Explored:
                # Calculate the new cost
                new_cost = cost[current] + 1
                # Check if the new position is not in the open set or if the new cost is lower than the current cost
                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    # Update the cost and add the new position to the open set
                    cost[(nx, ny)] = new_cost
                    priority = new_cost + way(finish, (nx, ny))
                    heapq.heappush(Frontier, (priority, (nx, ny)))
                    # Update the came_from dictionary
                    came_from[(nx, ny)] = current
    # If we reach here, there is no solution
    return "NO Solution Found"


def Display(maze, path, lines):
    # Mark the path on the maze
    for i, line in enumerate(lines):
        for j, ch in enumerate(line.strip()):
            if (i, j) in path and (i, j) != path[0] and (i, j) != path[-1]:
                maze[i][j] = "+"

    # Convert the maze to a string for display
    maze_str = "\n".join(" ".join(str(x) for x in row) for row in maze)

    return maze_str
