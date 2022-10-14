from django.db import models
from pathlib import Path

# Create your models here.

def upload_image_to(instance, filename):
    return Path("static")/"images"/filename
