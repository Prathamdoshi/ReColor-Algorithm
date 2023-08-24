# importing libraries
from rembg import remove
from PIL import Image
import os
import extcolors
import webcolors

input_path = "/Users/prathamdoshi/PycharmProjects/ReColor/raw_images/"
output_path = "/Users/prathamdoshi/PycharmProjects/ReColor/images/"

inventory = {}

counter = 1

for filename in os.listdir(input_path):

    input_path_formatted = os.path.join(input_path, filename)
    output_path_formatted = os.path.join(output_path, filename)
    output_path_formatted = output_path_formatted.replace(".jpeg", ".png")

    input_image = Image.open(input_path_formatted)
    output = remove(input_image)

    colors, pixel_count = extcolors.extract_from_image(output)

    print(f"Processing: {filename}, {counter} file out of {len(os.listdir(input_path))}")
    counter += 1

    max_val = 0

    for c in colors:

        # print(f"{c[0]}  :  {round(c[1] / pixel_count * 100, 2)}% ({c[1]})")

        if round(c[1] / pixel_count * 100, 2) > max_val:
            max_val = round(c[1] / pixel_count * 100, 2)

            inventory[filename] = c[0]

    output.save(output_path_formatted)


def color_name_to_rgb(color_name):
    try:
        rgb_tuple = webcolors.name_to_rgb(color_name)
        return rgb_tuple

    except ValueError:
        return None


# Ask the user for their favorite color
user_favorite_color = input("Enter your favorite color: ")

# Convert the color name to RGB
rgb_value = color_name_to_rgb(user_favorite_color)

# Display the RGB value
if rgb_value:
    print(f"The RGB value of {user_favorite_color} is: {rgb_value}")
else:
    print(f"Sorry, '{user_favorite_color}' is not a recognized color name.")


def calculate_color_similarity(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5


recommendation = {}

for i in inventory:
    recommendation[i] = calculate_color_similarity(tuple(rgb_value), inventory[i])

final = {k: v for k, v in sorted(recommendation.items(), key=lambda item: item[1])}

final_output = list(final.items())[:5]
print(final_output)
