from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'short_description', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title tag'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter short description'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter body'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'short_description', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title tag'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter short description'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter body'}),
        }