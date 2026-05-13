from PIL import Image
import numpy as np

def ft_load(path: str):

 if not path.lower().endswith((".jpg", ".jpeg")):
  print("Error: Wrong format. JPG or JPEG only")
  return
 
 try:
  img = Image.open(path)
  rgb_im = img.convert('RGB')
  pixels = np.array(rgb_im)

 except FileNotFoundError:
  print("Error: File not found")
  return
 
 except OSError:
  print("Error: Cannot open image")
  return

 shape = pixels.shape
 print(f"The shape of image is: {shape}")
 return pixels
