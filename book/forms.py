from django import forms

from book.models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'birthday', 'country','email','photo','biography']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Muallifning to\'liq nomini kiriting'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Tug\'ilgan sanani tanlang'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Davlatni kiriting (masalan: O\'zbekiston)'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'user@gmail.com'
            })
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'description', 'price', 'image','file',]
        widgets = {
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kitob nomini kiriting'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Kitob haqida qisqacha ma\'lumot yozing',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control form-control-sm',  # form-control-sm kichik o'lcham uchun
                'accept': 'image/*'  # faqat rasm fayllarni qabul qilish
            }),
        }
        labels = {
            'author': 'Muallif',
            'title': 'Kitob nomi',
            'description': 'Tavsif',
            'price': 'Narxi',
            'is_published': 'Nashr etilganmi?'
        }