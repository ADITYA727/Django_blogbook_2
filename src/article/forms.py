from django import forms
from .models import Article, Repository

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]



class GithubForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ["repo_name","repo_url","repo_dec"]        