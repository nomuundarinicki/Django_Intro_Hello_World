from django.conf.urls import url
#from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
]

""" Then open VIEWS
def index(request):
    return render(request,'helloworld_app/index.html')

create template with HTML
go to helloworld_app
make new file
apps/helloworld_app/templates/index.html

"""
