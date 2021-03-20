from PIL import Image
import numpy as np
from scipy import ndimage

img = Image.open('E:/Documents/diploma/data/chest_xray/train/PNEUMONIA/person111_virus_209.jpeg')
fer =ndimage.sobel(img)
fer.show()