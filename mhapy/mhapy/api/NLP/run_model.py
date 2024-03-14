"""
In the File we implement the Runnin of the Model

We implement the run_model which will be used to run the model on the test data and return the predictions
"""
# import model
# import BERT_mini
# import BERT
from .get_model import *


def run_model(text:str, model_path:str, model_type:str)->int:
    """
    This function calls get_model to get the model and then runs the model on the test data and returns the predictions
    """

    # We load our model 
    model = get_model(model_path, model_type)

    prediction = model.give_score(text)

    return prediction
