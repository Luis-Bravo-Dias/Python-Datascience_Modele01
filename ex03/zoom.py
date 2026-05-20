from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():

    try:
        img = ft_load("animal.jpeg")
        print(img)
        height, width = img.shape[0], img.shape[1]

        y_center = height // 2
        x_center = width // 2

        zoom = img[
         y_center - 200: y_center + 200,
         x_center - 200: x_center + 200
        ]
        # grayscale
        zoom = np.mean(zoom, axis=2, keepdims=True)

        # float to int
        zoom = zoom.astype(np.uint8)

        print(f"New shape after slicing: {zoom.shape}")
        print(zoom)
        plt.imshow(zoom.squeeze(), cmap="gray")
        plt.show()

    except ValueError as error:
        print(error)

    except FileNotFoundError as error:
        print(error)

    except OSError as error:
        print(error)


if __name__ == "__main__":
    main()
