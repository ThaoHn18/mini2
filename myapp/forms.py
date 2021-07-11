# from django.db.models import fields
from django.forms import ModelForm,widgets
from django import forms
from django.core.exceptions import ValidationError
from .models import Book,Author

class AuthorForm(ModelForm):
    class Meta:
        model= Author
        fields = "__all__"
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        
    def clean_email(self): # validation cho thuộc tính của author
        input_email = self.cleaned_data['email']
        try:
            Author.objects.get(email=input_email) # Lấy report theo email
        except Author.DoesNotExist:
            return input_email
        raise ValidationError(f"{input_email} đã tồn tại. Mời bạn nhập mail khác")

class Bookform(ModelForm):
    class Meta:
        model= Book
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'pub_date':forms.DateInput(attrs={'class':'form-control','type' : 'date'}),
            'author':forms.Select(attrs={'class':'form-control'}),
        }