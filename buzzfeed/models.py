from django.db import models

# Create your models here.

#This is the model of the buzzfeedcomments, which shoud have the  
#the user associated wkith tehu sercreated, the json,and the datewa creatd. 



class BuzzfeedSearch(models.Model):
	created  = models.DateTimeField(auto_now_add=True) 
	json = models.CharField(max_length= 10000)
	user =models.CharField(max_length = 1000) 

