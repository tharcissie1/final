from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, RedirectView
from django.utils.decorators import method_decorator
from .models import Article, Comment, College
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.forms import ModelForm
from django.utils import timezone
from .forms import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from rootFolder.settings import EMAIL_HOST_USER
from django.db.models import Q







#####################     dealing with search features       ######################
class SearchResult(ListView):
    model = Article
    template_name = 'core/search_results.html'

    def get_queryset(self):
        search = self.request.GET.get('query')
       
        object_list = Article.objects.filter(

            Q(subject__icontains=search) | Q(message__icontains=search)
        )
        return object_list


def cst(request):
    articles_cst = Article.objects.filter(college__name='CST').order_by('-id')
    return render(request,'core/college_articles.html',{'articles_cst':articles_cst})

def cbe(request):
    articles_cbe = Article.objects.filter(college__name='CBE').order_by('-id')
    return render(request,'core/college_articles.html',{'articles_cbe':articles_cbe})

def cmhs(request):
    articles_cmhs = Article.objects.filter(college__name='CMHS').order_by('-id')
    return render(request,'core/college_articles.html',{'articles_cmhs':articles_cmhs})

def ce(request):
    articles_ce = Article.objects.filter(college__name='CE').order_by('-id')
    return render(request,'core/college_articles.html',{'articles_ce':articles_ce})

def cass(request):
    articles_cass = Article.objects.filter(college__name='CASS').order_by('-id')
    return render(request,'core/college_articles.html',{'articles_cass':articles_cass})

def cavm(request):
    articles_cavm = Article.objects.filter(college__name='CAVM').order_by('-id')
    return render(request,'core/college_articles.html',{'articles_cavm':articles_cavm})


################################## section of like view  ##################################
class ArticleLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        print(pk)
        obj = get_object_or_404(Article, pk=pk)
        url_= obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return  url_


##############################################  section of dislike view  ###############################
class ArticleDislikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        print(pk)
        ob = get_object_or_404(Article, pk=pk)
        urll_= ob.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in ob.dislikes.all():
                ob.dislikes.remove(user)
            else:
                ob.dislikes.add(user)
        return urll_











################ function for finding subscribers and  create bew article    ################
def subscriber():
    subscribers_list = []

    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        subscribers_list.append(subscriber.email)

    return subscribers_list




def new_article(request):
    subject = "Hello Subscriber"
    message = 'A new article from your choice has been created, be the first to read it and share your feedback'
    send_mail(subject, message, EMAIL_HOST_USER,subscriber())

    template_name = 'core/new.html'
    return render (request, template_name)
