# Google Search Data Viewer  
  
  
## Technologies  
  
  
Backend: Python / Django  
Frontend: **Boring** Bootstrap5 
  
  
  
 ## Get Started


### Prerequisites

Python 3.10.2 was used for development  


### Installing  

Clone the repository to your local machine:  


``` 
git clone https://github.com/liamstevens111/google-search-data-viewer.git 
```


cd into the directory and create a virtual environment to install dependcies and run the application (**recommended**)  

```
cd google-search-data-viewer  
python -m venv .venv  
```

Activate the virtual environment.  

On Windows:  

```
cd ./.venv/scripts/ && activate.bat  
```

or use your favourite code editor, ie VS Code to automatically activate it for you.  


Install depenencies from the base directory:  

```  
pip install -r requirements.txt  
```


### Usage

Rename **.env.example** in the root directory to **.env** and declare your environment variables for your secret key, database etc. For example:

```
DEBUG=True
SECRET_KEY = 'fe££@f2Ldffe&gOK-cln@89-gte_=slpeefe87!5nza%(0q6^rggrgrgfn^)r6p+rzctp'

DB_NAME=googlesearch
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=127.0.0.1
```

If using Postgres and not sqlite as above, first ensure you have created the corresponding databasebase and credentials listed above prior to running the following migrations.


Create migrations:
```
python manage.py migrate
```


Create a superuser to login to the admin  

**(Note: currently this will not create an associated Profile for the User, so you will have to manually create one or use the regular Signup method)**:

```
python manage.py createsuperuser 
```
  
  
  

Run the development server:  
  
  

```
python manage.py runserver
```
  
  
Go to http://127.0.0.1:8000/
