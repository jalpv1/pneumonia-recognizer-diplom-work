from click.testing import Result
from keras.models import load_model
from keras_preprocessing.image import ImageDataGenerator

def recognize_image():
        ans = "no"
        image_size = 256
        datagen = ImageDataGenerator(rescale=1. / 255)
        from numpy.random import seed
        seed(1)
        model = load_model('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/my_model')
        model.summary()
        one_img = datagen.flow_from_directory(
                'E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images',
                target_size=(image_size, image_size),
                color_mode="grayscale",
                batch_size=1,
                class_mode='binary')
        y_pred = model.predict(one_img)
        print(y_pred)
        anwer = create_answer(y_pred)
        return anwer

def create_answer(y_pred):
   answer = y_pred[0] > 0.5
   result = 'unknown'
   probability = str(y_pred[0][0])
   conclusion ='unknown'
   status ='unknown'
   if (answer[0] == True):
       result = "Pneumonia was detected. The probability of disease is about "
       conclusion = " Doctor consultation required."
   if (answer[0] == False):
      result = "Pneumonia was`t detected. The probability of disease is about "
   conclusionstatus = (y_pred[0]>0.6)
   if(conclusionstatus[0]==True):
      conclusion = conclusion+ " The probability is closed to 50%. The expert analysis required"
   statusWARNING = (y_pred[0] < 0.6 and y_pred[0] > 0.4 )
   if(statusWARNING == True):
       status = "WARNING"
   statusWARNING = (y_pred[0] > 0.6)
   if (statusWARNING == True):
       status = "CRITICAL"
   statusWARNING = (y_pred[0] < 0.40)
   if (statusWARNING == True):
       status = "NORMAL"
   data = {'conclusion': conclusion, 'probability': probability, 'status': status,'result':result}
   return data