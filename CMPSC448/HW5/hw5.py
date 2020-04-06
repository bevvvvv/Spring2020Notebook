import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Input, Conv1D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras import backend, optimizers
from tensorflow.keras import applications
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from itertools import repeat
import os

# instantiate variables/training params
img_width, img_height = 28, 28

train_data_dir = './train'
validation_data_dir = './validate'
nb_train_samples = 48000 # according to Kaggle 60k total
nb_validation_samples = 12000
number_of_epochs = 20
batch_size = 200

# Requires 3 channels when reading from png
# Only use 1 channel from csv or greyscale
input_shape = (img_width, img_height, 1)

# Create Deep Net Model
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, kernel_regularizer=keras.regularizers.l2(0.001)))
model.add(Activation('relu'))
model.add(Dense(256, kernel_regularizer=keras.regularizers.l2(0.001)))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10, kernel_regularizer=keras.regularizers.l2(0.001)))
model.add(Activation('softmax'))


model.compile(loss='sparse_categorical_crossentropy',
              optimizer='rmsprop',  
              metrics=['accuracy'])

# load data (from csv)
def train_generator():
    with open('fashion-mnist_train.csv', "r") as csv1:
          while True:
              reader1 = csv.reader(csv1)
              next(reader1) # skip headers
              count = 1
              batch_count = 1
              batch = []
              batch_labs = []
              for row1 in reader1:
                  row = list(map(lambda x: [x], row1)) # one channel
                  if count > nb_train_samples:
                      break
                  # create 28 by 28 image
                  img = []
                  steps = (img_height * img_width) // img_width 
                  img.append(row[1:1+img_width])
                  for i in range(steps):
                      img.append(row[i * img_width:(i * img_width) + img_width])
                  # add image to current batch
                  batch.append(img)
                  batch_labs.append(row[0])
                  if batch_count == batch_size:
                      yield (np.array(batch, dtype=np.float), np.array(batch_labs, dtype=np.float))
                      batch_count = 1
                  count += 1
                  batch_count += 1
              del reader1

def validation_generator():
    with open('fashion-mnist_train.csv', "r") as csv1:
          while True:
              reader1 = csv.reader(csv1)
              next(reader1) # skip headers
              count = 1
              batch_count = 1
              batch = []
              batch_labs = []
              for row1 in reader1:
                  if count <= nb_train_samples:
                      count += 1
                      continue
                  row = list(map(lambda x: [x], row1)) # one channel
                  # create 28 by 28 image
                  img = []
                  steps = (img_height * img_width) // img_width 
                  img.append(row[1:1+img_width])
                  for i in range(steps):
                      img.append(row[i * img_width:(i * img_width) + img_width])
                  # add image to current batch
                  batch.append(img)
                  batch_labs.append(row[0])
                  if batch_count == batch_size:
                      yield (np.array(batch, dtype=np.float), np.array(batch_labs, dtype=np.float))
                      batch_count = 1
                  count += 1
                  batch_count += 1
              del reader1

# load data (images with auto augmentation)
train_datagen = ImageDataGenerator(rescale=1. / 255)#,
                                   #shear_range=0.2,
                                   #zoom_range=0.2,
                                   #horizontal_flip=True)


test_datagen = ImageDataGenerator(rescale=1. / 255)

train_gen = train_datagen.flow_from_directory(train_data_dir,
                                                    target_size=(img_width, img_height),
                                                    batch_size=batch_size,
                                                    color_mode='grayscale',
                                                    class_mode='sparse')

validation_gen = test_datagen.flow_from_directory(validation_data_dir,
                                                        target_size=(img_width, img_height),
                                                        batch_size=batch_size,
                                                        color_mode='grayscale',
                                                        class_mode='sparse')

#train_gen = train_generator()
#validation_gen = validation_generator()

# Display model description
model.summary()

# Train model on data
model.fit(x=train_gen,
          steps_per_epoch = (nb_train_samples // batch_size),
          epochs = number_of_epochs,
          validation_data = validation_gen,
          validation_steps = (nb_validation_samples // batch_size))

# save trained model
model.save_weights('./second_try_double_epoch.h5')

"""## Recap Training"""

history = model.history

history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

epochs = range(1, len(history_dict['accuracy']) + 1)

plt.plot(epochs, loss_values, 'r', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()


history_dict = history.history
accu_values = history_dict['accuracy']
val_accu_values = history_dict['val_accuracy']

plt.plot(epochs, accu_values, 'r', label='Training Accuracy')
plt.plot(epochs, val_accu_values, 'b', label='Validation Accuracy')
plt.title('Training and validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

"""## Predictions"""

# create order

file_names = []
for i in range(1, 10001):
    file_names.append('./img' + str(i) + '.png')
df = pd.DataFrame({'filename': file_names})

test_datagen = ImageDataGenerator(rescale=1. / 255)

test_data_dir = './test'
test_gen = test_datagen.flow_from_dataframe(df, directory = test_data_dir,
                                                        target_size=(img_width, img_height),
                                                        batch_size=batch_size,
                                                        color_mode='grayscale',
                                                        shuffle=False,
                                                        class_mode=None)
                       
#print(df.filename)
# can load weights here if model created
predictions = model.predict(test_gen)

index = 0
with open('./submission_sepich.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Id", "predicted"])
    for image_pred in predictions:
        class_pred = np.argmax(image_pred)
        writer.writerow([index, class_pred])
        index += 1
print('Done')