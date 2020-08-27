from django import forms
from .models import BlogComment




class BlogCommentForm(forms.ModelForm):
    """Форма комментарий"""
    class Meta:
        model = BlogComment
        fields = ['comment_text', 'parent']
        widgets = {
            'comment_text': forms.TextInput(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Ваш коментарий', 'id': False})
        }