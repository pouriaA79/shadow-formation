import numpy as np
from matplotlib import image
import matplotlib.pyplot as plt
# function to get image
def get_image():
    user_input = input("enter directory: ")
    image_data = image.imread(user_input)

    return image_data


def make_shadows(row, column, image, img_data):
    for i in range(row):
        for j in range(row):
            if (img_data[i][j][0] >= 230) and (img_data[i][j][1] >= 230) and (img_data[i][j][2] >= 230):
                image[i][j] = (255, 255, 255)
            else:
                image[i][j] = (128, 128, 128)
    for j in range(row):
        for i in range(row, int(column * 1.3)):
            image[j][i] = (255, 255, 255)
    return image


def transform(row, column, image, new_image):
    for j in range(row):
        for i in range(row):
            if (image[j][i][0] == 128) and (image[j][i][1] == 128) and (image[j][i][2] == 128):
                (k, t) = np.dot((i, j), shear_matrix)
                # print(t, k)
                new_image[int(t)][int(k)] = (128, 128, 128)
    return new_image


def final_picture(row, new_image, img_data):
    for j in range(row):
        for i in range(row):
            if (img_data[i][j][0] <= 230) or (img_data[i][j][1] <= 230) or (img_data[i][j][2] <= 230):
                new_image[i][j] = (255, 255, 255)
                new_image[i][j] = img_data[i][j]
    return new_image


if __name__ == '__main__':
    img_data = get_image()
    # get number of rows and columns of image
    row, column, x = img_data.shape

    # make 2 image first for shadows and second for final image
    image = np.zeros((row, int(column * 1.3), 3), dtype='uint8')
    new_image = np.zeros((row, int(column * 1.3), 3), dtype='uint8')
    # make image of shadows
    image = make_shadows(row, column, image, img_data)

    shear_matrix = ([1, 0], [0.1, 1])
    # make new_image white
    for j in range(row):
        for i in range(int(column * 1.3)):
            new_image[j][i] = (255, 255, 255)
    # transform shadows
    new_image = transform(row, column, image, new_image)

    # make final image
    new_image = final_picture(row, new_image, img_data)

    plt.imshow(new_image)
    plt.show()
