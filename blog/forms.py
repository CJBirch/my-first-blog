
from django import forms
from .models import Post, Comment

#PostForm is the name of the form
class PostForm(forms.ModelForm):
	#Where we tell Django which model to base the form on
	class Meta:
		#Form follows the format defined in Post
		model = Post
		#Which fields from Post should appear and are required
		#If they aren't filled, page will prompt for them
		fields = ('title', 'text',)
		#Author and date_created are set automatically in Post model

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'text',)