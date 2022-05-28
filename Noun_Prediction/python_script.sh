    cd code
lang=python #programming language
lr=5e-5
batch_size=8
beam_size=10
source_length=512 
target_length=100
data_dir=../data/Python-NP-Data
output_dir=../output/$2
train_file=$data_dir/
epochs=5
pretrained_model=Salesforce/codet5-base

CUDA_VISIBLE_DEVICES=$1 python run.py \
    --model_type codet5 \
    --model_name_or_path $pretrained_model \
    --train_filename $train_file \
    --output_dir $output_dir \
    --max_source_length $source_length \
    --max_target_length $target_length \
    --beam_size $beam_size \
    --train_batch_size $batch_size \
    --eval_batch_size $batch_size \
    --learning_rate $lr \
    --num_train_epochs $epochs \
    --do_train \
    --do_eval \
    --do_test 





