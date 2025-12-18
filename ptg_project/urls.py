"""ptg_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home_view
from games.views import games_view
from community.views import community_view
from statute.views import statute_view
from faq.views import faq_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name= 'home'),
    path('home/', home_view, name = 'home'),
    path('games/', games_view, name = 'games'),
    path('community/', community_view, name = 'community'),
    path('statute/', statute_view, name = 'statute'),
    path('faq/', faq_view, name = 'faq'),
]
