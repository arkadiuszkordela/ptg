from django.shortcuts import render

# Create your views here.

def statute_view(request, *args, **kwargs):
    return render(request, 'statute.html', {})