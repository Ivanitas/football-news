from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'thumbnail', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter news title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Enter news content'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'thumbnail': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image URL (optional)'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize category field choices
        self.fields['category'].choices = News.CATEGORY_CHOICES