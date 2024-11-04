import streamlit as st
import numpy as np
import os
from PIL import Image

st.title("Free-form photoshop")


# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    image = st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    image_array = np.array(Image.open(uploaded_file))

st.subheader("Image Gallery")

# Placeholder for the gallery
gallery_placeholder = st.empty()

gallery_images = []
for filename in os.listdir("./working_examples/"):
    image_path = os.path.join("./working_examples/", filename)
    gallery_images.append(np.array(Image.open(image_path)))

# Display the gallery
cols = st.columns(len(gallery_images))
for idx, col in enumerate(cols):
    with col:
        st.image(gallery_images[idx], use_column_width=True)

    

