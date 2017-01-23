from music.models import Album
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import AlbumForm, MusicianForm

def MusicianCreate(request):
        form = MusicianForm(request.POST or None)
        print request.user
        if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
        context = {
              "form": form,
        }
        return render(request, "addmusician.html", context)


def AlbumCreate(request):
	form = AlbumForm(request.POST or None)
        print request.user
        if form.is_valid():
                instance = form.save(commit=False)
		instance.save()
	context = {
              "form": form,
        }
        return render(request, "addalbum.html", context)	
def AlbumAll(request):
        music = Album.objects.all().order_by('name')
        context = {'music':music}
        return render_to_response('musicall.html', context, context_instance=RequestContext(request))
