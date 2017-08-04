from django.conf.urls import url
from collator.core import views

urlpatterns = [
    url('^$', views.home_page, name='home'),
]
