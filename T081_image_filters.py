"""
ECOR 1042 T081
Emily Tang
Taytum George
Alexander Bundgaard
Matthew Gray
Last edited: Mar. 31, 2021

Milestone 1 and 2 Image Filters
"""

import numpy as np
from point_manipulation import get_x_y_lists, sort_points
from simple_Cimpl_filters import grayscale
from Cimpl import *

def red_channel(image: Image) -> Image:
    """
    T081 Matthew Gray
    
    Returns a new Image that only contains the red portion of the provided 
    Image.
    
    >>> file = load_image(choose_file()) 
    >>> red_image = red_channel(file)
    >>> show(red_image)
    """
    new_image = copy(image)  
    for x, y, (r, g, b) in image:
        red = create_color(r, 0, 0)
        set_color(new_image, x, y, red)       
    return new_image

def green_channel(image: Image) -> Image: 
    """
    T081 Taytum George
    
    Takes the given Image, and returns a version of that Image which has had  
    a green filter applied over its entirety.
    
    >>> file = load_image(choose_file())
    >>> green_filtered_image = green_channel(file)
    >>> show(green_filtered_image)
    """
    green_filtered_image = copy(image) 
    for x, y, (r, g, b) in image:
        color = create_color(0, g, 0)
        set_color (green_filtered_image, x, y, color)
    return green_filtered_image

def blue_channel(image: Image) -> Image:
    """
    T081 Alexander Bundgaard
    Edited by: Emily Tang
    
    Returns a blue filtered image.

    >>> file = load_image(choose_file())
    >>> image = blue_channel(file)
    >>> show(image)
    """
    red_image = copy(image)
    for x, y, (r, g, b) in image:
        blue = create_color(0, 0, b)
        set_color(red_image, x, y, blue)
    return red_image

def combine(r_img: Image, g_img: Image, b_img: Image) -> Image:
    """
    T081 Emily Tang
    
    Returns an Image that combines the red, green, and blue Images provided.
    Assumes that all Images provided have the same width and height.
    
    >>> r_img = load_image('red_image.png')
    >>> g_img = load_image('green_image.png')
    >>> b_img = load_image('blue_image.png')
    >>> combine(r_img, g_img, b_img)
    """
    # Create a new Image using the width and height of the provided Images
    rgb_img = copy(r_img)
    
    # Go through each row and column of the new Image
    for x, y, (r, g, b) in rgb_img:
        # Get the RGB components of the pixel from each Image provided
        r_pixel = get_color(r_img, x, y)
        g_pixel = get_color(g_img, x, y)
        b_pixel = get_color(b_img, x, y)
        # Create a new Color using RGB components from the Images provided
        rgb_pixel = create_color(r_pixel[0], g_pixel[1], b_pixel[2])
        # Sets the Color of the pixel in the new Image
        set_color(rgb_img, x, y, rgb_pixel)   
        
    # Return the Image that combines the red, green, and blue Images
    return rgb_img

def _determine_color(colour: str) -> Color:
    """
    T081 Emily Tang
    
    Returns a Color based on the inputted string.
    
    >>> _determine_color("blue")
    Color(0, 0, 255)
    >>> _determine_color("white")
    Color(255, 255, 255)
    >>> _determine_color("aqua")
    Color(0, 255, 255)
    """
    # Colour constants
    BLACK = create_color(0, 0, 0)
    WHITE = create_color(255, 255, 255)
    BLOOD = create_color(255, 0, 0)
    GREEN = create_color(0, 255, 0)
    BLUE = create_color(0, 0, 255)
    LEMON = create_color(255, 255, 0)
    AQUA = create_color(0, 255, 255)
    PINK = create_color(255, 0, 255)
    GRAY = create_color(128, 128, 128)
    
    if colour == "black":
        return BLACK
    elif colour == "white":
        return WHITE
    elif colour == "blood":
        return BLOOD
    elif colour == "green":
        return GREEN
    elif colour == "blue":
        return BLUE
    elif colour == "lemon":
        return LEMON
    elif colour == "aqua":
        return AQUA
    elif colour == "pink":
        return PINK
    elif colour == "gray":
        return GRAY

def three_tone(image: Image, col_1: str, col_2: str, col_3: str) -> Image: 
    """
    T081 Taytum George
    Edited by: Emily Tang
    
    Takes the given Image, and returns a version of that image which has had a 
    "Three-Tone Filter" applied over it's entirety (changing the colors of each
    pixel to red, green, or blue based off their current average color values).
    
    >>> file = load_image(choose_file())
    >>> three_tone_filtered_image = three_tone(file)
    >>> show(three_tone_filtered_image)
    """
    # Create a copy of the inputted Image
    three_tone_img = copy(image)
    # Go through each pixel in the inputted Image
    for x, y, (r, g, b) in image:
        # Determine the brightness of each pixel
        brightness = (r + g + b) // 3
        if 0 <= brightness <= 84:
            # Set pixel to the first inputted color
            set_color(three_tone_img, x, y, _determine_color(col_1))
        elif 85 <= brightness <= 170:
            # Set pixel to the second inputted color
            set_color(three_tone_img, x, y, _determine_color(col_2))
        elif 171 <= brightness <= 255:
            # Set pixel to the third inputted color
            set_color(three_tone_img, x, y, _determine_color(col_3))
    # Return the three tone Image to the user
    return three_tone_img

def extreme_contrast(image: Image) -> Image:
    """
    T081 Matthew Gray
    
    Returns a copy of the image that has extreme contast, the RGB values for 
    each pixel are either 255 or 0.
    
    >>> file = load_image(choose_file()) 
    >>> red_image = red_filter(file)
    >>> show(red_image)
    """
    new_image = copy(image)
    newr = 0
    newg = 0
    newb = 0    
    for x, y, (r, g, b) in image:
        if 127 >= r >= 0:
            new_r = 0
        elif 255 >= r >= 128:
            new_r = 255    
        if 127 >= g >= 0:
            new_g = 0 
        elif 255 >= g >= 128:
            new_g = 255  
        if 127 >= b >= 0:
            new_b = 0      
        elif 255 >= b >= 128:
            new_b = 255    
        extreme_colour = create_color(new_r, new_g, new_b)
        set_color(new_image, x, y, extreme_colour)           
    return new_image

def sepia(image: Image) -> Image:
    """
    T081 Alexander Bundgaard
    Edited by: Emily Tang
    
    Returns a sepia tinted Image.
    
    >>> image = load_image(choose_file())
    >>> image_sepia = sepia(image)
    """
    sepia_img = grayscale(image)
    for x, y, (r, g, b) in image:
        if r < 63:
            sepia = create_color(g * 1.1, g, g * 0.9)
        elif r <= 191:
            sepia = create_color(g * 1.15, g, g * 0.85)
        else:
            sepia = create_color(g * 1.08, g, g * 0.93)
        set_color(sepia_img, x, y, sepia)
    return sepia_img

def _adjust_component(value: int) -> int:
    """
    T081 Emily Tang
    
    Returns the value of the midpoint of the quadrant when given a value of a
    pixel's red, green, or blue component. Assumes that the given value is an 
    integer between 0 and 255, inclusive.
    
    >>> _adjust_component(0)
    31
    >>> _adjust_component(20)
    31
    >>> _adjust_component(63)
    31
    >>> _adjust_component(64)
    95
    >>> _adjust_component(100)
    95
    >>> _adjust_component(127)
    95
    >>> _adjust_component(128)
    159
    >>> _adjust_component(179)
    159
    >>> _adjust_component(191)
    159
    >>> _adjust_component(192)
    223
    >>> _adjust_component(200)
    223
    >>> _adjust_component(255)
    223
    """
    # Constants for the midpoints of the quadrants
    MP_Q1 = 31
    MP_Q2 = 95
    MP_Q3 = 159
    MP_Q4 = 223
    
    # Check which quadrant the inputted value lies in
    if value >= 0 and value <= 63:
        return MP_Q1
    elif value >= 64 and value <= 127:
        return MP_Q2
    elif value >= 128 and value <= 191:
        return MP_Q3
    elif value >=192 and value <= 255:
        return MP_Q4

def posterize(image: Image) -> Image:
    """
    T081 Emily Tang
    
    Returns an Image that has a smaller amount of colours than the original
    inputted Image.
    
    >>> image = posterize(load_image('p2-original.png'))
    >>> show(image)
    """
    # Create a copy of the Image
    posterized_img = copy(image)
    # Go through each row and column of the new Image
    for x, y, (r, g, b) in posterized_img:
        # Get the new RGB components of each pixel
        r_pixel = _adjust_component(r)
        g_pixel = _adjust_component(g)
        b_pixel = _adjust_component(b)
        # Sets the Color of the pixel in the new Image
        set_color(posterized_img, x, y, create_color(r_pixel, g_pixel, b_pixel))
    # Return the posterized Image
    return posterized_img

def detect_edges(original: Image, threshold: int) -> Image:
    """
    T081 Alexander Bundgaard
    Reviewed by: Emily Tang
    
    Takes an Image and a threshold, returns a edge detected filtered Image 
    containing only black and white pixels.
    
    >>> image = load_image(choose_file())
    >>> filtered_image = filter_edge_detection(image, 32)
    """
    WHITE = create_color(255, 255, 255)
    BLACK = create_color(0, 0, 0)    
    
    # Make a copy of the image for modification
    new = copy(original)

    # For every pixel that has a pixel below it (So exclude the bottom row)
    for y in range(0, get_height(original) - 1):

        for x in range(0, get_width(original)):
            # Get average colour value for top and bottom pixel
            brightness_upper = sum(get_color(original, x, y)) // 3
            brightness_lower = sum(get_color(original, x, y + 1)) // 3
            # Calculate contrast of the top and bottom pixel
            contrast = abs(brightness_lower - brightness_upper)

            # Conditional statements for colour selection
            if contrast > threshold:
                set_color(new, x, y, BLACK)
            else:
                set_color(new, x, y, WHITE)

    # Sets last row to WHITE
    for x in range(get_width(original)):
        set_color(new, x, get_height(original)-1, WHITE)

    #returns filtered image
    return new

def _interpolation(point_list: list) -> list:
    """
    T081 Emily Tang

    Returns a list of the coefficients of the interpolating polynomial if the
    inputted sorted list contains two or three items. Returns a list of the
    quadratic regression polynomial that is best fit to the points on the list
    provided if the sorted inputted list contains more than three items.

    >>> _interpolation([(0, 2), (5, 5)])
    [0.6, 2]
    >>> _interpolation([(2, 0), (40, 10), (50, 15)])
    [0.00493421, 0.05592105, -013157895]
    >>> _interpolation([(1, 1), (3, 5), (4, 2), (8, 6)])
    [-0.36317042, 1.3498078, -0.07230459]
    """
    # Get a 2D list of x and y values of point_list
    x_y_values = get_x_y_lists(point_list)
    
    # Perform interpolation if the user entered two or three poitns
    if (len(point_list) == 2) or (len(point_list) == 3):
        return np.polyfit(x_y_values[0], x_y_values[1], len(point_list) - 1)
    # Perform quadratic regression if the user entered more than three points
    elif len(point_list) > 3:
        return np.poly1d(np.polyfit(x_y_values[0], x_y_values[1], 2)).c
    
def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
    """
    T081 Emily Tang
    
    Solves f(x)-val=0 for x between 0 and max-x where polycoeff contains the
    coefficients of f, using EPSILON of 1 (as we only need ints for pixels).
    Returns None if there is no solution between the bounds.
    
    >>> _exhaustive_search(639, [6.33e-03, -3.80e+00, 5.57e+02], 0)
    253
    >>> _exhaustive_search(639, [7.24e-04, -1.19e+00, 4.51e+02], 0)
    590
    >>> _exhaustive_search(639, [7.24e-04, -1.19e+00, 4.51e+02], 479)
    None
    """
    EPSILON = 1
    step = EPSILON
    guess = 0
    
    while abs(np.polyval(polycoeff, guess) - val) >= EPSILON and guess <= max_x:
        guess += step
    
    if guess > max_x:
        return None
    else:
        return guess

def _image_border_finding(image_size: list, interpol: list) -> list :
    """
    T081 Emily Tang
    
    Returns the pixels where the curve intersects the border of the Image by
    using the width and height of the Image, and the coefficients of the
    binomial or polynomial of the curve.
    
    >>> _image_border_finding([680, 480], [0.99299065, 3.02803738])
    [[0, 3], [479, 480]]
    >>> _image_border_finding([680, 480], [-3.98695179e-03, 1.37151142e+00, 1.35643349e+01])
    [[0, 13], [353, 0]]
    >>> _image_border_finding([680, 480], [1.77233791e-02, -8.99939181e+00, 5.82542478e+02])
    [[76, 0], [496, 480]]
    """
    # Initialize a list to store the pixels where the curve intersects
    points = []
    
    # Determine f(0)
    if len(interpol) == 2:
        cross_left = interpol[1]
    else:
        cross_left = interpol[2]
    
    # Determine f(pixel_x - 1)
    if len(interpol) == 2:
        cross_right = (interpol[0] * (image_size[0] - 1)) + interpol[1]
    else:
        cross_right = (interpol[0] * (image_size[0] - 1) ** 2) + (interpol[1] * (image_size[0] - 1)) + interpol[2]
    
    # Determine f(x) = 0 using exhaustive enumeration search
    cross_bottom = _exhaustive_search(image_size[0], interpol, 0)
    
    # Determine f(x) = pixel_y - 1 using exhaustive enumeration search
    cross_top = _exhaustive_search(image_size[0], interpol, image_size[1] - 1)
        
    # Determine if the curve crosses the left order of the Image
    if cross_left >= 0 and cross_left <= image_size[1]:
        # Add point to list
        points.append([0, int(cross_left)])
        
    # Determine if the curve crosses the right border of the Image
    if cross_right >= 0 and cross_right <= image_size[1]:
        # Add point to list
        points.append([image_size[0], int(cross_right)])
        
    # Determine if the curve crosses the bottom border of the Image
    if cross_bottom != None:
        # Add point to list
        points.append([cross_bottom, 0])    
    
    # Determine if the curve crosses the top border of the Image
    if cross_top != None:
        # Add point to list
        points.append([cross_top, image_size[1]])    
    
    # Returns the pixels where the curve intersects the border of the Image
    return sort_points(points) 

def draw_curve(image: Image, colour: str, point_list: list = None) -> tuple:
    """
    T081 Emily Tang
    Reviewed by: Alexander Bundgaard
    
    Returns a tuple containing an Image with a curve drawn on it, and a list of
    points on the border of the Image using the inputted Image, and colour.
    
    >>> curve = draw_curve(load_image('p2-original.jpg'), "aqua", None)
    >>> show(curve[0])
    """
    # Notify the user of the size of the Image in pixels
    pixel_x = get_width(image)
    pixel_y = get_height(image)
    print("The size of the Image is " + str(pixel_x) + " x " + str(pixel_y) + 
          ".")

    # Ask the user how many pixel coordinates they want to provide
    pixel_coordinates = input("How many pixel coordinates would you like to provide? Please enter a value greater or equal to two: ")

    # Initialize a list for the pixel coordinates
    point_list = []
    # Ask the user to enter the coordinates of the pixels
    for i in range(int(pixel_coordinates)):
        x = input("Please enter the x value of pixel #" + str(i + 1) + ": ")
        y = input("Please enter the y value of pixel #" + str(i + 1) + ": ")
        # Add the pixel coordinates to the list
        point_list.append((int(x), int(y)))
    # Sort the list in ascending order
    point_list = sort_points(point_list)

    # Determine coefficients of the binomial or polynomial
    interpolation = _interpolation(point_list)
    
    # Determine the pixels where the curve intersects the border of the Image
    intersect_border = _image_border_finding([pixel_x, pixel_y], interpolation)
    
    # Create a copy of the inputted Image
    draw_image = copy(image)

    # Create a Color to draw the line with based on the inputted colour string
    color = _determine_color(colour)

    # Draw the curve from left to right, starting at the first border intersection
    for i in range(intersect_border[0][0], pixel_x):
        # Get the y value of the pixel using the coefficients and the x value
        y_value = int(np.polyval(interpolation, i))
        # Set the color of the pixel at that x and y value
        if 0 <= y_value < pixel_y:
            set_color(draw_image, i, y_value, color)
        # Draw 4 pixels above and below the line
        for j in range(4):
            # Determine if the above y-value is still in the Image
            if 0 <= y_value + j + 1 < pixel_y:
                # Set the color of the pixel at that x and above y-value
                set_color(draw_image, i, y_value + j + 1, color)
            # Determine if the below y-value is still in the Image
            if 0 <= y_value - j + 1 < pixel_y:
                # Set the color of the pixel at that x and below y-value
                set_color(draw_image, i, y_value - j + 1, color)
    # Return the Image with the curve and the intersecting border points
    return (draw_image, intersect_border)

def flip_horizontal(image: Image) -> Image:
    """
    T081 Matthew Gray
    Reviewed by: Taytum George
    
    Returns a copy of the Image flipped horizontally.
    
    >>> file = load_image(choose_file()) 
    >>> flipped_horizontal_image = flip_horizontal(file)
    >>> show(flipped_horizontal_image)
    """
    new_image = copy(image)
    
    X = get_width(image)
    Y = get_height(image)
    
    for x in range(X // 2):
        for y in range(Y):
            r1, g1, b1 = get_color(image, x, y)
            pixel1 = create_color(r1, g1, b1)
            r2, g2, b2 = get_color(image, X - x - 1, y)
            pixel2 = create_color(r2, g2, b2)
            set_color(new_image, X - x -1, y, pixel1)
            set_color(new_image, x, y, pixel2)
    return new_image

def flip_vertical (image: Image) -> Image: 
    """
    T081 Taytum George
    Reviewed by: Matthew Gray
    
    Takes the given image, and returns a version of that image which has had a 
    "vertical flip" applied to it's entirety (flipping the image, by reflecting
    all individual pixels over an x-axis made by a horizontal line bisecting 
    the original image at half its height).
    
    >>> file = load_image(choose_file())
    >>> vertical_flipped_image = vertical(file)
    >>> show(vertical_flipped_image)
    """
    # Finding the height of the image (how tall it is)
    inputted_image_height = get_height(image)

    # Making a copy of the image to apply the flip to
    vertical_flipped_image = copy(image)
    
    # Taking the color of each cell, and translating that color to a cell with
    # the same X coordinate, and a negate Y coordinate (thereby flipping it)
    for x, y, (r, g, b) in image:
        color = create_color(r, g, b)
        set_color (vertical_flipped_image, x, -y, color)
    return vertical_flipped_image