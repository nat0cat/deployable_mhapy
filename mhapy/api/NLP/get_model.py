"In this file We implement the get_model which will be used to get the model from model.pth. using pytorch "

# Importing the required libraries

import os

from .BERT_mini import BERT_mini
from .BERT import BERT



def get_model(path:str, model_type:str):
    """
    This function is used to get the model from the path provided. It loads the model into a class regardless of the model type.(Vader, BERT, LSTM, etc.)
    Args:
    string: str: The path of the model file
    model_type: str: The type of the model that is being loaded
    Returns:
    model: The model which is loaded from the path
    """


    # We check if the path is empty
    if path == "":
        raise ValueError("No path has been provided")
 
    # We check if the path is valid
    if not os.path.exists(path):
        raise ValueError("The path provided is not valid")
    
    # We check if the model type is valid
    if model_type == "":
        raise ValueError("No model type has been provided")
    
    # We load the model according to the model type
    if model_type == "BERT":
        model = BERT(path)
    elif model_type == "BERT_mini":
        model = BERT_mini(path)

    return model

