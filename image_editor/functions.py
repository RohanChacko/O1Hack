import requests
import base64
import os
import replicate
# Example usage
API_KEY = "" # Add here
os.environ["REPLICATE_API_TOKEN"] = "" # add here

# Function to convert an image file from the filesystem to base64
def image_file_to_base64(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return base64.b64encode(image_data).decode('utf-8')

# Function to call the SD inpainting API
def INPAINTING(image_path, prompt, mask_path, api_key=API_KEY):
    """
    Perform inpainting on an image using the Segmind API.
    Args:
        image_path (str): Path to the input image file.
        prompt (str): Text prompt describing the desired inpainting.
        mask_path (str): Path to the mask image file.
        api_key (str): API key for authentication with the Segmind API.
    Returns:
        bytes: The generated image data if the request is successful.
        None: If the request fails, returns None and prints an error message.
    """

    url = "https://api.segmind.com/v1/flux-inpaint"

    # Request payload
    data = {
    "base64": False,
    "guidance_scale": 7.5,
    "image": image_file_to_base64(image_path),  # Or use image_file_to_base64("IMAGE_PATH")
    "image_format": "jpeg",
    "mask": image_file_to_base64(mask_path),  # Or use image_file_to_base64("IMAGE_PATH")
    "negative_prompt": "bad quality, painting, blur",
    "num_inference_steps": 25,
    "prompt": prompt,
    "quality": 95,
    "sampler": "euler",
    "samples": 1,
    "scheduler": "simple",
    "seed": 12467,
    "strength": 1.0
    }

    headers = {'x-api-key': api_key}
    
    response = requests.post(url, json=data, headers=headers)
    # Check the response
    if response.status_code == 200:
        return response.content  # This would be the generated image data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def CONTROLNET(image_path, prompt, controlnet_type, api_key=API_KEY):
    """
    Generates an image based on the given prompt and controlnet type using the Segmind API.
    Args:
        image_path (str): The path to the input image.
        prompt (str): The text prompt to guide the image generation.
        controlnet_type (str): The type of controlnet to use. Must be one of ["canny", "depth", "pose", "tile"].
        api_key (str, optional): The API key for authentication. Defaults to API_KEY.
    Returns:
        bytes: The generated image data if the request is successful.
        None: If the request fails, returns None and prints the error message.
    """

    url = "https://api.segmind.com/v1/flux-controlnet"
    
    assert controlnet_type in ["canny", "depth", "pose", "tile"]
    # Request payload
    data = {
    "base64": False,
    "cn_stop": 0.5,
    "cn_strength": 0.45,
    "cn_type": controlnet_type,
    "custom_height": 1024,
    "custom_width": 1024,
    "guidance": 3.5,
    "image": image_file_to_base64(image_path),  # Or use image_file_to_base64("IMAGE_PATH")
    "image_format": "jpeg",
    "prompt": prompt,
    "quality": 95,
    "sampler": "euler",
    "samples": 1,
    "scheduler": "simple",
    "seed": 652889,
    "steps": 20,
    "use_input_img_dimension": False
    }

    headers = {'x-api-key': api_key}

    response = requests.post(url, json=data, headers=headers)
    # Check the response
    if response.status_code == 200:
        return response.content  # This would be the generated image data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def upload_image_to_cloudinary(image_path):
    """
    Uploads an image to Cloudinary and returns the public URL.

    :param image_path: Path to the image file
    :return: Public URL of the uploaded image or None if failed
    """
    import cloudinary
    import cloudinary.uploader

    # Configuration       
    cloudinary.config( 
        cloud_name = "dinldkxvr", 
        api_key = "727274748126377", 
        api_secret = "165LAzqYM33dXACOYb8f1O2xslc",
        secure=True
    )
    try:
        # Upload an image
        # cloudinary.uploader.upload(image_path, public_id="image")
        # srcURL = cloudinary.CloudinaryImage("image").build_url()
        # return srcURL
        upload_result = cloudinary.uploader.upload(image_path, public_id="image")
        return upload_result["secure_url"]

    except Exception as e:
        print("An error occurred during upload:", e)
        return None
    
def GSAM(image_path, prompt):
    """
    Takes in an image and a prompt, and return the corresponding binary mask output. 
    Stores the mask as 'output_mask.png' in the current directory, which can be further used for further tasks.

    Args:
        image_path (str): The file path to the input image.
        prompt (str): The mask prompt to guide the model.

    Returns:
        None

    """
    image_url = upload_image_to_cloudinary(image_path)
    output = replicate.run(
        "okaris/grounded-sam:cc9418bf8c2163cdf72f5d39b0607ac4bbf7b99add7fd9b191fb6b0f8814194d",
        input={
            "image": image_url,
            "mask_prompt": prompt,
            "adjustment_factor": 15
        }
    )

    # The predict method returns an iterator, and you can iterate over that output.
    for idx, file_output in enumerate(output):
        if idx == 2:
            with open(f'output_mask.png', 'wb') as f:
                f.write(file_output.read())


if __name__=="__main__":
    image_path = "./images/image1.jpg"
    prompt = "a man rowing a boat on a lake"
    # result = SD_INPAINTING(API_KEY, image_path, mask_path, prompt)
    result = CONTROLNET_CANNY(image_path, prompt)
    if result:
        with open("output_image.png", "wb") as f:
            f.write(result)
        print("Image saved as 'output_image.png'")

