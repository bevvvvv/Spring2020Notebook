import csv
import numpy as np
import matplotlib.pyplot as plt
import imageio

train_data_dir = './train'
validation_data_dir = './validate'
test_data_dir = './test'
input_data_dir = './csvdata'
nb_train_samples = 48000 # according to Kaggle 60k total
nb_validation_samples = 12000

img_width, img_height = 28, 28
'''
with open(input_data_dir + '/fashion-mnist_train.csv', "r") as csv1:
    reader1 = csv.reader(csv1)
    next(reader1) # skip headers
    count = 1
    is_training = True
    for row1 in reader1:
        if count > nb_train_samples:
            is_training = False
        if count > nb_train_samples + nb_validation_samples:
            break
        # create 28 by 28 image
        img = []
        steps = (img_height * img_width) // img_width 
        img.append(row1[1:1+img_width])
        for i in range(steps):
            img.append(row1[i * img_width:(i * img_width) + img_width])

        H = np.array(img, dtype=np.float)
        # subdirs are class names
        if is_training:
            imageio.imwrite(train_data_dir + '/' + str(row1[0]) + '/img' + str(count) + '.png', H)
        else:
            imageio.imwrite(validation_data_dir + '/' + str(row1[0]) + '/img' + str(count) + '.png', H)
        count += 1
'''
with open(input_data_dir + '/fashion-mnist_test.csv', "r") as csv1:
    reader1 = csv.reader(csv1)
    next(reader1) # skip headers
    count = 1
    for row1 in reader1:
        # create 28 by 28 image
        img = []
        steps = (img_height * img_width) // img_width 
        img.append(row1[1:1+img_width])
        for i in range(steps):
            img.append(row1[i * img_width:(i * img_width) + img_width])

        H = np.array(img, dtype=np.float)
        # subdirs are class names
        imageio.imwrite(test_data_dir + '/img' + str(count) + '.png', H)
        count += 1

