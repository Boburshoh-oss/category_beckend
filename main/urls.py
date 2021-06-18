from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category/<int:id>',views.category,name="category"),
    path('Blog/<int:id>',views.detail_view,name='detail'),
    path('search',views.search_view,name='search_view')
]
