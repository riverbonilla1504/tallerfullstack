from pathlib import Path

# BASE_DIR: Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Mantén esta clave en secreto en producción
SECRET_KEY = "django-insecure-10795e*c7u&*w-^a#)=x=&jl#%f)t8tnf*b7v_tf6zw-^rpraw"

# DEBUG: Activa/desactiva modo de desarrollo
DEBUG = True  # ⚠️ Cambiar a False en producción

# ALLOWED_HOSTS: Define qué dominios pueden acceder al servidor
ALLOWED_HOSTS = ['*']  # ⚠️ En producción, cambia esto por dominios específicos

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "AppVehiculos",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Permitir solicitudes externas
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "GestionVehiculos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "GestionVehiculos.wsgi.application"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangotests',
        'USER': 'djangotests_user',
        'PASSWORD': 'vsEr3czSoV5nWB0D5p1naY6EbuXAAJBs',
        'HOST': 'dpg-cvs9n5muk2gs739prahg-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "es"  # Cambiado a español
TIME_ZONE = "America/Bogota"  # Ajusta tu zona horaria
USE_I18N = True
USE_TZ = True

# 📌 Configuración de archivos estáticos
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # Asegura que se sirvan archivos estáticos

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 📌 Configuración de Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # Cambia a IsAuthenticated en producción
    ],
}

# 📌 Configuración de CORS para permitir solicitudes desde cualquier origen
CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ En producción, restringe esto
CORS_ALLOW_CREDENTIALS = True
