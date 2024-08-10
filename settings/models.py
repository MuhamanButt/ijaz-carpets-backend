from django.db import models
from .mongodb import db

settings_collection = db['settings']