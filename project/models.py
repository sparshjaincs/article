from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 1000,blank = True,unique = True)
    def __str__(self):
        return self.name
class Project(models.Model):
    title = models.CharField(max_length = 1000,blank = True,unique = True)
    language =  models.ForeignKey(Category, related_name='languagecategory', to_field='name', on_delete=models.CASCADE)
    tags = models.CharField(max_length = 1000,blank = True)
    description = models.TextField(blank = True)
    link = models.TextField(blank = True)

    def __str__(self):
        return self.title