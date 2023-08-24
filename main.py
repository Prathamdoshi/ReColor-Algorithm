# importing libraries
from rembg import remove
from PIL import Image
import os
import extcolors

"""
Function: remove_background
Params: Input directory path & Output directory path
Returns: None
Purpose: Removes background of all the files in the input directory and pastes in output directory. 
"""

input_path = "/Users/prathamdoshi/PycharmProjects/ReColor/raw_images/"
output_path = "/Users/prathamdoshi/PycharmProjects/ReColor/images/"

inventory = {}

for filename in os.listdir(input_path):

        input_path_formatted = os.path.join(input_path, filename)
        output_path_formatted = os.path.join(output_path, filename)
        output_path_formatted = output_path_formatted.replace(".jpeg",".png")

        input = Image.open(input_path_formatted)
        output = remove(input)

        colors, pixel_count = extcolors.extract_from_image(output)

        print(f"{filename}")

        max_val = 0

        for c in colors:

           # print(f"{c[0]}  :  {round(c[1] / pixel_count * 100, 2)}% ({c[1]})")

           if round(c[1] / pixel_count * 100, 2) > max_val:

                   max_val = round(c[1] / pixel_count * 100, 2)

                   inventory[filename] = c[0]





        output.save(output_path_formatted)

print(inventory)