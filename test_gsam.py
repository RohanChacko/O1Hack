import replicate


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
    
def GSAM(image_url, prompt):

    output = replicate.run(
        "okaris/grounded-sam:cc9418bf8c2163cdf72f5d39b0607ac4bbf7b99add7fd9b191fb6b0f8814194d",
        input={
            "image": image_url,
            "mask_prompt": prompt,
            "adjustment_factor": -5
        }
    )

    # The predict method returns an iterator, and you can iterate over that output.
    for idx, file_output in enumerate(output):
        with open(f'output_{idx}.png', 'wb') as f:
            f.write(file_output.read())

if __name__ == "__main__":
    # Replace these variables with your values
    image_path = "/Users/rohanc/Downloads/1661545915123.jpeg"

    public_url = upload_image_to_cloudinary(image_path)

    if public_url:
        print("Image successfully uploaded.")
        print("Public URL:", public_url)
        GSAM(public_url, "person")

    # else:
    #     print("Image upload failed.")
