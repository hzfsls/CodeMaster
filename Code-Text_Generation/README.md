# Code-Text Generation

## Code-Text Generation Task

Code-Text Generation is the first pre-training task we apply on CodeT5 model. It's similar to code summarization task, but we split each sentence in the comment so one code snippet can generate multiple natural language comments.

### Dependency

- torch
- transformers

### Pre-train

We pre-train the model on 2*1080Ti GPUs. It takes about 60 hours for 5 epoch pre-training.

You can run the following scripts for pre-training a model on original CodeT5 model with code-text generation task:

`bash java_script.sh [gpu-id] [model-name]`

`bash python_script.sh [gpu-id] [model-name]`

### Pre-training Data

We have Java and Python pre-training data for this task.

Java Data -- [CodeSum_Data](https://github.com/xing-hu/TL-CodeSum)
Python Data -- [Code_Docstring_Corpus](https://github.com/EdinburghNLP/code-docstring-corpus)

You can get the dataset through the above repository, or through [our link](https://drive.google.com/drive/folders/1M7wVQB6ul6OUDpphQaQ7HT2VyEs30v3o?usp=sharing).

We extract code-comment pairs in the above datasets, and change the data format to "train.code" and "train.comment" files. The data in './data' folder are all full data without preprocessing, so if you simply use these data to run the pre-training task, you will get much higher score on CodeQA compared to our results since the code snippets in these data cover part of code snippets in the test set.

In our paper, we deduplicate the dataset, filter code-comment pairs with the same code snippet in the dev/test set, split the comment into sentences and remove all sentences which are not natural language. If you're interested, you can preprocess the data by yourself.

### Get Pre-trained Models

You can choose to download CodeT5(CTG) model on [Google Drive](https://drive.google.com/drive/folders/1DsZvOcGMXjswps1I5_AuOMWVvzZQDFWk?usp=sharing).















