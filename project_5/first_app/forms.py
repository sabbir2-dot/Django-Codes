from django import forms


# widgets == field to html input

class contactForm(forms.Form):
    name = forms.CharField(label="User Name ", help_text="total length shoukd be inside 40 words", widget=forms.Textarea)
    file = forms.FileField()
    email = forms.EmailField(label="Email ")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField()
    appointment = forms.DateTimeField()
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES)
    meal = [('p', 'peparroni'), ('m', 'mashroom')]
    pizza = forms.MultipleChoiceField(choices=meal)
