from django.shortcuts import render

# Create your views here.

def community_view(request, *args, **kwargs):
    return render(request, 'community.html', {})