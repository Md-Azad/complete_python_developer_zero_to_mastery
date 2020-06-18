import sys
import os

from PIL import Image

imege_folder = sys.argv[1]

output_folder = sys.argv[2]

if not os.path.exists( output_folder):

    os.makedirs(output_folder)

for filename in os.listdir(imege_folder):
    img = Image.open(f'{imege_folder}{filename}')

    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')

    print('successfully converted')