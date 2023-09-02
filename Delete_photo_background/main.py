from rembg import remove
from PIL import Image

input_path = ''                     # place of image
output_path = 'Output_image_1.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)