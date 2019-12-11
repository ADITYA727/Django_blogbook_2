from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm, GithubForm
from .models import Article, Comment, Like, Repository
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
from django.contrib.auth.models import User

# Create your views here.



def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    response.set_cookie('java-kjk', 'fdbjhks SHUKLA')  
    return response  


def getcookie(request):  
    tutorial  = request.COOKIES 
    print(tutorial['csrftoken'])
    return HttpResponse("java tutorials @: ",tutorial['csrftoken']);




def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"blogs.html",{"articles":articles})


@login_required(login_url = "user:login")
def payment(request):
    return render(request,'payment.html'); 



@login_required(login_url = "user:login")
def chat_with_friend(request):
    return render(request,'chat_with_friend.html');   


@login_required(login_url = "user:login")
def gallary(request):
    return render(request,'gallary.html');         



def index(request): 
    repo_list = Repository.objects.all()
    # keyword = request.GET.get("keyword")
    # if keyword:
    #     articles = Article.objects.filter(title__contains = keyword)
    #     return render(request,"articles.html",{"articles":articles})
    # articles = Article.objects.all()
    # get_likes = Like.objects.all().count()
    return render(request,"index.html",{"repo_list":repo_list})


def like(request):
    if request.method == 'GET':
        post_id = request.GET['like_id']
        print(post_id)
        user = Article.objects.get(id=post_id)
        likedpost = Article.objects.get(id=post_id)
        print(likedpost)
        m = Like( likes = likedpost )
        m.save()
        get_likes = Like.objects.all()
        data = serializers.serialize('json', list(get_likes))
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse("unsuccesful")    


    
    
def about(request):
    return render(request,"about.html")

@login_required(login_url = "user:login")
def find_people(request):
    users = User.objects.all()
    return render(request,"find_people.html",{"users_list":users})    


@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {"articles":articles}
    return render(request,"blog_settings.html",context)



@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article successfully created")
        return redirect("article:articles")
    return render(request,"addarticle.html",{"form":form})


def detail(request,id): 
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url = "user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Article successfully updated")
        return redirect("article:dashboard")


    return render(request,"update.html",{"form":form})


@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Article Successfully Deleted")
    return redirect("article:dashboard")


def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))



@login_required(login_url = "user:login")   
def repo(request):
    if request.method == "POST":
        repo_name = request.POST.get("repo_name")
        repo_url = request.POST.get("repo_url")
        repo_dec = request.POST.get("repo_dec")
        repo_url = repo_url.strip()
        repo = Repository(repo_name = repo_name, repo_url =repo_url , repo_dec = repo_dec)
        repo.save()
        return redirect('/')

    
    return render(request,'git_hub.html')

   




  



    