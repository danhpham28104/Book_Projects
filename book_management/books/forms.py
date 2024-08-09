from django import forms
from .models import Book

# định nghĩa lớp Book Form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'genre', 'quantity', 'description']
