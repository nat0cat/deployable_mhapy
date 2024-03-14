# Project Overview and Decisions
Our subteam was tasked with handling the **NLP** aspect of the chatbot. 
Our subteam was therefore tasked with analysing the data and generating accurate predictions.


## Decisions
When looking for a model we look for the most efficient model which could represent our situation. We looked on huggingface in order to find a model.
BERT  is efficient in predicting scores for our application thanks to its deep understanding of language context and nuances Its pre-trained nature on a vast corpus of text also accelerates and enhances its prediction capabilities for specific tasks with fine-tuning.
We wanted to implement an analysis accross multiple various models but due to our time constraint, we aimed to implement a working analysis with the BERT model. We used BERT as it works extremly well and it is able to refine itself greatly.
We looked for datasets on hugging face as well as kaggle in order for us to fine-tune our model.
We then had to organise our files, we divided our work into 3 files: run_model.py, get_model.py, training.ipynb and tempCodeTunnerFile. 



## Work seperation
When dividing work we first looked for models on our own. After previous discusions with mhappy it was agreed upon for them to give us a gpt key in order for us to train GPT models and therefore obtain much more efficient and powerful analysis. But due to their lack of response which led to us parting ways. We had to look for a new model. Ben suggested using a BERT model.

-Ben Liu: I did research on the model to use as well as on general NLP paradigms, and I also did research and looked on hugging face and Kaggle for a suitable dataset. I also implemented the model and BERT fine-tuning. And helped debugging.

- Najim Rhalmi: I did research on the models for the NLP paradigms, and looked for datasets which could be used on hugging face. I implemented the loading and running of the models to generate the predictions. I also wrote the Read.me for our subteam as well as the sub-team report, and helped on the main report.





