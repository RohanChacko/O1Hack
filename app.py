import streamlit as st
import numpy as np
import time
from PIL import Image

st.title("Photoshop ka bap")

# Text input for chat
user_input = st.text_input("You: ", "")

# Display the user input
if user_input:
    st.write("You: " + user_input)

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    image = st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    image_array = np.array(Image.open(uploaded_file))
    

