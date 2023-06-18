from colors import palette_color as color
import constants
import text

messages = ['Welcome!']
text_size = 50

# Global variable to manage animating new messages
offset = text_size

def proper(message):
    return message[0].upper() + message[1:]

def new(message):
    'Adds a new message to the queue'
    global offset
    messages.insert(0, message)
    offset = text_size

    if len(messages) > 5:
        messages.pop()

def draw(surface):
    'Draws all messages to the surface'
    global offset
    height = surface.get_height()
    for i, message in enumerate(messages):
        # Hilight the 2 most recent messages, all others should be dim
        text_color = i <= 1 and color(constants.C_FG) or color(constants.C_GRAY)
        text.write(
            surface,
            0,
            height - text_size * (i + 1) + offset,
            message,
            scale=text_size,
            color=text_color)

    offset *= .9
