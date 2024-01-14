# a_star_pathfinder.py

import heapq

class AStarPathfinder:
    def __init__(self, maze_gen_dfs):
        self.maze_gen_dfs = maze_gen_dfs
        self.start = maze_gen_dfs.start_point
        self.end = maze_gen_dfs.end_point
        self.cost_so_far = {}
        self.came_from = {}

    def heuristic(self, node):
        return abs(node[0] - self.end[0]) + abs(node[1] - self.end[1])

    def get_neighbors(self, node):
        neighbors = [
            (node[0] + 1, node[1]),
            (node[0] - 1, node[1]),
            (node[0], node[1] + 1),
            (node[0], node[1] - 1),
        ]
        return [(x, y) for x, y in neighbors if 0 <= x < self.maze_gen_dfs.width and 0 <= y < self.maze_gen_dfs.height]

    def a_star(self):
        heap = [(0, self.start)]
        visited = set()

        while heap:
            cost, current = heapq.heappop(heap)

            if current == self.end:
                path = [current]
                while current in self.came_from:
                    current = self.came_from[current]
                    path.append(current)
                return path[::1]

            visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited and self.maze_gen_dfs.maze[neighbor[1]][neighbor[0]] != '#':
                    new_cost = cost + 1
                    if neighbor not in self.cost_so_far or new_cost < self.cost_so_far[neighbor]:
                        self.cost_so_far[neighbor] = new_cost
                        priority = new_cost + self.heuristic(neighbor)
                        heapq.heappush(heap, (priority, neighbor))
                        self.came_from[neighbor] = current

        return None
