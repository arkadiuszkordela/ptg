from django.shortcuts import render

# Create your views here.

def games_view(request, *args, **kwargs):
    return render(request, 'games.html', {})