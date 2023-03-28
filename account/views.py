from django.shortcuts import render

# Create your views here.

def account_view(request, *args, **kwargs):
    return render(request, 'account.html', {})