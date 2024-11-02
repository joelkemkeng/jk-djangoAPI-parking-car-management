# Sur votre Ordinateur Windows

#--- Telecharger Python Version 3.12.5
Lien: https://www.python.org/downloads/release/python-3125/

# Cree l'environnement Python Nommee (.venv)
python -m venv .venv

# Activez l'environnement (.venv)
.venv\Scripts\Activate.ps1

# installer les dependance 
pip install -r requirements.txt




#instruction 

# install Server Postgress
        +++++++ install version postgresql-16 
        https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

        +++++++ install version  pgadmin4-8.11
        https://www.pgadmin.org/download/pgadmin-4-windows/


# Open pgAdmin 
# Open Server Postgress install
# Create One dataBase and configure 
        DATABASES = {
            'default': {
                'NAME': 'mytestdb',
                'USER': 'postgres',
                'PASSWORD': 'root',
                'HOST': 'localhost',
                'PORT': '5433',
            }
        }

# open Command Terminal in this folder project 

# Activate environnement -> 
.venv\Scripts\Activate.ps1

# Test Server -> 
python manage.py runserver 

# if good close server with (ctrl + c)

# Migrate Data Base Postgress Project 
python manage.py makemigrations

# Migrate DataBase 
python manage.py migrate 


# run Server
python manage.py runserver 


Voici une version améliorée et mieux structurée de votre documentation pour une meilleure lisibilité et compréhension :

---

Avec cette version, les instructions sont plus claires et bien organisées pour permettre une configuration facile du projet sur un environnement Windows.