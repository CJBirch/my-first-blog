from django.db import models
from django.utils import timezone


# Creating models
class Post(models.Model):
	author = models.ForeignKey('auth.User') #Link to another model
	title = models.CharField(max_length=200) #CharField - limit no. characters
	text = models.TextField()    #TextField - text unlimited
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	#Function: publish (within Post)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):  #Return a string to Post title
		return self.title
