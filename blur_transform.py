###Author : Harsha Arya###
###Date   : 22-06-2020###

from PIL import Image
from PIL import ImageFilter
import os
import argparse

def blur_images(directory):
    for img in os.listdir(directory):
        im = Image.open(directory+img)
        im_blurred=im.filter(ImageFilter.BLUR)
        im_blurred.save(directory+img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="blur")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')

    args = parser.parse_args()

    blur_images(args.directory)
