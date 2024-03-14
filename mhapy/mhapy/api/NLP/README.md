# Welcome to Rubber Frog Studios' mhapy Project Subteam3

## Partner Intro
 * Include the names, emails, titles, primary or secondary point of contact at the partner organization
 * Provide a short description about the partner organization. (2-4 lines)

## Description about the project
Our subteam project is to the Integration of a BERT NLP model which we train using a dataset found on kaggle. We then analyse user inputs and generate a score accordingly.
​
## Key Features
- **Custom BERT Model Training:** Utilizing a pretrained BERT Model from Hugging Face to facilitate data training.
- **Effortless Model Loading and Prediction:** Efficient loading of trained models for new data predictions.
- **Insightful Analysis:** ML-driven results provide deep insights into patient issues, aiding diagnosis and treatment planning.
​
## Instructions
The user will inputs a string in the command line and our program return a score according to the given prompt.
 
 ## Development requirements
1. **Prerequisites:** Python 3.10 is required.
3. **Install Dependencies:** Execute `pip install ...` Pytorch, Pandas, sklearn, Numpy, transformers to install necessary Python packages. 

#### Deploying the Model
- **Loading the Model:** `get_model.py` efficiently loads your trained BERT model.(Implemented such that it can load different models but only BERT will be used for D2)
- **Running Predictions:** `run_model.py` allows for input of new patient data and provides mental health predictions, offering valuable insights for healthcare professionals. While in \deliverable-1-16-mhapy\deliverables\D2\NLP, run the file run_model.py. Once in the python command line, run the following:
python -c "import run_model; run_model.deploy_model('<YOUR MESSAGE HERE>')"


#### Training Your Model
- Utilize the `training.ipynb` Jupyter notebook for a the code pertaining to BERT model training with patient data, including data preprocessing, model setup, and training.

 


