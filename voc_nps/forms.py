from django import forms
from django.contrib.auth.forms import UserCreationForm
Role_CHOICES = (
    ('', 'Choose...'),
    ("TeamMember", "Team Member"),
    ("Freelancer", "Freelancer"),
    ("Admin", "Admin"),
)
phone_CHOICES = (

    ("+91", "+91"),
    ("+88", "+88"),
    ("+92", "+92"),
)
class UserRegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    role=forms.ChoiceField(choices=Role_CHOICES,label="Your Designation")
    teamcode=forms.CharField(label='Team Code',widget=forms.TextInput(attrs={'placeholder': 'Team Code'}),required=False)
    email = forms.CharField(label='Eamil',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password','pattern':"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[#$@!%^&*_]).{8,}", 'title':"Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}),required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),required=False)
    phonecode=forms.ChoiceField(label="Code",choices=phone_CHOICES)
    #profile_image=forms.ImageField(label="")
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'Password','pattern':"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[#$@!%^&*_]).{8,}", 'title':"Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"}))
