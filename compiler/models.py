from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Language(models.Model):
    lang = models.CharField(max_length=1000,unique = True)
    template = models.TextField(blank = True)
    def __str__(self):
        return self.lang

class PlayGround(models.Model):
    user = models.ForeignKey(User, related_name='playground_user', to_field='username', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000,blank = False,default="Untitled")
    def __str__(self):
        return self.title + str(self.user)

class ExtendPlay(models.Model):
    instance = models.ForeignKey(PlayGround, related_name='playground_ins', on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, related_name='playground_lang', to_field='lang', on_delete=models.CASCADE)
    code = models.TextField(blank = True,null = True)




