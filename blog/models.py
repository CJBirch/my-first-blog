from django.db import models
from django.utils import timezone


# Creating models
class Post(models.Model):
	author = models.ForeignKey('auth.User') #Link to another model
	title = models.CharField(max_length=200) #CharField - limit no. characters
	text = models.TextField()    #TextField - text unlimited
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	#Function: post.publish, to publish a draft post - when publish 
	#button is clicked, creates a publication date of now.
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	#Moderate the comments
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

	def __str__(self):  #Return a string to Post title
		return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text