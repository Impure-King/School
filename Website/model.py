import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow import (keras)
from tensorflow.keras import (losses,
                              optimizers,
                              Sequential)
from tensorflow.keras.layers import (Dense,
                                     BatchNormalization,
                                     ReLU,
                                     Reshape,
                                     Conv2DTranspose,
                                     Conv2D,
                                     Activation)

from matplotlib import pyplot as plt

init = tf.keras.initializers.RandomNormal(stddev=0.02)

# Building a Generator:
def build_generator(seed_size):
    """
    Builds the generator model
    
    Parameters:
        seed_size: size of the random vector fed into the generator
    
    Returns:
        model: keras model representing the generator
    """
    model = Sequential()
  
    # Block - 1
    model.add(Dense(6*6*1024,kernel_initializer=init,input_dim=seed_size))
    model.add(BatchNormalization())
    model.add(ReLU())
    model.add(Reshape((6,6,1024))) # Resulting shape = (6,6,1024) 

    # Block - 2
    model.add(Conv2DTranspose(512,kernel_size=5,strides=2,padding='same',use_bias=False,kernel_initializer=init))
    model.add(BatchNormalization())
    model.add(ReLU())  # Resulting shape = (12,12,512)

    # Block - 3
    model.add(Conv2DTranspose(256,kernel_size=5,strides=2,padding='same',use_bias=False,kernel_initializer=init))
    model.add(BatchNormalization())
    model.add(ReLU()) # Resulting shape = (24,24,256)

    # Block - 4
    model.add(Conv2DTranspose(128,kernel_size=3,strides=2,padding='same',use_bias=False,kernel_initializer=init))
    model.add(BatchNormalization())
    model.add(ReLU()) # Resulting shape = (48,48,128)

    # Block - 5
    model.add(Conv2DTranspose(3,kernel_size=3,strides=2,padding='same',use_bias=False,kernel_initializer=init))
    model.add(Activation('tanh')) # Resulting shape = (96,96,3)

    return model

# Weight loader and Predictor:

def generate_faces(generator, seed_size = 128):
    """Generates random Anime faces"""
    
    # generate 64 images by giving 64 inputs
    noise = tf.random.normal([2,seed_size])
    generated_images = generator(noise)

    fig = plt.figure(figsize=(12,12))
    for i in range(generated_images.shape[0]):
        plt.subplot(1,2,i+1)
        # Convert to range [0,1] for plt.imshow()
        plt.imshow((generated_images[i,:,:,:]*0.5+0.5))
        plt.axis("off")
    plt.savefig('static\generated.jpg')
    plt.show()

def load_save(model):
    model.load_weights("generator_weights-test.h5")
    generate_faces(model)

model = build_generator(seed_size=128)
model = load_save(model)
