# Create a virtual environment

```md
python -m venv ./fakeurlgenerator
```

# Activate the virtual environment

```md
cd fakeurlgenerator/scripts
activate
```

# Installing Django and creating the django project

```md
pip install django
django-admin startproject fakeurlgenerator
cd fakeurlgenerator
```

# Create an app for maintaining urls

```md
django-admin startapp app
```

# Update Settings.py

1. Environments

```md
import os
from dotenv import load_dotenv
load_dotenv()
```

2. Installed Apps

```md
'app',
```

3. Middlewares

```md
'whitenoise.middleware.WhiteNoiseMiddleware',
```

4. STATICFILES STORAGE (for production)

```md
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

5. Templates

* For connecting the HTML, Javascript

```md
'DIRS': [os.path.join(BASE_DIR,'templates')],
```

6. Static Files

* For Connecting the css

```md
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'statifiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```

7. Set Allowed Hosts and Debug For Production

# Installation

```md
pip install python-dotenv whitenoise gunicorn
```

# Start the Server

```md
python manage.py runserver
```
