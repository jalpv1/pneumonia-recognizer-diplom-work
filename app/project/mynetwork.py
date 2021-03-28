from click.testing import Result
from keras.models import load_model
from keras_preprocessing.image import ImageDataGenerator

def recognize_image():
        ans = "no"
        image_size = 128
        datagen = ImageDataGenerator(rescale=1. / 255)
        from numpy.random import seed
        seed(1)
        model = load_model('E:/Documents/diplomaDev/pneumonia-recogognizer-app/my_model')
        model.summary()
        one_img = datagen.flow_from_directory(
                'E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images',
                target_size=(image_size, image_size),
                color_mode="grayscale",
                batch_size=1,
                class_mode='categorical')
        y_pred = model.predict(one_img)
        print(y_pred)
        anwer = create_answer(y_pred)
        return anwer

def create_answer(y_pred):
   result = 'unknown'
   probability = y_pred[0][0]*100
   conclusion ='unknown'
   status = 'unknown'
   pneumonia_probability = str(y_pred[0][0])
   if(probability<40):
       result = "was`t detected."
       status = "NORMAL"
       conclusion = "The probability of pneumonia disease is low"
   if (probability > 41 and probability < 59):
       result = "was detected."
       status = "INTERMEDIATE"
       conclusion = "The probability of pneumonia disease is intermediate. Additional expert analysis required."
   if (probability > 60 and probability < 70):
       result = " was detected."
       status = "UPPER-INTERMEDIATE"
       conclusion = "The probability of pneumonia disease is high. Doctor consultation required."
   if (probability > 70):
       result = "was detected."
       status = "CRITICAL"
       conclusion = "The probability of pneumonia disease is very high. Doctor consultation required, immediately."
   data = {'conclusion': conclusion, 'probability': str(round(probability)) + "%", 'status': status,'result':result}
   return data