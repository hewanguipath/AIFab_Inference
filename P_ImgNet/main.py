# Made by WangHe, for UiPath Ai Fab demo only
# he.wang@uipath.com
import json
import os
import tensorflow as tf
import numpy as np
from io import BytesIO
from collections import Counter 


class Main:
    def __init__(self):
        self.loaded = None   
    
    def load(self):
        self.imagenet_labels = np.array(open('ImageNetLabels.txt').read().splitlines())
        self.model = tf.keras.applications.MobileNetV2()
        self.loaded = True   
        
    def predict(self, file):
        img = tf.keras.preprocessing.image.load_img(BytesIO(file), target_size=[224, 224])
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = tf.keras.applications.mobilenet.preprocess_input(x[tf.newaxis,...])

        if not self.loaded:
            self.load()
        result = self.model(x)

        dictOfRes = dict(zip(self.imagenet_labels, np.asarray(result[0])))
        TopXdictOfRes = Counter(dictOfRes).most_common(5) 
        #print (TopXdictOfRes)

        return json.dumps({k : str(round(v*100)) for k, v in TopXdictOfRes})


if __name__ == "__main__":
    main = Main()
    with open(r"C:\Users\He.Wang\Pictures\WeChat Image_20190307163317.jpg", "rb") as image:
        f = image.read()
        b = bytearray(f)
        
    print(main.predict(b))


