from PIL import Image
import numpy as np

def ft_load(path: str):

 img = Image.open(path)
 rgb_im = img.convert('RGB')
 pixels = np.array(rgb_im)
 shape = pixels.shape
 print(f"The shape of image is: {shape}")
 return pixels