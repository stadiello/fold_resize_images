from PIL import Image
import os

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.LANCZOS)
        img.save(output_path)

def resize_images_in_directory(directory, size):
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".webp") or filename.endswith(".jfif"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, filename)
            resize_image(input_path, output_path, size)
            print(f"Resized {filename} to {size}")

resize_images_in_directory("C:\\Users\\stadiello\\Documents\\blog\\docs\\images", (150, 150))
