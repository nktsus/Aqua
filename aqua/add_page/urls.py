from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.request_page, name='request_page'),
]