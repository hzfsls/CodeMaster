# CodeQA-CodeT5

## Experiment on CodeT5

The code is mainly copied from [CodeQA](https://github.com/jadecxliu/CodeQA/tree/main/codeBERT) with some minor modification.

### Dependency

- pytorch
- transformers

### Finetune

We fine-tune the model on 2*1080Ti GPUs.

You can run the following scripts for finetuning a model for CodeQA using original CodeT5 model:

`bash java_script.sh [gpu-id] [model-name]`

`bash python_script.sh [gpu-id] [model-name]`

Or you can run the following scripts for finetuning a model for CodeQA using a pre-trained CodeT5-based model.
(You should rename the model file as "pytorch_model.bin" and put the file under './models/my_pretrained_model/' or modify the load_model_path params before running the scripts):

`bash java_script_use_pretrained.sh [gpu-id] [model-name]`

`bash python_script_use_pretrained.sh [gpu-id] [model-name]`

These scripts will automatically run test after training. You can also run 'java_script_test.sh' or 'python_script_test.sh' scripts to get the result without training. See [CodeQA](https://github.com/jadecxliu/CodeQA/tree/main/codeBERT) for details.






















