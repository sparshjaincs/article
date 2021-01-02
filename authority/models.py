from django.db import models
from coding.models import *
import datetime
# Create your models here.
class Mock(models.Model):
    LOCK = (
        ('True','True'),('False','False')
    )
    title = models.CharField(max_length = 1000,unique = True,blank = False)
    company = models.ForeignKey(Company, related_name='companies_names', to_field='company_name', on_delete=models.CASCADE)
    pattern = models.ManyToManyField(Categories,blank=True,related_name="categories_name")
    lock = models.CharField(max_length=1000,choices=LOCK,default="True")
    subscribers = models.ManyToManyField(User,default=None,blank=True,related_name="subscribers_name")
    def __str__(self):
        return self.title

class Test_Series(models.Model):
    instance =  models.ForeignKey(Mock, related_name='mock_name', to_field='title', on_delete=models.CASCADE)
    title = models.CharField(max_length = 1000,unique = True,blank = False)
    questions = models.ManyToManyField(Aptitude,blank=True,related_name="question_series")
    #duration = models.IntegerField()
    time_duration = models.IntegerField(default=90)
    subscribers = models.ManyToManyField(User,default=None,blank=True,related_name="subscribers_series")
    def __str__(self):
        return self.title

class Test_Given(models.Model):
    users =  models.ForeignKey(User, related_name='my_user', to_field='username', on_delete=models.CASCADE)
    given =  models.ForeignKey(Test_Series, related_name='given_test', to_field='title', on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)
    solution = models.CharField(max_length=5000,default="{}")
    def __str__(self):
        return self.users.username
