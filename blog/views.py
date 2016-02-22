from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# Create views (pages) here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    # http://127.0.0.1:8000/post/pk/ will retrun the full text of a post

def post_new(request):
	#Once a post is submitted, will be displayed in the form
	#If method is POST - if there is information saved in the form
	if request.method == "POST":
		form = PostForm(request.POST)
		#Are all the required fields set?
		if form.is_valid():
			#Don't want to save straight away, want to add an author first
			post = form.save(commit=False)
			#add an author, as we didn't in PostForm
			post.author = request.user
			post.published_date = timezone.now()
			#save the form
			post.save()
			#When saved, will be redirected to the detail page for post
			return redirect('post_detail', pk=post.pk)
	else:
		#Blank form, for when we access the page for the first time
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
    # To create a new Post form, call PostForm() and pass it to the template

def post_edit(request, pk):
	#Extract the post model we want to edit
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
    	# Populate fields with the post needing editing
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    # Using the same template as the create a new post page