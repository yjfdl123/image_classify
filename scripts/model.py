#encoding=utf-8
from tensorflow import keras
from keras.applications import mobilenet
from tensorflow.keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.layers import Dense,GlobalAveragePooling2D
import numpy as np
from tensorflow.keras.models import Model
import util, config 

class ImageModel(object):
    def __init__(self):
        self.model_mobilenet = None
        self.basemodel_name = "mobilenet"
        self.base_version = util.get_hour_str()
        self.cur_model_name = "" 
        self.cur_model_version = ""

    def preprocessing_image(self, img_path, target_size, architecture):
        img = image.load_img(img_path, target_size=target_size)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = architecture.preprocess_input(x)
        return x

    def load_model(self):
        self.model_mobilenet = mobilenet.MobileNet(weights='imagenet')
        cur_version = util.get_hour_str()
        new_model_name = self.basemodel_name + "_" + cur_version 
        new_model_version = cur_version
        self.cur_model_name, self.cur_model_version = new_model_name, new_model_version
        print("init modelname:%s version:%s" % (new_model_name, new_model_version))
        return new_model_name, new_model_version



    def predict_image(self, img_path):
        x_mobilenet = self.preprocessing_image(img_path, (224, 224), mobilenet)
        preds_mobilenet = self.model_mobilenet.predict(x_mobilenet)
        print('Predicted MobileNet:', decode_predictions(preds_mobilenet, top=5)[0])
        ret = decode_predictions(preds_mobilenet, top=2)[0]
        ret = ret[0]
        score = round(float(ret[2]), 4)
        return self.cur_model_name, self.cur_model_version, score 

    def finetune_model(self):
        base_model=mobilenet.MobileNet(weights='imagenet',include_top=False)
        x=base_model.output
        x=GlobalAveragePooling2D()(x)
        #x=Dense(1024,activation='relu')(x) #we add dense layers so that the model can learn more complex functions and classify for better results.
        #x=Dense(1024,activation='relu')(x) #dense layer 2
        x=Dense(512,activation='relu')(x) #dense layer 3
        predictions=Dense(2,activation='softmax')(x) #final layer with softmax activation

        model = Model(inputs=base_model.input, outputs=predictions)
        for i,layer in enumerate(model.layers):
            print(i,layer.name)
        for layer in base_model.layers:
            layer.trainable=False
        dir_path = config.DIR_UPLOAD_DATA
        train_ds = keras.utils.image_dataset_from_directory(
            directory=dir_path,
            labels='inferred',
            label_mode='categorical',
            batch_size=32,
            image_size=(256, 256))
        model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])
        model.fit(train_ds, epochs=3)
        
        cur_version = util.get_hour_str()
        new_model_name = self.basemodel_name + "_" + cur_version 
        new_model_version = cur_version
        print("init modelname:%s version:%s" % (new_model_name, new_model_version))
        self.cur_model_name, self.cur_model_version = new_model_name, new_model_version
        return new_model_name, new_model_version



if __name__ == "__main__":
    obj = ImageModel()
    # print(predict_image())
    # print(finetune_model())
    print(1)