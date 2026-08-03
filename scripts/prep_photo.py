from PIL import Image
from rembg import remove
import cv2
import numpy as np

# Read the original image
input_image = Image.open("PHOTO.jpg")

# Remove the background
output_image = remove(input_image)

# Create a white background
white_bg = Image.new("RGB", output_image.size, (255, 255, 255))

# Paste the person onto the white background
white_bg.paste(output_image, mask=output_image.split()[3])

# Save temporarily
white_bg.save("white_bg.png")