from django.db import models

PLACE_CHOICES = (
        ('Domestic', 'Domestic'),
        ('International', 'International'),
)

VISIT_CHOICE = (
	('Business', 'Business'),
	('Pleasure', 'Pleasure'),
)

class Place(models.Model):
        name            = models.CharField(max_length=200)
        country         = models.CharField(max_length=200)
	reason		= models.CharField(max_length=10, choices=VISIT_CHOICE) 
        international_domestic        = models.CharField(max_length=15, choices=PLACE_CHOICES)
	visit_date = models.DateField()
	attraction = models.CharField(max_length=200)
        description     = models.TextField(blank=True)
	
        def __unicode__(self):
                return self.name
