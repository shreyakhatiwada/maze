from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_text_opengl(message, font, color, bg_color,display):
    # Calculate text size
    text_surface = font.render(message, True, color)
    text_width, text_height = text_surface.get_size()
    padding = 10
    # Calculate background size with padding
    bg_width = text_width + 2 * padding
    bg_height = text_height + 2 * padding

    # Calculate centered position
    centered_position = ((display[0] - bg_width) / 2, (display[1] - bg_height) / 2)

    # Draw background
    glColor3f(bg_color[0], bg_color[1], bg_color[2])
    glBegin(GL_QUADS)
    glVertex2f(centered_position[0], centered_position[1])
    glVertex2f(centered_position[0] + bg_width, centered_position[1])
    glVertex2f(centered_position[0] + bg_width, centered_position[1] + bg_height)
    glVertex2f(centered_position[0], centered_position[1] + bg_height)
    glEnd()

    # Draw text
    glColor3f(color[0], color[1], color[2])
    glRasterPos2f(centered_position[0] + padding *2.5, centered_position[1] +padding* 2.5)

    for character in message:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character))

