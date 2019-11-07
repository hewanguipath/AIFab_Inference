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
        """Load the model and labels."""
        self.loaded = tf.saved_model.load('model')
        labels_path = os.path.join('model', "label.txt")    
        self.imagenet_labels = np.array(open(labels_path).read().splitlines())
        
    def predict(self, file):
        """Load the image and resize to moblenet size 224x224."""
        img = tf.keras.preprocessing.image.load_img(BytesIO(file), target_size=[224, 224])
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = tf.keras.applications.mobilenet.preprocess_input(x[tf.newaxis,...])
        
        """Load the model and labels."""
        if not self.loaded:
            self.load()
        
        """Imported signatures always return dictionaries."""
        infer = self.loaded.signatures[list(self.loaded.signatures.keys())[0]]
        
        """The 1st Key of structured output is the output layer's name"""
        result = infer(tf.constant(x))[list(infer.structured_outputs.keys())[0]]
        
        dictOfRes = dict(zip(self.imagenet_labels, np.asarray(result[0])))
        TopXdictOfRes = Counter(dictOfRes).most_common(5) 
    
        return json.dumps({
            k : str(round(v*100)) for k, v in TopXdictOfRes
            })

if __name__ == "__main__":
    main = Main()
    with open(r"c:\tmp\images.jpg", "rb") as image:
        f = image.read()
        b = bytearray(f)
        
    print(main.predict(b))

