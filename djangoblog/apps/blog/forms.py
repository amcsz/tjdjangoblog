from django import forms


class CreateForm(forms.Form):
    title = forms.CharField(label="Title of Post", max_length=200)
    content = forms.CharField(widget=forms.Textarea)