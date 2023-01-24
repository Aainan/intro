from django.urls import path

from .views import index_view

app_name = 'table'
urlpatterns = [
    path('', index_view, name='index')
]
