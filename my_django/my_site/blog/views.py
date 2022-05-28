from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):

    articles=Article.objects.all()

    print(articles)
    
    return render(request,"blog/index.html" ,{'articles':articles})


def detail(request,pk):

    articles=Article.objects.get(pk=pk)

    print(articles)
    #article=get_object_or_404(article,pk=pk)
    context={'article':articles}

    return render(request,"blog/detail.html" ,context)
