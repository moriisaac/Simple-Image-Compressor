'''
Author: Mori Isaac Wesonga
Date: 2020-05-05
Description: This is a simple image compressor
Don't Forget to star

'''


import PIL
from PIL import Image
import argparse

def compress_image(input_directory, output_directory, compression_level):
    image = Image.open(input_directory)

    # Compress the image
    image.save(output_directory, "JPEG", optimize=True, quality=compression_level)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_directory", help="The path to the directory containing the images to be compressed.")
    parser.add_argument("output_directory", help="The path to the directory where the compressed images will be saved.")
    parser.add_argument("compression_level", type=int, help="An integer value between 1 and 100 that specifies the level of compression.")
    args = parser.parse_args()

    compress_image(args.input_directory, args.output_directory, args.compression_level)
