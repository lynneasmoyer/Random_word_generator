from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^random_word$', views.generator),
    url(r'^reset$', views.reset),
]