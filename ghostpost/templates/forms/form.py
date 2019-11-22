from django import forms


class NewPost(forms.Form):
    boast = forms.CharField(widget=forms.CheckboxInput, required=False)
    post = forms.CharField(widget=forms.Textarea, max_length=280)
