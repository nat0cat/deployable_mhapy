import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np
from .model import Model

class BERT(Model):
    def __init__(self, path:str):
        self.path = path
        self.model = self.load_BERT(self.path)

    def give_score(self, text:str)->int:
        return self.run_model(text)
    
    def load_BERT(self, path:str)->nn.Module:
        """
        This function is used to load the BERT model last layer from the path provided. We will then load back the model  and return it
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

        if train_on_gpu:
            gpu_count = torch.cuda.device_count()
            if gpu_count > 1:
                multi_gpu = True
            else:
                multi_gpu = False
        

        #Here is the issue: We are loading using map_location since it's the only way it run on my local machine but then it creates 
                #an issue when assigning to the model's classifier which needs an array
        last_layer = torch.load(path, map_location = device)

        model = BertForSequenceClassification.from_pretrained(
            'bert-base-uncased', num_labels = 4,output_attentions = False,output_hidden_states = False
            )
        weights = last_layer

        # We load the last layer of the model
        new_layer = nn.Linear(in_features=768, out_features=4, bias=True) 
        new_layer.load_state_dict(weights)

        
        model.classifier = new_layer

        model.to(device)

        return model
    
    def bert_encode(texts:str)->np.array:
    
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

        tokenized = tokenizer.encode_plus(texts,add_special_tokens=False,max_length=391,
        padding='max_length',
        truncation=True,
        return_tensors='pt',
        return_attention_mask=False,
        return_token_type_ids=False)
        
        return tokenized['input_ids'][0]
    
    def get_predictions(data_set:torch.tensor, model:nn.Module):
        """
        This function is used to get the predictions from the model on the data set provided.
        Args:
        data_set: nn.tensor: The data set on which the model is run
        model: nn.Module: The model which is run on the data set
        Returns:
        predictions: nn.tensor: The predictions from the model on the data set
        """
        # We run the model on the data set
        # if model is None:
        #     raise ValueError("Model is not initialized")
        
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
        
        data_point = data_set.unsqueeze(0).to(device)
        predictions = model(data_point).logits

        prediction = torch.argmax(predictions, dim=1)
        
        return prediction.item()
    
    def run_model(self, text:str)->np.array:
        """
        This function calls get_model to get the model and then runs the model on the test data and returns the predictions.
        We also print in the terminal a clear formatted message to show the user that the model is running and at the end what`s the result"""

        # We load our model 
        model = self.model

        vector = self.bert_encode(text)

        # Now we run the model on the test data
        predictions = self.get_predictions(vector, model)


        return predictions
