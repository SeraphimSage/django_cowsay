from django import forms


class Cowsay_Form(forms.Form):
    text_input = forms.CharField(max_length=120)
