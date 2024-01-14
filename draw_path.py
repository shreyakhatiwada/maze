from OpenGL.GL import *

def draw_path(path, cell_size):
    glColor3f(0, 1, 1)
    glBegin(GL_QUADS)
    for node in path:
        glVertex2f(node[0] * cell_size, node[1] * cell_size)
        glVertex2f((node[0] + 1) * cell_size, node[1] * cell_size)
        glVertex2f((node[0] + 1) * cell_size, (node[1] + 1) * cell_size)
        glVertex2f(node[0] * cell_size, (node[1] + 1) * cell_size)
    glEnd()

