# AIFab_Inference

pre-condition: you have to have a orch tenant with AI Fab

1. Zip the P folder, which contains the transfer-learning model with flowers, and upload it to AI Fab as ML package, choose "file" as input type
   
2. Create a ML skill in AI Fab, with the ML package, takes ~3min to finish deploy

3. Connect the robot to the Orch with AI Fab, Open the workflow with UiPath Studio community 19.10, select the ML skill to the one you had just created.

4. Run the workflow, Select a image file, and wait 5-10 sec, will get the result in json

