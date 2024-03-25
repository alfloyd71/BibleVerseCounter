from django import forms

class BookChaptersVersesForm(forms.Form):
    bookname=forms.CharField(max_length=100, label='Book Name',widget=forms.TextInput(attrs={'id':'book-name','placeholder': 'Book Name'}))
    bookandchapter=forms.CharField(max_length=100, label='Book and Chapter',widget=forms.TextInput(attrs={'id':'book-and-chapter','placeholder': 'Book and Chapter'}))




