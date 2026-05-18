from PIL import Image
import numpy as np

def ft_load(path: str):
 """Loads an image, prints its format, and its pixels
content in RGB format"""

 if not path.lower().endswith((".jpg", ".jpeg")):
  raise ValueError("Error: Wrong format. JPG or JPEG only")

 try:
   img = Image.open(path)
   rgb_im = img.convert("RGB")
   pixels = np.array(rgb_im)

 except FileNotFoundError:
  raise FileNotFoundError("Error: File not found")

 except OSError:
  raise OSError("Error: Cannot open image")

 shape = pixels.shape
 print(f"The shape of image is: {shape}")

 return pixels
