from django.shortcuts import render
from homepage.models import Index

# Create your views here.
def homepage_index(request):
    my_self = Index.objects.all()
    context = {
        'my_self': my_self
    }
    return render(request, 'homepage/homepage_index.html', context)