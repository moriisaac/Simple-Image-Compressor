Simple Image Compressor

A simple and easy-to-use Python script to compress images.

Requirements

Python 3
Pillow library
Usage
Clone the repository to your local machine and run the following command in the terminal:

php

Copy code
python image_compressor.py <input_directory> <output_directory> <compression_level>
Where:

input_directory is the path to the directory containing the images to be compressed.
output_directory is the path to the directory where the compressed images will be saved.
compression_level is an integer value between 1 and 100 that specifies the level of compression. A higher value results in a smaller file size but lower image quality.
Example

javascript
Copy code
python image_compressor.py ~/images/ ~/compressed_images/ 70
This will take all the images in the ~/images/ directory, compress them with a compression level of 70, and save the compressed images in the ~/compressed_images/ directory.

Note
The script will only compress JPEG and PNG images. Any other image formats will be ignored.
