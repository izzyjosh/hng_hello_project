from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "djangecb3ceb36ead0450db47bfef46586a9cd77c02befd566d6af317493a6693a83bb583989fdd118c7657257c4a29f4b1fcadc8"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1']



# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "main.apps.MainConfig",
    "rest_framework"
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"



WSGI_APPLICATION = "core.wsgi.application"




# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


#ipinfo API key
IPINFO_API_TOKEN = "c5d3ea64ad4c30"

#openwhethermap api key
OPENWHETHER_API = "fc4b24a0bfb27829b9d480e3f8dc0c30"
