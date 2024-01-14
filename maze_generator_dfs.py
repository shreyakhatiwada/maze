# maze_generator_dfs.py

import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 
class MazeGeneratorDFS:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [['#' for _ in range(width)] for _ in range(height)]
        self.stack = [(0, 0)]
        self.visited_cells = set()
        self.visited_cells.add((0, 0))
        self.start_point = (0, 0)
        self.end_point = (width - 1, height - 1)
        self.maze[self.start_point[1]][self.start_point[0]] = 'S'
        self.maze[self.end_point[1]][self.end_point[0]] = 'E'

    def generate_maze_step(self):
        if not self.stack:
            return

        current_row, current_col = self.stack[-1]
        self.maze[current_row][current_col] = '.'

        neighbors = [
            (r, c) for r, c in [
                (current_row - 2, current_col),
                (current_row + 2, current_col),
                (current_row, current_col - 2),
                (current_row, current_col + 2),
            ]
            if 0 <= r < self.height and 0 <= c < self.width and (r, c) not in self.visited_cells
        ]

        if neighbors:
            next_row, next_col = random.choice(neighbors)
            self.visited_cells.add((next_row, next_col))
            self.maze[(current_row + next_row) // 2][(current_col + next_col) // 2] = '.'
            self.stack.append((next_row, next_col))
        else:
            self.stack.pop()

    def draw_maze(self, cell_size, window_size):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for row in range(self.height):
            for col in range(self.width):
                if self.maze[row][col] == '#':
                    glColor3f(0, 0, 0)
                elif self.maze[row][col] == 'S':
                    glColor3f(0, 1, 0)
                elif self.maze[row][col] == 'E':
                    glColor3f(1, 0, 0)
                else:
                    glColor3f(1, 1, 1)

                glBegin(GL_QUADS)
                glVertex2f(col * cell_size, row * cell_size)
                glVertex2f((col + 1) * cell_size, row * cell_size)
                glVertex2f((col + 1) * cell_size, (row + 1) * cell_size)
                glVertex2f(col * cell_size, (row + 1) * cell_size)
                glEnd()
