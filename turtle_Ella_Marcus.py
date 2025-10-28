
# Turtle Village — Lite (Student Scaffold)
# Focus: loops, decisions, try/except, and small functions.
# Run this file locally (IDLE/Thonny/PyCharm).

# ===>>>  REMOVE PASS IN ALL METHODS TO CODE

# NOTE about Turtle coordinate axis.
# turtle centers the origin (x == 0, y == 0 ) in the center of the canvas
# so if our default screen size is : CANVAS_W, CANVAS_H = 800, 600
#  the corners of your screen are :
# Top-left: (-CANVAS_W/2, CANVAS_H/2) → (-400, 300)
# Top-right: ( CANVAS_W/2, CANVAS_H/2) → ( 400, 300)
# Bottom-left: (-CANVAS_W/2, -CANVAS_H/2) → (-400, -300)
# Bottom-right: ( CANVAS_W/2, -CANVAS_H/2) → ( 400, -300)

# -------------------------------------------------------------------------------------------
# File: turtle_Ella_Marcus.py
# By: Ella Marcus
# Date: 10/26/2025
# Description: Draw multiple houses with trees and optional sun in a grid based on user input
# -------------------------------------------------------------------------------------------
# Pseudocode for turtle village:
# Define function move_to(x, y)
#     -prepare to move function without drawing
#     call T.penup
#     picks up pen so it doesn't draw
#     call T.goto
#     move pen to new x,y coordinate
#     call T.pendown
#     puts down pen to prepare it for drawing
# Define function draw_line(x1, y1, x2, y2)
#     call move_to
#     moves pen to right location without drawing
#     call T.goto
#     draws line from x,y to new x,y
# Define function fill_rect_center(cx, cy, w, h, color)
#     set black fillcolor
#     set black pencolor
#     call move_to
#     moves pen to the left:
#         half the width of the rec from the center and down half the height (w/2, cy + h/2) without drawing
#     call T.begin_fill
#     begins fill of the rectangle
#     (uses loop) for i in range of 1 to 2
#         move forward by width w,
#         turn 90 degrees,
#         move forward by height h,
#         turn 90 degrees
#     call T.end_fill
# Define fill_triangle(p1, p2, p3, color)
#     call T.fillcolor
#     set pencolor to black
#     call move_to p1 to move pen without drawing
#     call T.begin_fill
#     call T.goto p2, goes to 2nd point
#     call T.goto p3, goes to 3rd point
#     call T.goto p1, goes back to first point
#     call T.end_fill
# Define function fill circle center(cx, cy, r, color)
#     call T.fillcolor
#     set pencolor to black
#     call move_to the bottom of the circle (cx, cy - r)
#     call T.begin_fill
#     call T.circle, to draw a full circle
#     call T.end_fill
# Define ask_choice_int(prompt, allowed)
#     set allowed set to a set containing all values in allowed
#     while loop forever
#         try
#             prompt user with prompt and list of allowed set
#             convert input to integers, store in houses
#         if error occurs in the conversion print "Please enter a valid number."
#             continue loop
#         if input not in allowed_set
#             print "Please enter a number in allowed_set"
#             continue loop
#         else
#             return houses- returns input for use in later functions
# Define function ask_choice_str(prompt, allowed)
#     convert allowed to lowercase
#     while loop forever
#         prompt user with prompt and allowed
#         if user_entry from user not in allowed_lower
#             print "Please enter a valid entry in allowed:"
#             continue loop
#         else
#             return user_entry, for use in later functions
# Define draw_roads(cols, rows, cell_w, cell_h)
#     set top_y = CANVAS_H / 2 - TOP_MARGIN
#     set bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
#     set left_x = -CANVAS_W / 2
#     set right_x = CANVAS_W / 2
#     call T.pencolor, set pencolor to black
#     call T.width(5), set width to 5
#     use for loop to draw rows
#     for r in range(1,rows)
#     set y to be equal to top_y - r * cell_h
#     call draw_line(left_x, y, right_x, y) to draw lines
#     use for loop to draw columns
#     for c in range(1,cols)
#     set x to be equal to left_x + c * cell_w
#     call draw_line(x, top_y, x, bot_y) to draw lines
# Define draw_house_centered(cx, cy, size_key, theme_key, roof_style)
#     w, h = SIZES[size_key]
#     colors = THEMES[theme_key]
#     set body_c = colors["body"]
#     set roof_c = colors["roof"]
#     set door_c = colors["door"]
#     set win_c = colors["window"]
#     call fill_rect_center(cx, cy, w, h, body_c) to draw body of house
#     if input for roof_style is triangle
#         set yT = cy + h / 2
#         call fill_triangle(
#             (cx - 0.5 * w, cy + 0.5 * h),
#             (cx, yT + 0.5 * h),
#             (cx + 0.5 * w, cy + 0.5 * h),
#             roof_c
#         ) - to draw roof
#     else, if triangle not selected
#         fill_rect_center(cx, cy + 0.5 * h, w * 1.02, 0.25 * h, roof_c) to draw flat roof
#     call fill_rect_center(cx, cy - 0.23 * h, 0.2 * w, 0.5 * h, door_c) to draw door
#     call fill_rect_center(cx - 0.2 * w, cy, 0.1 * w, 0.15 * h, win_c) to draw window
# Define draw_tree_near(cx, cy, size_key)
#     set w, h = SIZES[size_key]
#     set tw, th = w * 0.10, h * 0.40 as ratios
#     set side = random.choice([-1, 1])
#     set tx = cx + side * (w*0.45)
#     set ty = cy - h*0.5 + th/2
#     set r = 0.15 * w
#     call fill_rect_center(tx, ty, tw, th, "#422008") to draw trunk
#     call fill_circle_center(tx, cy, r, "#32a84a") to draw canopy
# Define draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)
#     set cell_w = CANVAS_W / cols
#     set cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows
#     call draw_roads(cols, rows, cell_w, cell_h) to draw lines
#     for r in range(rows)- use for loop
#         for c in range(cols)- use nested loop to draw multiple houses
#             compute cx = -CANVAS_W / 2 + (c + 0.5) * cell_w
#             compute cy = CANVAS_H / 2 - TOP_MARGIN - (r + 0.5) * cell_h
#             call draw_house_centered(cx, cy, size_key, theme_key, roof_style) to draw house
#             call draw_tree_near(cx, cy, size_key) to draw tree
#     if input for sun_flag is yes
#         set r = 35
#         set cx = CANVAS_W/2 - r - 20
#         set cy = CANVAS_H/2 - r - 20
#         call fill_circle_center(cx, cy, r, "yellow") to draw sun in corner
# Define main
#     print "Welcome to Turtle Village - Lite!"
#     prompt user "How many houses per row? allowed- 2,3"
#     set value to cols
#     prompt user "How many rows? allowed- 2"
#     set value to rows
#     prompt user "House size allowed- s,m,l"
#     set value to size_key
#     prompt user "Color theme allowed- pastel,primary"
#     set value to theme_key
#     Prompt user "Roof type allowed- triangle,flat"
#     set value to roof_style
#     Prompt user "Draw a sun? allowed- y,n"
#     set value to sun_flag
#     lowercase input of all prompts
#     set window T.setup(CANVAS_W, CANVAS_H); T.speed(0); T.tracer(False)
#     set cell_w = CANVAS_W / cols
#     set cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows
#     call draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style) to draw to village
#     set T.tracer(True); T.hideturtle(); T.done() to finish
# Define if __name__ == "__main__"
#     call main()


import turtle as T
import random

# ---------- constants ----------
CANVAS_W, CANVAS_H = 800, 600
TOP_MARGIN, BOTTOM_MARGIN = 40, 40


# size of houses 
SIZES = {
    "s": (120, 80),
    "m": (150, 100),
    "l": (180, 120),
}

'''
How to use Themes : 
# Use a theme like this:
colors = THEMES[theme_key]          # where theme_key is either "pastel" or "primary"
body_c  = colors["body"]            # we then can access the colors for the body of the house
roof_c  = colors["roof"]            # color of the roof of the house 
door_c  = colors["door"]            # door 
win_c   = colors["window"]          # window -- feel free to add or change the colors 
                                    # there is are beautiful pallette choices at coolors.co

# how to apply :
fill_rect_center(cx, cy, w, h, body_c)  # house body
'''
THEMES = {
    "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7", window="#fff7ae"),
    "primary": dict(body="red", roof="blue", door="gold", window="#aee3ff"),
}


def move_to(x, y):
    """
    x - position on x coordinate axis
    y - position on y coordinate axis
    """
    T.penup(); T.goto(x, y); T.pendown()


def draw_line(x1, y1, x2, y2):
    """
       we draw a line from x1,y1
       x1 - position on x coordinate axis
       y1 - position on y coordinate axis
       
       to x2, y2
       x2 - position on x coordinate axis
       y2 - position on y coordinate axis
    """
    move_to(x1, y1); T.goto(x2, y2)


def fill_rect_center(cx, cy, w, h, color):
    """
    cx - center of rectangle x coordinate 
    cy - center of rectangle y coordinate 
    w - width of rectangle 
    h - height of rectangle 
    color - color of rectangle 
    """
    T.fillcolor(color); T.pencolor("black")
    move_to(cx - w/2, cy + h/2)
    T.begin_fill()
    for _ in range(2):
        T.forward(w); T.right(90); T.forward(h); T.right(90)
    T.end_fill()


def fill_triangle(p1, p2, p3, color):
    """
    Draw a filled triangle defined by three points.
    
    p1 — point 1 (x1, y1)
    p2 — point 2 (x2, y2)
    p3 — point 3 (x3, y3)
    color — fill color for the triangle
    
    Notes:
    - Each point is an (x, y) tuple.
    - Depending on your triangle, some x’s or y’s may be equal (e.g., flat base).
    
    Example:
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    fill_triangle(p1, p2, p3, color)
    """

    T.fillcolor(color); T.pencolor("black")
    move_to(*p1); T.begin_fill()
    T.goto(*p2); T.goto(*p3); T.goto(*p1)
    T.end_fill()


def fill_circle_center(cx, cy, r, color):
    """
    a circle is defined by 
    cx - the center of your circle, x coordinate 
    cy - center of your circle, y coordinate 
    r - radius 
    color - color of circle 
    """
    T.fillcolor(color); T.pencolor("black")
    move_to(cx, cy - r)  # turtle draws circles from the bottom
    T.begin_fill(); T.circle(r); T.end_fill()


def ask_choice_int(prompt, allowed):
    """
    Prompt the user for an integer in an allowed set and reprompt an error.

    In a while loop (continues until True), ask for a valid number from the allowed list.
    Print an error if an incorrect number is given - one that can't be converted to an integer.
    Reprompt the user until a correct number is entered.
    Prompt for:
        1. houses per row
        2. how many houses
    Parameters:
        prompt (str): message that is displayed to prompt the user
        allowed (list of int): list of integers that is allowed as input from the user
    Returns:
        int: the integer that user enters as input
    """

    # A set is a list which only allows one unique item to exist, not any duplicates
    # If duplicates are given, set removes all duplicates
    allowed_set = set(allowed)
    # Set loop to go on forever until user enters valid integers
    while True:
        try:
            houses = int(input(f"{prompt} {allowed}: "))
        except ValueError:  # Catch error if integer is not entered
            print("Please enter a valid number.")
            continue  # Reprompt user
        if houses not in allowed_set:  # If input entered not one of allowed
            print(f"Please enter a number in {allowed}: ")
            continue  # Reprompt user
        return houses  # Return value for late usage


def ask_choice_str(prompt, allowed):
    """
    Prompt the user for a string in an allowed set and reprompt an error.

    In a while loop (continues until True), ask for a valid string from allowed list.
    If invalid input is entered reprompt until correct.
    Prompt for:
        1. house size 
        2. color theme
        3. roof type 
        4. sun
    Parameters:
        prompt (str): message that is displayed to prompt the user
        allowed (list of str): list of strings that is allowed as input from the user
    Returns:
        str: the string that user enters as input
    """
    allowed_lower = [a.lower() for a in allowed] # Convert to lower case all in allowed list
     # Set loop to go on forever until user enters valid string
    while True:
        user_entry = input(f"{prompt} {allowed}: ")
        if user_entry.lower() not in allowed_lower:  # If input entered not one of allowed
            print(f"Please enter a valid entry in {allowed}: ")
            continue  # Reprompt user until valid string is entered
        return user_entry  # Return str for later usage


def draw_roads(cols, rows, cell_w, cell_h):
    """
    Draw straight separator lines between rows and columns (simple roads).

    Set margins to draw roads as rows (horizontal) and columns (vertical).
    Use a for loop to draw as many lines as user inputs.
    Parameters:
        cols (int): number of columns in grid.
        rows (int): number of rows in grid.
        cell_w (float): width of each box in grid (cell).
        cell_h (float): height of each box in grid (cell).
    Returns:
        None
    """
    # Set margins of grid
    top_y = CANVAS_H / 2 - TOP_MARGIN
    bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
    left_x = -CANVAS_W / 2
    right_x = CANVAS_W / 2

    # Set pen color and pensize
    T.pencolor("black"); T.width(5)
    # Draw horizontal separators
    for r in range(1,rows):
        y = top_y - r * cell_h  # Compute y coordinate of where to draw line
        draw_line(left_x, y, right_x, y)
    # Draw vertical separators
    for c in range(1,cols):
        x = left_x + c * cell_w  # Compute x coordinate of where to draw line
        draw_line(x, top_y, x, bot_y)


def draw_house_centered(cx, cy, size_key, theme_key, roof_style):
    """
    Draw a simple house centered at (cx, cy).

    The house drawn is composed of a rectangle, roof, door, and window.
    The roof can either be a triangle or rectangle.
    Uses theme key to establish color of the house and size key to establish size.
    Parameters:
        cx (float): x coordinate of house.
        cy (float): y coordinate of house.
        size_key (str): size of house in s, m, l.
        theme_key (str): colors of house in pastel, primary.
        roof_style (str): roof of house in y, n.
    """
    w, h = SIZES[size_key]  # Size of house
    colors = THEMES[theme_key]  # Theme_key is either "pastel" or "primary"
    body_c = colors["body"]  # Color for the body of the house
    roof_c = colors["roof"]  # Color of the roof of the house
    door_c = colors["door"]  # Color of door
    win_c = colors["window"]  # Color of window
    # Call function to draw and fill house body
    fill_rect_center(cx, cy, w, h, body_c)
    # Call function to draw and fill roof of house
    # Check if roof input is triangle or flat
    if roof_style == "triangle":  # If triangle is selected, draw triangle
        yT = cy + h / 2
        fill_triangle((cx - 0.5 * w, cy + 0.5 * h), (cx, yT + 0.5 * h), (cx + 0.5 * w, cy + 0.5 * h), roof_c)
    # If flat roof os selected, draw rectangle
    else:
        fill_rect_center(cx, cy + 0.5 * h, w * 1.02, 0.25 * h, roof_c)
    # Call function to draw door in middle of house body
    fill_rect_center(cx, cy - 0.23 * h, 0.2 * w, 0.5 * h, door_c)
    # Call function to draw window next to door
    fill_rect_center(cx - 0.2 * w, cy, 0.1 * w, 0.15 * h, win_c)


def draw_tree_near(cx, cy, size_key):
    """
    Draw a small tree near the house (left or right).

    Tree is composed of a rectangle and circle drawn from calling other functions.
    It is placed randomly next to the house.
    Parameters:
        cx (float): x coordinate of house.
        cy (float): y coordinate of house.
        size_key (str): size of house in s, m, l.
    """
    w, h = SIZES[size_key]  # Width and height based on size key
    # Trunk size (in ratios)
    tw, th = w * 0.10, h * 0.40
    # Place tree to left or right of the house randomly
    side = random.choice([-1, 1])
    tx = cx + side * (w * 0.45)  # X coordinate where it will go
    ty = cy - h * 0.5 + th / 2  # Y coordinate of where it will go
    r = 0.15 * w  # Radius of canopy of tree
    # Draw and fill trunk
    fill_rect_center(tx, ty, tw, th, "#422008")
    # Draw and fill canopy above trunk
    fill_circle_center(tx, cy, r, "#32a84a")


def draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style):
    """
    Compute cell sizes, draw roads, and loop over grid to place houses/trees/sun.

    Call functions to draw complete village.
    Use loop to draw houses multiple times.
    Draw sun based on input from user.
    Parameters:
        cols (int): number of columns in grid.
        rows (int): number of rows in grid.
        size_key (str): size of house in s, m, l.
        theme_key (str): colors of house in pastel, primary.
        sun_flag (str): sun in y,n from user.
        roof_style (str): roof of house in y, n from user.
    """
    # Set margins of grid
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # Draw roads first
    draw_roads(cols, rows, cell_w, cell_h)
    # Nested loops to draw houses in village multiple times
    for r in range(rows):
        for c in range(cols):
            #  Compute cx, cy as center of house per formula
            cx = -CANVAS_W / 2 + (c + 0.5) * cell_w
            cy = CANVAS_H / 2 - TOP_MARGIN - (r + 0.5) * cell_h

            #  Draw house
            draw_house_centered(cx, cy, size_key, theme_key, roof_style)
            #  Draw tree
            draw_tree_near(cx, cy, size_key)
    # Check if user wants sun
    if sun_flag == 'y':
        r = 35  # Set radius of sun
        cx = CANVAS_W/2 - r - 20  # Set x coordinate of where to draw sun
        cy = CANVAS_H/2 - r - 20  # Set y coordinate of where to draw sun
        fill_circle_center(cx, cy, r, "yellow")  # Draw sun


def main():
    """
    Prompt user and draw complete village.

    Prompt user to get input about what to draw.
    Call all functions to draw complete village - house, roof, door, window, tree, and sun.
    """
    # User introduction to program
    print("Welcome to Turtle Village — Lite!")
    # Prompt user and define what is in allowed list
    cols = ask_choice_int("How many houses per row?", [2, 3])
    rows = ask_choice_int("How many rows?", [2])  # you may change to [2, 3]
    size_key = ask_choice_str("House size", ["S","M","L"]).lower()
    theme_key = ask_choice_str("Color theme", ["pastel","primary"]).lower()
    roof_style = ask_choice_str("Roof type", ["triangle","flat"]).lower()
    sun_flag = ask_choice_str("Draw a sun?", ["y","n"]).lower()

    # Set window
    T.setup(CANVAS_W, CANVAS_H); T.speed(0); T.tracer(False)

    # Set the size of the property
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # Call draw_village with inputs
    draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)
    # Finalize village and turtle
    T.tracer(True); T.hideturtle(); T.done()

if __name__ == "__main__":
    main()
