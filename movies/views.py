from django.shortcuts import render, render_to_response
from django.template import RequestContext
from movies.models import Movie
from django.contrib.auth.decorators import login_required

from .forms import MoviesForm
from .forms import CategoryForm
def CategoryCreate(request):
        form = CategoryForm(request.POST or None)
        print request.user
        if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
        context = {
              "form": form,
        }
        return render(request, "addcategory.html", context)

def MovieCreate(request):
	form = MoviesForm(request.POST or None)
	print request.user
	if form.is_valid():
                instance = form.save(commit=False)
		instance.save()
	context = { 
	      "form": form,
	}
	return render(request, "addmovie.html", context)

def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "addmovie.html", context)



@login_required
def MoviesAll(request):
	if not request.user.is_authenticated():
                return HrttpResponseRedirect('/login/')
	movies = Movie.objects.all().order_by('name')
	context = {'movies':movies}
	return render_to_response('moviesall.html', context, context_instance=RequestContext(request))
		
def SpecificMovie(request, moviename):
	movie1 = Movie.objects.get(name=moviename)
	context = {'movie1':movie1}
	return render_to_response('singlemovie.html', context, context_instance=RequestContext(request))


def index(request):
	form = MoviesForm()
        return render_to_response('index.html', context_instance=RequestContext(request))
