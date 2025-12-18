from django.shortcuts import render

# Create your views here.

def faq_view(request, *args, **kwargs):
    return render(request, 'faq.html', {})