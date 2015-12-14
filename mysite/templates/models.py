from django.db import models


class Result(models.Model) :
	json = models.CharField() 
	pub_date= models.DateTimeField('date')

 	def __unicode__(self):
        return self.name