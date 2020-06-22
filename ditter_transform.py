###Author : Harsha Arya###
###Date   : 22-06-2020###

from PIL import Image
from PIL import ImageFilter
import os
import argparse

def im_converted(directory):
    for img in os.listdir(directory):
        im = Image.open(directory+img)
        im_converted=im.convert('1')
        im_converted.save(directory+img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="blur")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')

    args = parser.parse_args()
    im_converted(args.directory)
