from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
from scipy import signal as sg
from scipy.ndimage import filters


def get_coordinates(image, kernel, channel, brightness):
    convolved = sg.convolve(image[:, :, channel], kernel[:, :, channel], mode = 'full')
    plt.imshow(convolved, cmap='gray')
    coordinates = np.argwhere(convolved > brightness)

    return coordinates


def get_tfls(image_name):
    image = plt.imread(image_name)
    img_for_kernel = plt.imread('tfl_for_kernel.png')
    red_kernel = img_for_kernel[90:95, 1460:1465]
    green_kernel = img_for_kernel[127:132, 1420:1425]
    red_coordinates = get_red_coordinates(image)
    green_coordinates = get_green_coordinates(image)

    # plt.plot(green_coordinates[:, 1], green_coordinates[:, 0], 'g+')
    plt.plot(red_coordinates[:, 1], red_coordinates[:, 0], 'r+')
    plt.show()
    return red_coordinates[:, 0], red_coordinates[:, 1], green_coordinates[:, 0], green_coordinates[:,1]


def get_red_coordinates(image):
    img_for_kernel = plt.imread('tfl_for_kernel.png')
    red_kernel = img_for_kernel[87:92, 1455:1460] # TODO change the crope? [90:95, 1460:1465]
    return get_coordinates(image, red_kernel, 0, 11)



def get_green_coordinates(image):
    img_for_kernel = plt.imread('tfl_for_kernel.png')
    green_kernel = img_for_kernel[127:132, 1420:1425]
    return get_coordinates(image, green_kernel, 1, 17)


get_tfls('ppp.png')