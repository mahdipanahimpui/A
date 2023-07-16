from django import forms
from .models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = '__all__' # all part of Todo model
        fields = ['title', 'created', 'body']
    

