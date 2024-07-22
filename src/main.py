import os
from PIL import Image

def load_image(path):
    try:
        image = Image.open(path)
        return image
    except IOError:
        print("Unable to load image")
        return None

def convert_to_grayscale(image):
    return image.convert('L')

ASCII_CHARS = "@%#*+=-:. "

def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return ascii_str

def generate_ascii_art(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width) / 2  # Adjusting for character proportions
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    grayscale_image = convert_to_grayscale(resized_image)
    
    ascii_str = map_pixels_to_ascii(grayscale_image)
    img_width = grayscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    return ascii_img

def save_ascii_art(ascii_art, path):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, "w") as f:
        f.write(ascii_art)

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the path to save the ASCII art: ")
    image = load_image(image_path)
    if image:
        ascii_art = generate_ascii_art(image)
        print(ascii_art)
        save_ascii_art(ascii_art, output_path)
