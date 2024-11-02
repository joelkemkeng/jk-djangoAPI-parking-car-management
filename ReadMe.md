
# Guide de Configuration du Projet sur Windows

**Auteur** :  
- **Nom** : KEMKENG NGOUZA 
- **Prénom** : KEDI JOEL
- **nom court** : Joel Kemkeng  
- **Nom de l'entreprise** : HasDigit @HasDigit 
- **Initiales** : @HasDigit 
- **Adresse mail** : kedikemkeng@gmail.com 
- **Adresse mail** : kedikemkenh@hasdigit.com 
- **Téléphone** : +33 7 51 54 27 74



## 1. **Installation de Python**

### Télécharger Python 3.12.5
- [Téléchargez Python 3.12.5](https://www.python.org/downloads/release/python-3125/)
- Lors de l'installation, assurez-vous de cocher l'option **"Ajouter Python au PATH"**.

### Créer et Activer un Environnement Virtuel
1. **Créer l'environnement virtuel** dans le répertoire du projet :
    ```bash
    python -m venv .venv
    ```

2. **Activer l'environnement virtuel** :
    ```bash
    .venv\Scripts\Activate.ps1
    ```

3. **Installer les dépendances** à partir du fichier `requirements.txt` :
    ```bash
    pip install -r requirements.txt
    ```

---

## 2. **Installation et Configuration de PostgreSQL et pgAdmin**

### Installer PostgreSQL 16
- Téléchargez et installez PostgreSQL 16 depuis [ce lien](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

### Installer pgAdmin 4 (Version 8.11)
- Téléchargez et installez pgAdmin 4 version 8.11 depuis [ce lien](https://www.pgadmin.org/download/pgadmin-4-windows/).

---

## 3. **Configuration de PostgreSQL**

### Ouvrir pgAdmin et Configurer un Serveur
1. Lancez **pgAdmin**.
2. Ouvrez votre serveur PostgreSQL (précédemment installé).
3. **Créer une nouvelle base de données** :
   - Nom de la base de données : `mytestdb`.

### Configuration de la Base de Données dans le Projet
Dans le fichier `settings.py` de votre projet Django, configurez la base de données comme suit :
```python
DATABASES = {
    'default': {
        'NAME': 'mytestdb',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
```

---

## 4. **Commandes à Exécuter**

### 4.1. Activation de l'Environnement Virtuel
Ouvrez un terminal à partir du répertoire racine de votre projet et activez l'environnement virtuel :
```bash
.venv\Scripts\Activate.ps1
```

### 4.2. Tester le Serveur Django
Pour tester que le serveur fonctionne correctement :
```bash
python manage.py runserver
```
- Si le serveur fonctionne correctement, vous pouvez le fermer avec la combinaison **Ctrl + C**.

### 4.3. Migration de la Base de Données

1. **Créer les migrations** pour la base de données :
    ```bash
    python manage.py makemigrations
    ```

2. **Appliquer les migrations** à PostgreSQL :
    ```bash
    python manage.py migrate
    ```

---

## 5. **Lancer le Serveur**

Une fois les migrations effectuées, lancez à nouveau le serveur :
```bash
python manage.py runserver
```

---

## 6. **Résumé des Commandes Utiles**

- **Créer l'environnement virtuel** :
    ```bash
    python -m venv .venv
    ```

- **Activer l'environnement virtuel** :
    ```bash
    .venv\Scripts\Activate.ps1
    ```

- **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

- **Tester le serveur** :
    ```bash
    python manage.py runserver
    ```

- **Créer les migrations** :
    ```bash
    python manage.py makemigrations
    ```

- **Appliquer les migrations** :
    ```bash
    python manage.py migrate
    ```

- **Lancer le serveur** :
    ```bash
    python manage.py runserver
    ```

---
