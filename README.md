# AIFab_Inference

# Pre-request: 
you have to have a orch tenant with AI Fab

# Call the predict with demo Model in folder P
1. Zip the P folder, which contains the transfer-learning model with flowers, and upload it to AI Fab as ML package, choose "file" as input type
   
2. Create a ML skill in AI Fab, with the ML package, takes ~3min to finish deploy

3. Connect the robot to the Orch with AI Fab, Open the workflow with UiPath Studio community 19.10, select the ML skill to the one you had just created.

4. Run the workflow, Select a image file, and wait 5-10 sec, will get the result in json

# Retrain your own image dataset
1. Set up the python enviroment, with tensorflow 2.0, or Tensorflow-gpu if you have an GPU of Nvidia

2. Run retrain_tf2.py with your folder as input

3. Copy your model file and label into P\model

4. Run main.py in folder P to have a test

# TBD as next step
1. I will provide a ipynb and documents next month for easier training without python env

# License
This project is under [Apache License](http://www.apache.org/licenses/LICENSE-2.0), since the retrain.py is based on the demo of Google Tensorflow hub
