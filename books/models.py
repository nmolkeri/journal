from django.db import models


class Book(models.Model):
        name            = models.CharField(max_length=200)
        author         = models.CharField(max_length=200)
        year          = models.CharField(max_length=10)
        read_date = models.DateField()
        category = models.CharField(max_length=200)
        comment     = models.TextField(blank=True)
	

	def __unicode__(self):
        	        return self.name
