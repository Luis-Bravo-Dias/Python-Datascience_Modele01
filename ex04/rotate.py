from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def main():

    try:
        img = ft_load("animal.jpeg")
        print(img)
        height, width = img.shape[0], img.shape[1]
        
        y_center = height // 2
        x_center = width // 2
        
        zoom = img[
         y_center - 200 : y_center + 200,
         x_center - 200 : x_center + 200
		]
        #grayscale
        zoom = np.mean(zoom, axis=2)
        
		#float to int
        zoom = zoom.astype(np.uint8)
        
		#rotate  
        h = len(zoom)
        w = len(zoom[0])
        rot = []
        
        for x in range(w):
         new_row = []
         for y in range(h):
          new_row.append(zoom[y][x])
         rot.append(new_row)
        

        rot = np.array(rot)
        print(f"New shape after Transpose: {rot.shape}")
        print(rot)
        plt.imshow(rot.squeeze(), cmap="gray")
        plt.show()

    except ValueError as error:
        print(error)

    except FileNotFoundError as error:
        print(error)

    except OSError as error:
        print(error)


if __name__ == "__main__":
    main()