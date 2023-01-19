import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras
import tensorflow as tf
from matplotlib import pyplot as plt

# Weight loader and Predictor:

def generate_faces(generator, seed_size = 128):
    """Generates random Anime faces"""
    
    # generate 64 images by giving 64 inputs
    noise = tf.random.normal([1,seed_size])
    generated_images = generator(noise)

    fig = plt.figure(figsize=(12,12))
    for i in range(generated_images.shape[0]):
        plt.subplot(1,2,i+1)
        # Convert to range [0,1] for plt.imshow()
        plt.imshow((generated_images[i,:,:,:]*0.5+0.5))
        plt.axis("off")
    plt.savefig(r'Website/static/generated.jpg')

def load_save():
    model = keras.models.load_model(r'Website/weights/generator-test')
    generate_faces(model)


