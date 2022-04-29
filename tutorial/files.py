import uuid
import os

from PIL import Image
from io import BytesIO
from django.core.files import File

def image_upload(instance, file_name):
    ext = file_name.split('.')[-1]
    file_name = uuid.uuid4().hex
    return 'full/%s/%s.%s' % (file_name[:2], file_name, ext)

def thumb_upload(instance, file_name):
    ext = file_name.split('.')[-1]
    file_name = uuid.uuid4().hex
    return 'thumbnail/%s/%s.%s' % (file_name[:2], file_name, ext)

def create_thumbnail(file):
    name, ext  = os.path.splitext(file.name)
    image = Image.open(file)
    image.thumbnail((128, 128))
    thumb_io = BytesIO()
    image.save(thumb_io, "WEBP")
    return File(thumb_io, name+".webp")
