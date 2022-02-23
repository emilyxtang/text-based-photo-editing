"""
ECOR 1042 T081
Taytum George
Matthew Gray
Edited by: Emily Tang
Last edited: Apr. 5, 2021

Interactive User Interface
"""

# Import Cimpl and Image Filters
from Cimpl import *
from T081_image_filters import three_tone, extreme_contrast, sepia, posterize, detect_edges, draw_curve, flip_vertical, flip_horizontal

# Variable to determine whether the program should continue to run or now
running = True

# Variable to determine whether if a valid Image was selected by the user or not
image = 0

def check_valid_command(command: str) -> bool:
    """
    T081 Emily Tang
    
    Checks if the user entered a valid command based on the inputted string.
    
    >>> check_valid_command("3")
    True
    >>> check_valid_command("f")
    False
    """
    # List of valid commands for the interactive user interface
    VALID_COMMANDS = ["L", "l", "S", "s", "3", "X", "x", "T", "t", "P", "p", 
                      "E", "e", "D", "d", "V", "v", "H", "h", "Q", "q"]
    # Determine if the command is valid or not
    if command in VALID_COMMANDS:
        return True
    else:
        return False

def show_and_save_image(image: Image) -> Image:
    """
    T081 Emily Tang
    
    Shows the inputted Image to the user and returns it.
    
    >>> show_and_save_image(three_tone_image)
    three_tone_image
    """
    # Display the Image to the user
    show(image)
    # Return the Image to the user
    return image

while(running == True):
    # Four-line menu of commands
    print("L)oad image  S)ave-as")
    print("3)-tone X)treme contrast T)int sepia P)osterize")
    print("E)dge detect D)raw curve V)ertical flip H)orizontal flip")
    print("Q)uit")
    print("")
    choose = input(": ")
    
    # Notify the user that an invalid command has been entered
    if check_valid_command(choose) == False:
        print("No such command")
    
    # Allow the user to select an Image file
    elif (choose == "L" or choose == "l"):
        file = choose_file()
        # Load the Image
        image = load_image(file)
        # Show the Image to the user
        show(image)     
    
    # Notify the user if they have not inputted an Image file yet
    elif (image == 0):
        print("No image loaded")     
    
    # Save the current Image to a file
    elif(choose == "S" or choose == "s"):
        # Saves the Image to a file called "untitled"
        save_as(image)
    
    # Apply the three-tone filter to the Image and show it to the user
    elif(choose == "3"):
        three_tone_image = three_tone(image, "lemon", "blood", "aqua")
        image = show_and_save_image(three_tone_image)
    
    # Apply the extreme contrast filter to the Image and show it to the user
    elif(choose == "X" or choose == "x"):
        xtreme_image = extreme_contrast(image)
        image = show_and_save_image(xtreme_image)
    
    # Apply the sepia filter to the Image and show it to the user
    elif(choose == "T" or choose == "t"):
        sepia_tint_image = sepia(image)
        image = show_and_save_image(sepia_tint_image)
    
    # Apply the posterize filter to the Image and show it to the user
    elif(choose == "P" or choose == "p"):
        posterized_image = posterize(image)
        image = show_and_save_image(posterized_image)
    
    # Apply the edge detection filter to the Image and show it to the user
    elif(choose == "E" or choose == "e"):
        image_threshold = int(input("Threshold?: "))
        edge_image = detect_edges(image, image_threshold)
        image = show_and_save_image(edge_image)
    
    # Apply the draw curve filter to the Image and show it to the user
    elif(choose == "D" or choose == "d"):
        curve_on_image = draw_curve(image, "lemon")
        image = show_and_save_image(curve_on_image[0])
        
    # Apply the flip vertical filter to the Image and show it to the user
    elif(choose == "V" or choose == "v"):
        vert_image = flip_vertical(image)
        image = show_and_save_image(vert_image)
    
    # Apply the flip horizontal filter to the Image and show it to the user
    elif(choose == "H" or choose == "h"):
        horiz_image = flip_horizontal(image)
        image = show_and_save_image(horiz_image)
    
    # Terminate the program 
    elif(choose == "Q" or choose == "q"):
        running = False