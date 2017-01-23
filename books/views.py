from .models import Book
from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import BookForm

def BookCreate(request):
        form = BookForm(request.POST or None)
        print request.user
        if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
        context = {
              "form": form,
        }
        return render(request, "addbook.html", context)
def BookAll(request):
        books = Book.objects.all().order_by('name')
        context = {'books':books}
        return render_to_response('booksall.html', context, context_instance=RequestContext(request))
