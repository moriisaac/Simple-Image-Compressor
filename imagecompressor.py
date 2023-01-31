'''
Author: Mori Isaac Wesonga
Date: 2020-05-05
Description: This is a simple image compressor
Don't Forget to star

'''




import PIL
from PIL import Image
from tkinter.filedialog import *


def main():
    print("\033[32m", "Welcome to the image compressor😇", "\033[0m")
    compressImage()

def compressImage():
    # Open the image
    file = askopenfilename()
    image = Image.open(file)

    # Compress the image
    image.save('compressed.jpg',"JPEG", optimize=True, quality=50)

    # Show the image
    image.show()


if __name__ == "__main__":
    main()
