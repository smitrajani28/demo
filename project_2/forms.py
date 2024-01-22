from django import forms

class userform(forms.Form):
    value1=forms.CharField(label="name",required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    value2=forms.EmailField(label="email")

class calc1(forms.Form):
    CHOICES= [
    ('+', '+'),
    ('-', '-'),
    ('*', '*'),
    ('/', '/'),
    ]
    dropdown1=forms.CharField(label="operation", widget=forms.Select(choices=CHOICES))
    value1=forms.CharField(label="value_1")
    value2=forms.CharField(label="value_2")

class subjectform(forms.Form):
    sub1=forms.CharField(label="math", required=False)
    sub2=forms.CharField(label="chemistry", required=False)
    sub3=forms.CharField(label="physics", required=False)