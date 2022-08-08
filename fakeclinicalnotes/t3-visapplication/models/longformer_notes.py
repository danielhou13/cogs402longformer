import torch.nn as nn
import torch
from transformers import AutoModelForSequenceClassification
import pdb

def longformer_finetuned_notes():
    test = torch.load("/content/drive/MyDrive/cogs402longformer/models/full_augmented_lr2e-5_dropout3_10_trained_threshold.pt")
    model = AutoModelForSequenceClassification.from_pretrained('allenai/longformer-base-4096', state_dict=test['state_dict'], num_labels = 2)
    setattr(model, 'num_hidden_layers', model.config.num_hidden_layers)
    setattr(model, 'num_attention_heads', model.config.num_attention_heads)
    setattr(model, 'hidden_size', model.config.hidden_size)
    return model