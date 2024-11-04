# import cv2
# import numpy as np

# def load_image(image_path):
#     image = cv2.imread(image_path, cv2.IMREAD_COLOR)
#     if image is None:
#         raise FileNotFoundError(f"Image at path '{image_path}' not found.")
#     return image

# def overlay_text(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, 
#                                   font_scale=1, color=(255, 255, 255), thickness=2, 
#                                   background_color=None, padding=5, alpha=0.6):
#     """
#     Overlay semi-transparent text on an image at the specified position.

#     Args:
#         image (numpy.ndarray): The original image.
#         text (str): The text to overlay.
#         position (tuple): (x, y) coordinates for the text.
#         font: OpenCV font type.
#         font_scale (float): Font scale factor.
#         color (tuple): Text color in BGR.
#         thickness (int): Thickness of the text.
#         background_color (tuple, optional): Background color in BGR. If None, no background.
#         padding (int): Padding around the text if background is used.
#         alpha (float): Transparency factor (0.0 fully transparent, 1.0 fully opaque).

#     Returns:
#         image (numpy.ndarray): Image with semi-transparent text overlay.
#     """
#     x, y = position
#     (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

#     # Create an overlay image
#     overlay = image.copy()

#     if background_color:
#         # Draw rectangle background on the overlay
#         cv2.rectangle(overlay, 
#                       (x - padding, y - text_height - padding), 
#                       (x + text_width + padding, y + baseline + padding), 
#                       background_color, 
#                       thickness=cv2.FILLED)

#     # Put the text on the overlay
#     cv2.putText(overlay, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

#     if background_color:
#         # Blend the overlay with the original image
#         cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
#     else:
#         # If no background, blend only the text
#         cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

#     return image


# def add_top_text(image, text):
#     height, width, _ = image.shape
#     font_scale = 1.5
#     thickness = 3
#     color = (255, 255, 255)  # White
#     background_color = (0, 0, 0)  # Black
    
#     text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
#     text_x = (width - text_size[0]) // 2
#     text_y = text_size[1] + 20  # 20 pixels from top
    
#     image = overlay_text(image, text, (text_x, text_y), 
#                         font_scale=font_scale, 
#                         color=color, 
#                         thickness=thickness, 
#                         background_color=background_color, 
#                         padding=10)
#     return image

# def add_bottom_left_info(image, date_text, location_text):
#     height, width, _ = image.shape
#     margin = 20
#     icon_size = (30, 30)  # Width, Height
    
#     # Overlay calendar icon
#     # image = overlay_icon(image, 
#     #                      (margin, height - icon_size[1] - margin), 
#     #                      icon_size=icon_size)
    
#     # Add date text
#     text_x = margin + icon_size[0] + 10
#     text_y = height - margin
#     font_scale = 0.8
#     thickness = 2
#     color = (255, 255, 255)  # White
#     background_color = (0, 0, 0)  # Black
#     alpha = 0.6

#     image = overlay_text(image, date_text, (text_x, text_y), 
#                         font_scale=font_scale, 
#                         color=color, 
#                         thickness=thickness, 
#                         background_color=background_color, 
#                         padding=5,
#                         alpha=alpha)
    
#     # Overlay location icon
#     location_icon_x = margin
#     location_icon_y = height - icon_size[1] - margin - 50  # 50 pixels above date

    
#     # Add location text
#     loc_text_x = margin + icon_size[0] + 10
#     loc_text_y = height - margin - 50  # Align with location icon
#     image = overlay_text(image, location_text, (loc_text_x, loc_text_y), 
#                         font_scale=font_scale, 
#                         color=color, 
#                         thickness=thickness, 
#                         background_color=background_color, 
#                         padding=5,
#                         alpha=alpha)
    
#     return image

# def save_image(image, save_path):
#     cv2.imwrite(save_path, image)

# def display_image(image, window_name='Image'):
#     cv2.imshow(window_name, image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# def main():
#     # Paths to resources
#     original_image_path = '/Users/rohanc/Downloads/1661545915123.jpeg'  # Update this path
#     # calendar_icon_path = 'icons/calendar.png'      # Update this path
#     # location_icon_path = 'icons/location.png'      # Update this path
#     output_image_path = './final_image.jpg'  # Update this path
    
#     # Load original image
#     image = load_image(original_image_path)
    
#     # Add top text
#     top_text = "think slow & think deep with O1"
#     image = add_top_text(image, top_text)
    
#     # Add bottom left info
#     date_text = "Nov 2nd 11:00 AM"
#     location_text = "AGI House"
#     image = add_bottom_left_info(image, date_text, location_text)
    
#     # Save the final image
#     save_image(image, output_image_path)
    
#     # Optionally, display the image
#     # display_image(image, 'Final Image')

# if __name__ == "__main__":
#     main()
