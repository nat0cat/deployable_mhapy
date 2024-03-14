from .model import Model
import torch
from transformers import BertTokenizer
import numpy as np


class BERT_mini(Model):
    def __init__(self, path:str):
        self.path = path
        self.model = None
        self.load_BERT_mini()
    
    def tokenize(self, text:str)->np.array:
        tokenizer = BertTokenizer.from_pretrained('prajjwal1/bert-mini', do_lower_case=True)
        
        tokenized = tokenizer.encode_plus(text, add_special_tokens=False,max_length=200,
        padding='longest',
        truncation=True,
        return_tensors='pt',
        return_attention_mask=False,
        return_token_type_ids=False)
        
        return tokenized['input_ids']
        
    def give_score(self, text:str)->int:
        
        if torch.cuda.is_available(): 
            dev = "cuda" 
        else: 
            dev = "cpu" 
        device = torch.device(dev) 
        train_on_gpu = torch.cuda.is_available()

        # Number of gpus
        if train_on_gpu:
            gpu_count = torch.cuda.device_count()
            if gpu_count > 1:
                multi_gpu = True
            else:
                multi_gpu = False
        
        tokenized_text = self.tokenize(text).to(device)
        logits = self.model(tokenized_text).logits
        prediction = torch.argmax(logits, dim=1)
        return prediction.item()
            
    def load_BERT_mini(self):
        """
        This function is used to load the ENTIRE BERT model from the path provided. We will then load back the model and return it
        Args:
        string: str: The path of the model file
        Returns:
        model: The BERT model which is loaded from the path
        """
        if torch.cuda.is_available(): 
            dev = "cuda" 
        else: 
            dev = "cpu" 
        device = torch.device(dev) 
        train_on_gpu = torch.cuda.is_available()

        # Number of gpus
        if train_on_gpu:
            gpu_count = torch.cuda.device_count()
            if gpu_count > 1:
                multi_gpu = True
            else:
                multi_gpu = False
        
        model = torch.load(self.path, map_location = device)
        
        model.to(device)

        self.model = model
