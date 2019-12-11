from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('comment/<int:id>',views.addComment,name = "comment"),
    path('git_hub/',views.repo, name='git_hub'), 
    path('find_people/',views.find_people, name='find_people'),
    path('payment/',views.payment, name='payment'),
    path('chat_with_friend/',views.chat_with_friend, name='chat_with_friend'),
    path('gallary/',views.gallary, name='gallary') 
 
    
]
