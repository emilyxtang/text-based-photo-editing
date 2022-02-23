"""
ECOR 1042 T081
Emily Tang
Alexander Bundgaard
Last edited: Mar. 31, 2021

File-Based Batch User Interface
"""

# Import Cimpl and all of the Image filters except for draw_curve
import Cimpl
from T081_image_filters import three_tone, extreme_contrast, sepia, posterize, detect_edges, flip_horizontal, flip_vertical

# Prompt the user for the name of the batch file
batch_file_name = input("Please enter the name of the batch file: ")

# Open the batch file
batch = []
with open(batch_file_name) as batch_file:
    # Read all the lines of the batch file and return them as a list of strings
    batch_lines = []
    for line in batch_file:
        batch_lines = line.split(" ")
        batch.append(batch_lines)

# Go through the lines of the batch file
for i in range(len(batch)):
    # Open the Image to be manipulated
    image = Cimpl.load_image(batch[i][0])
    # Perform all the Image manipulations
    for j in range(2, len(batch[i])):
        # Perform all the image manipulations
        if batch[i][j] == "3":
            image = three_tone(image, "aqua", "blood", "lemon")
        elif batch[i][j] == "X":
            image = extreme_contrast(image)
        elif batch[i][j] == "T":
            image = sepia(image)
        elif batch[i][j] == "P":
            image = posterize(image)
        elif batch[i][j] == "E":
            image = detect_edges(image, 15)
        elif batch[i][j] == "V":
            image = flip_vertical(image)
        elif batch[i][j] == "H":
            image = flip_horizontal(image)
    # Save the results to the designated file
    Cimpl.save_as(image, batch[i][1])