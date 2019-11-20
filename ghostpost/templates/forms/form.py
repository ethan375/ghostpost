from django import forms 


class NewPost(forms.Form):
    boast = forms.BooleanField()
    post = forms.CharField(widget=forms.Textarea, max_length=280)
