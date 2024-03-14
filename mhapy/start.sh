python3 -m venv venv

source venv/bin/activate

pip install django
pip install djangorestframework
pip install psycopg2-binary    #mac 
pip install psycopg2           #not mac 
pip install drf-yasg         # swagger 

python3 manage.py makemigrations   
python3 manage.py migrate   
python3 initial_data.py

# python3 manage.py loaddata initial_data.json  

# for  nlp 
pip install torch pandas scikit-learn numpy transformers 

python3 manage.py runserver  