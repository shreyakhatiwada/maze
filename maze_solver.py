import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 
import random
import time
import heapq
from maze_generator_dfs import MazeGeneratorDFS
from a_star_pathfinder import AStarPathfinder
from draw_path import draw_path
from draw_text_opengl import draw_text_opengl


def main():
    # Set maze size
    maze_width, maze_height = 40, 25
    cell_size = 20

    # Initialize Pygame and OpenGL
    pygame.init()

    pygame.font.init() 
    pygame.display.set_caption("2D Maze solver")
    Font = pygame.font.Font(None, 30)

    display = (maze_width * cell_size, maze_height * cell_size)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(0, display[0], display[1], 0, -1, 1)

    maze_gen_dfs = MazeGeneratorDFS(maze_width, maze_height)







    # Perform DFS to generate maze
    while maze_gen_dfs.stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        maze_gen_dfs.draw_maze(cell_size, display)
        pygame.display.flip()
        pygame.time.wait(10)
        maze_gen_dfs.generate_maze_step()

    # Display "Press Enter to reveal the path..." message
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black =(0,0,0)
    custom_color = (123,62,62)
    # create a rectangular object for the
    # text surface object
    # textRect = text.get_rect()   
    # textRect.center = (maze_width // 2, maze_height // 2)
    draw_text_opengl("Press Enter to reveal the path...", Font, green,black,display )
    pygame.display.flip()

    # Wait for the Enter key to reveal the path
    waiting_for_enter = True
    while waiting_for_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting_for_enter = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        maze_gen_dfs.draw_maze(cell_size, display)

        # Draw messages
        draw_text_opengl("Press Enter to reveal the path...", Font, green,black,display)

        pygame.display.flip()
        pygame.time.wait(10)

    # Perform A* pathfinding
    pathfinder = AStarPathfinder(maze_gen_dfs)
    path = pathfinder.a_star()
    # Draw maze and path
    while True:
        
        for event in pygame.event.get():
        
            pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif waiting_for_enter == False and  event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Generate a new maze

                maze_gen_dfs = MazeGeneratorDFS(maze_width, maze_height)
                while maze_gen_dfs.stack:
                    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                    maze_gen_dfs.draw_maze(cell_size, display)
                    pygame.display.flip()
                    pygame.time.wait(10)
                    maze_gen_dfs.generate_maze_step()

                # Display messages again
                print("Here")
                draw_text_opengl("Press Enter to reveal the path...", Font, green,black,display)
                pygame.display.flip()

                # Wait for the Enter key to reveal the path
                waiting_for_enter = True
                while waiting_for_enter:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            waiting_for_enter = False
                # Perform A* pathfinding
                pathfinder = AStarPathfinder(maze_gen_dfs)
                path = pathfinder.a_star()


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        maze_gen_dfs.draw_maze(cell_size, display)

        # Draw path
        if path:
            draw_path(path, cell_size)
        else:
            path_revealed= True
        pygame.display.flip()
        pygame.time.wait(10)

        if not path:
            continue

        new_path = []
        for node in path[:-1]:
            if maze_gen_dfs.maze[node[1]][node[0]] == '.':
                new_path.append(node)
        path = new_path





if __name__ == "__main__":
    main()
