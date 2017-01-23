from places.models import Place
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import PlaceForm

def PlaceCreate(request):
        form = PlaceForm(request.POST or None)
        print request.user
        if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
        context = {
              "form": form,
        }
        return render(request, "addplace.html", context)


def PlaceAll(request):
        places = Place.objects.all().order_by('name')
        context = {'places':places}
        return render_to_response('placeall.html', context, context_instance=RequestContext(request))
