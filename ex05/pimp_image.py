from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array):
 """Inverts the color of the image received."""
 inv = array.copy()
 inv = 255 - inv
 print(f"The shape of inv-image is: {inv.shape}")
 print(inv)
 plt.imshow(inv)
 plt.show()
 return inv

def ft_red(array):
 """Makes the image red"""
 red = array.copy()
 red = red * [1, 0, 0]
 print(f"The shape of red-image is: {red.shape}")
 print(red)
 plt.imshow(red)
 plt.show()
 return red

def ft_green(array):
 """Makes the image green"""

 green = array.copy()
 #remove red channel
 green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
 #remove blue channel
 green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
 print(f"The shape of green-image is: {green.shape}")
 print(green)
 plt.imshow(green)
 plt.show()
 return green

def ft_blue(array):
 """Makes the image blue"""

 blue = array.copy()
 #remove red channel
 blue[:, :, 0] = 0
 #remove green channel
 blue[:, :, 1] = 0
 print(f"The shape of blue-image is: {blue.shape}")
 print(blue)
 plt.imshow(blue)
 plt.show()
 return blue

def ft_grey(array):
 """Makes the image grey"""

 grey = array.copy()

 #grey[:, :, 0] = grey[:, :, 0] / 3
 #grey[:, :, 1] = grey[:, :, 1] / 3
 #grey[:, :, 2] = grey[:, :, 2] / 3
 #grey[:, :, 0] = grey[:, :, 0] + grey[:, :, 1] + grey[:, :, 2]
 #grey[:, :, 1] = grey[:, :, 0]
 #grey[:, :, 2] = grey[:, :, 0]

 grey[:, :, 0] = grey[:, :, 0] / 3
 grey[:, :, 1] = grey[:, :, 0]
 grey[:, :, 2] = grey[:, :, 0]


 print(f"The shape of grey-image is: {grey.shape}")
 print(grey)
 plt.imshow(grey)
 plt.show()
 return grey
