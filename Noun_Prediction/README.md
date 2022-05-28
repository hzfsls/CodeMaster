# Noun Prediction

## Noun Prediction Task

Noun Prediction is the second pre-training task we apply on CodeT5 model. It requires the model to predict the masked noun phrase in the input according to the input code snippet and natural language sentence with a noun phrase masked.

### Dependency

- torch
- transformers

### Pre-training Data

We use the same corpus as the code-text generation task, and extract noun phrase to fit the format of input of this task. See '../Noun_Extract' for generating files to run this pre-training task.

### Pre-train

After you generate files(train.code, train.before, train.after and train.target) for this task, put then under './data/Java-NP-Data' or './data/Python-NP-Data' folder.

We pre-train the model on 2*1080Ti GPUs. It takes about 120 hours for 5 epoch pre-training.

You can run the following scripts for pre-training a model on original CodeT5 model with noun prediction task:

`bash java_script.sh [gpu-id] [model-name]`

`bash python_script.sh [gpu-id] [model-name]`

Or you can run the following scripts for pre-training a CodeT5-based model which is applied other pretraining task.
(You should rename the model file as "pytorch_model.bin" and put the file under './models/my_pretrained_model/' or modify the load_model_path params before running the scripts):

`bash java_script_use_pretrained.sh [gpu-id] [model-name]`

`bash python_script_use_pretrained.sh [gpu-id] [model-name]`




### Get Pre-trained Models

You can choose to download CodeT5(CTG+NP) model on [Google Drive](https://drive.google.com/drive/folders/1DsZvOcGMXjswps1I5_AuOMWVvzZQDFWk?usp=sharing).















