# importing libraries
from rembg import remove
from PIL import Image
import os


"""
Function: remove_background
Params: Input directory path & Output directory path
Returns: None
Purpose: Removes background of all the files in the input directory and pastes in output directory. 
"""

def remove_background(input_path, output_path):

    for filename in os.listdir(input_path):

        input_path_formatted = os.path.join(input_path, filename)
        output_path_formatted = os.path.join(output_path, filename)
        output_path_formatted = output_path_formatted.replace(".jpeg",".png")

        input = Image.open(input_path_formatted)
        output = remove(input)
        output.save(output_path_formatted)

input_path = "/Users/prathamdoshi/PycharmProjects/ReColor/raw_images/"
output_path = "/Users/prathamdoshi/PycharmProjects/ReColor/images/"

# remove white background out of all the files in raw_images and images
remove_background(input_path,output_path)

