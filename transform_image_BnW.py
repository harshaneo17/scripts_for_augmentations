###Author : Harsha Arya###
###Date   : 22-06-2020###

from PIL import Image
import os
import argparse
def black_and_white_images(directory):
    for img in os.listdir(directory):
        im = Image.open(directory+img)
        im_converted = im.convert('L')
        im_converted.save(directory+img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="black_and_white")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')

    args = parser.parse_args()
    black_and_white_images(args.directory)
