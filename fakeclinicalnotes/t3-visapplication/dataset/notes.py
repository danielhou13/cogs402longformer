from datasets import load_dataset
from transformers import AutoTokenizer
import numpy as np
import pdb


def preprocess_function(tokenizer, example, max_length):
    example.update(tokenizer(example['text'], padding='max_length', max_length=max_length, truncation=True))
    example['tokens'] = list(map(tokenizer.convert_ids_to_tokens, example['input_ids']))
    return example

def get_notes_dataset(dataset_type):
    max_length = 256
    dataset = load_dataset("danielhou13/cogs402datafake")[dataset_type]
    new_col = list(np.arange(0, len(dataset)))
    dataset = dataset.add_column("idx", new_col)
    visualize_columns = dataset.column_names
    visualize_columns = ['idx', 'text', 'labels']

    tokenizer = AutoTokenizer.from_pretrained('allenai/longformer-base-4096')
    dataset = dataset.map(lambda x: preprocess_function(tokenizer, x, max_length), batched=True)

    setattr(dataset, 'visualize_columns', visualize_columns)
    setattr(dataset, 'input_columns', ['input_ids', 'attention_mask'])
    setattr(dataset, 'target_columns', ['labels'])
    setattr(dataset, 'max_length', max_length)
    setattr(dataset, 'tokenizer', tokenizer)
    return dataset

def notes_train_set():
    return get_notes_dataset('train')

def notes_test_set():
    return get_notes_dataset('test')
