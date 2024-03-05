from django import forms
from blog.models import Post,Comment

# class PostForm(forms.ModelForm):
    
#     class Meta():
#         model = Post
#         field = ('author','title','text')

#         widgets={
#             'title':forms.TextInput(attrs={'class':'textinputclass'}),
#             'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
#         } 

# class CommentForm(forms.ModelForm):
    
#     class Meta():
#         model = Comment
#         field = ('author','comment_msg')

#         widgets={
#             'author':forms.TextInput(attrs={'class':'textinputclass'}),
#             'comment_msg':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
#         } 
