from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Mois(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='img')
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre

class Module(models.Model):
    mois = models.ForeignKey(Mois, on_delete = models.CASCADE, related_name='mois_module')
    language = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')
    description=models.TextField()
    prix = models.IntegerField()
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.language
    
class Chapitre(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE, related_name='module_chapitre')
    titre = models.CharField(max_length=255)
    description=models.TextField()
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
class Cours(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete = models.CASCADE, related_name='chapitre_cours')
    titre = models.CharField(max_length=255)
    video = models.FileField()
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
    
class Usercourse(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE, related_name='module_usercourse')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_usercourse')
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username