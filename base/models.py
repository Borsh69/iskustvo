from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".gltf", ".glb"]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Comment(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True, blank=True)

class Artwork(models.Model):
    face = models.ImageField(upload_to="images/", verbose_name="Лицевое изображение",)
    name = models.CharField(max_length=40,)
    description = models.TextField(max_length=500,)
    uncompressed_img = models.ImageField(upload_to="images/", verbose_name="Оригинальное изображение", blank=True,)
    object3d = models.FileField(upload_to="files/", verbose_name="3D файл", blank=True, validators=[validate_file_extension])
    comments = models.ManyToManyField(Comment, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name
    


class User(models.Model):
    name = models.CharField(max_length=60,)
    avatar = models.ImageField(upload_to="images/",)
    tag = models.CharField(max_length=20, unique=True,)
    login = models.CharField(max_length=20, unique=True,)
    password = models.CharField(max_length=20)
    artworks = models.ManyToManyField(Artwork, blank=True, related_name="users")

    def __str__(self):
        return self.name
    




@receiver(pre_save, sender=Artwork)
def resize(sender,instance, **kwargs):
    if(instance.face):
        face = PILImage.open(instance.face)
        width,height = face.size
        new_width,new_height = 800, 600
        left = (width-new_width)/2
        right = (width+new_width)/2
        top = (height-new_height)/2
        bottom = (height+new_height)/2
        face = face.crop((left,top,right,bottom))
        thumb_io = BytesIO()
        face.save(thumb_io, format='PNG')
        instance.face.save(instance.face.name, InMemoryUploadedFile(thumb_io, None, f'{instance.face.name}', 'face', thumb_io.tell(), None), save=False)