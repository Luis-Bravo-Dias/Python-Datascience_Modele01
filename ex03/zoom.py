from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():

    try:
        img = ft_load("animal.jpeg")
        print(img)
        height, width = img.shape[0], img.shape[1]
        
        zoom_size = min(height, width) // 4
        y_center = height // 2
        x_center = width // 2
        
        zoom = img[
         y_center - zoom_size : y_center + zoom_size,
         x_center - zoom_size : x_center + zoom_size
		]
        
        zoom = np.mean(zoom, axis=2)
        print(f"Zoomed image shape: {zoom.shape}")
        print(zoom)
        plt.imshow(zoom, cmap="gray")
        plt.show()

    except ValueError as error:
        print(error)

    except FileNotFoundError as error:
        print(error)

    except OSError as error:
        print(error)


if __name__ == "__main__":
    main()