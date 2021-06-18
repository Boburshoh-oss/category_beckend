from django.shortcuts import get_object_or_404, render
from .models import Blog,Catigory
from django.views.generic import DetailView, ListView
from django.core.paginator import PageNotAnInteger, Paginator,EmptyPage
from django.db.models import Q
# Create your views here.

def category(request,id):
    category = get_object_or_404(Catigory, pk=id)
    blogs = Blog.objects.filter( categories=category )
    categories = Catigory.objects.all()

 
    return render(request,"index.html", {
        "Blog":blogs,
        "categories":categories
    })

def detail_view(request,id):
    blog_id = get_object_or_404(Blog, pk=id)
    categories = Catigory.objects.all()
    return render(request,'detail.html',{"Blog":blog_id,"categories":categories})
    
def search_view(request):
    query=request.GET.get('query')
    category = Catigory.objects.all()
    
    Blogs= Blog.objects.filter( Q(title__icontains=query) | Q(description__icontains=query) )
    return render(request, "index.html", {
        "Blog":Blogs,
        "categories":category
    })

def index(request):
    blog=Blog.objects.all()
    categories=Catigory.objects.all()
    return render(request,'index.html',{'Blog':blog,'categories':categories})