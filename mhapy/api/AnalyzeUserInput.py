from .NLP.run_model import *
import os

def AnalyzeUserInput(user_input, issue : int):
    """
    Analyzes the user input against a issue and it's score.

    This function simulates the analysis of a user's input for a given question
    by generating a random integer within the range of available options for the question.
    It primarily serves as a placeholder for more complex analysis logic.

    Parameters:
    - user_input (str): The input provided by the user. Currently not used in the function.
    - question (Question): An object representing the question, expected to have an attribute
      `question_options` which indicates the number of options available for the question.

    Returns:
    int: A random integer between 1 and the number of options available for the question.

    Note:
    The current implementation does not use the `user_input` parameter, as it only demonstrates
    the structure of such a function. Future implementations should incorporate analysis of
    `user_input` to generate meaningful results.

    Example:
    Assuming a `question` object with a `question_options` attribute of 5, this function
    will return a random integer between 1 and 5.

question = Question(5)  # Assuming Question is a class with question_options attribute.
    >>> AnalyzeUserInput("Some input", issue)
   3  # Example output, actual output will vary due to randomness.
    """

    # We check according to the issue
    path = "api/NLP/Models/BERT_mini_whole.pth"
    model_path = os.path.abspath(path)
    print("path", model_path)
    model_type = "BERT_mini"
    # if issue == 1:  # Issue 0 : ADHD
    #     # We use a specfic model for now it'll be BERT
    #     model_path = "path/to/model"
    #     model_type = "BERT"
    #
    # elif issue == 2:  # Issue 1 : Anxiety
    #     # We use a specfic model for now it'll be BERT
    #     model_path = "path/to/model"
    #     model_type = "BERT"
    # elif issue == 3:  # Issue 1 : depression
    #     # We use a specfic model for now it'll be BERT
    #     model_path = "path/to/model"
    #     model_type = "BERT"

    predictions = run_model(user_input, model_path, model_type)

    # # We return a the np array
    return predictions
    #return 1;
