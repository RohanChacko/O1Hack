import cv2
import numpy as np
from functions import *
import os

# Step 1: Make the dining counter look more modern and sleek
input_image_path = './images/agi_house.jpg'

# Generate mask for the dining counter
GSAM(input_image_path, 'wooden')
# Rename the mask to 'dining_counter_mask.png' to prevent overwriting
os.rename('output_mask.png', 'dining_counter_mask.png')

# Inpaint the dining counter to make it look modern
inpainted_data_1 = INPAINTING(input_image_path, 'modern counter', 'dining_counter_mask.png')

# Convert inpainted data to image
nparr = np.frombuffer(inpainted_data_1, np.uint8)
inpainted_img_1 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# Save intermediate result
cv2.imwrite('image_step1.jpg', inpainted_img_1)

# Step 2: Remove the cans in the image
# Generate mask for the cans
GSAM('image_step1.jpg', 'cans')
# Rename the mask to 'cans_mask.png'
os.rename('output_mask.png', 'cans_mask.png')

# Inpaint to remove the cans
inpainted_data_2 = INPAINTING('image_step1.jpg', '', 'cans_mask.png')

# Convert inpainted data to image
nparr = np.frombuffer(inpainted_data_2, np.uint8)
inpainted_img_2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# Save intermediate result
cv2.imwrite('image_step2.jpg', inpainted_img_2)

# Step 3: Remove the windows and make it look like concrete
# Generate mask for the windows
GSAM('image_step2.jpg', 'windows')
# Rename the mask to 'windows_mask.png'
os.rename('output_mask.png', 'windows_mask.png')

# Inpaint to remove windows and make it look like concrete
final_inpainted_data = INPAINTING('image_step2.jpg', 'concrete', 'windows_mask.png')

# Convert final inpainted data to image
nparr = np.frombuffer(final_inpainted_data, np.uint8)
final_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

# Save final image
cv2.imwrite('final_image.jpg', final_img)
