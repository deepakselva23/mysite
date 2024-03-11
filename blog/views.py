from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from blog.models import Post,Comment
from django.utils import timezone
from .form import PostForm, CommentForm
# from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


from django.views.generic import (TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView)

# Create your views here.

class PostView(ListView):
    model = Post
    template_name="post_list.html"
    def get_queryset(self):
        records = Post.objects.filter(publish_date__lte=timezone.now())
        print("records ",records)

        return records
        

class CreatePostView(CreateView):

    template_name="create_post.html"
    form_class = PostForm
    model = Post

    def get_success_url(self):
        post_id = self.object.id
        print("post_id ",post_id)
        return f'/post/{post_id}/'

def postpublish(request, pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish_post()
    return redirect('post_detail', pk)


class PostUpdateView(UpdateView):
    template_name="create_post.html"
    form_class = PostForm
    model = Post
    # success_url = reverse_lazy('post_detail')
    # redirect_field_name = 'post_detail'
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostRemoveView(DeleteView):
    model = Post
    template_name="delete_post.html"
    success_url = reverse_lazy('post_list')


class PostdetailView(DetailView):
    model = Post

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post'] = self.object  # Add 'post' to context with the value of the object
    #     return context

# class AddComment(CreateView):
#     form_class = CommentForm
#     template_name = 'create_comment.html'
#     model =Comment

#     def get_success_url(self) -> str:
#         post_id= self.object.id
#         return f'/post/{post_id}/'
    
def AddComment(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        print("this is pos ")
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm
        return render(request, 'create_comment.html', {"form": form})
    

def Commentapprove(request, pk):
    cmt = get_object_or_404(Comment,pk=pk)
    cmt.approve()
    return redirect('post_detail', cmt.post.pk)

    
def Commentremove(request, pk):
    cmt = get_object_or_404(Comment,pk=pk)
    post_id = cmt.post.pk
    # cmt.deleted_date = timezone.now()
    cmt.delete()
    return redirect('post_detail', post_id)

# class Commentremove(DeleteView):
#     model = Comment
#     template_name="delete_post.html"
#     success_url = reverse_lazy('post_list')