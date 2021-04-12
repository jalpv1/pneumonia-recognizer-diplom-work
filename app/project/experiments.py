from click.testing import Result
from keras.models import load_model
from keras_preprocessing.image import ImageDataGenerator
import keras, tensorflow
import numpy as np
def recognize_image():
    ans = "no"
    image_size = 128
    datagen = ImageDataGenerator(rescale=1. / 255)
    from numpy.random import seed
    seed(1)
    model = load_model('E:/Documents/diplomaDev/pneumonia-recogognizer-app/my_model')
    sess = tensorflow.compat.v1.keras.backend.get_session()
    img = tensorflow.compat.v1.read_file('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/static/images/p1.jpeg')
    img = tensorflow.image.decode_jpeg(img, channels=1)
    img.set_shape([None, None, 1])
    img = tensorflow.compat.v1.image.resize_images(img, (32, 32))
    img = img.numpy()  # convert to numpy array
    img = np.expand_dims(img, 0)  # make 'batch' of 1
    model.summary()

    y_pred = model.predict(img)
    print(y_pred)
    return y_pred

recognize_image()