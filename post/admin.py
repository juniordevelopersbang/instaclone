from django.contrib import admin
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields ='__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'nickname', 'content', 'created_at']
    lsit_display_links = ['author', 'nickname', 'content']
    form = PostForm
    
    def nickname(request, post):
        return post.author.profile.nickname