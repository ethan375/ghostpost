from django import forms 


class NewPost(forms.Form):
    boast = forms.CheckboxInput()
    post = forms.CharField(widget=forms.Textarea(max_length=280))
