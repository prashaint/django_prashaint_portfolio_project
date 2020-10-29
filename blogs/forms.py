from django import forms
from .models import BlogPost, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'author', 'category', 'content', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            #'updated_on': forms.TextInput(attrs={'class':'form-control'}),
            #'content': forms.Textarea(attrs={'class':'form-control'}),
            #'created_on': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.TextInput(attrs={'class':'form-control'}),
        }
        
