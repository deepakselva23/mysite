from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post,Comment
from django.utils import timezone
# from blog.form import PostForm,CommentForm

from django.views.generic import (TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView)

# Create your views here.

# def PostView(ListView):
#     model = Post

#     def get_queryset(self):
#         Post.objects.filter()
