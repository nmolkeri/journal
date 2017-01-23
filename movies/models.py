from django.db import models
class Movie(models.Model):
	RATING_STARS = (
        	('1', 'Not good'),
              	('2', 'Below average'),
        	('3', 'Average'),
        	('4', 'Above average'),
        	('5', 'Good'),
    	) 
       	#model = models.Forignkey
	name            = models.CharField(max_length=200)
        category        = models.ForeignKey('Category')
        year            = models.CharField(max_length=4)
        comment         = models.TextField(blank=True)
	rating 		= models.CharField(max_length=1, default='1', choices=RATING_STARS)
	image1          = models.ImageField(upload_to="movies/images/icons/", blank=True)
        def __unicode__(self):
                return self.name

class Category(models.Model):
        name            = models.CharField(max_length=200)
        description     = models.TextField(blank=True)

        def __unicode__(self):
                return self.name
