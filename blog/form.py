from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent', 'placeholder':"Type something"}),
        } 

class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author','comment_msg')

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'comment_msg':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
        