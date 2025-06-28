from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import array_to_img, img_to_array, load_img

#Passing the paramenters in the constructor of the ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range = 40,
    shear_range = 0.2,
    zoom_range = 0.4,
    horizontal_flip = True,
    brightness_range = ((0.5, 1.5))
)

img = load_img("/content/drive/MyDrive/Jeep Wrangler.jpg")
x = img_to_array(img)
x = x.reshape((1,) + x.shape)

import os

# Create the directory if it does not exist
os.makedirs('preview', exist_ok=True)

#Generating 5 samples using the defined parameters
i = 0
for batch in datagen.flow(x, batch_size = 1, save_to_dir = 'preview',save_prefix = 'image', save_format= 'jpeg'):
  i += 1
  if i > 5:
    break