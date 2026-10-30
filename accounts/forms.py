from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',

                'class': 'w-full p-4 bg-gray-800 text-white rounded-xl border border-gray-600'
            }
        )
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password'
        ]

        widgets = {

            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Username',

                    'class': 'w-full p-4 bg-gray-800 text-white rounded-xl border border-gray-600'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter Email',

                    'class': 'w-full p-4 bg-gray-800 text-white rounded-xl border border-gray-600'
                }
            ),

        }

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'bio',
            'college',
            'github_link',
            'linkedin_link',
            'skills',
            'experience_level',
            'resume',
        ]

        widgets = {

            'bio': forms.Textarea(
                attrs={
                    'rows': 5,
                    'class': 'w-full p-4 bg-slate-900 border border-slate-700 rounded-xl text-white'
                }
            ),

            'college': forms.TextInput(
                attrs={
                    'class': 'w-full p-4 bg-slate-900 border border-slate-700 rounded-xl text-white'
                }
            ),

            'github_link': forms.URLInput(
                attrs={
                    'placeholder': 'https://github.com/username',
                    'class': 'w-full p-4 bg-slate-900 border border-slate-700 rounded-xl text-white'
                }
            ),

            'linkedin_link': forms.URLInput(
                attrs={
                    'placeholder': 'https://linkedin.com/in/username',
                    'class': 'w-full p-4 bg-slate-900 border border-slate-700 rounded-xl text-white'
                }
            ),

            'skills': forms.Textarea(
                attrs={
                    'rows': 3,
                    'class': 'w-full p-4 bg-slate-900 border border-slate-700 rounded-xl text-white'
                }
            ),

            'experience_level': forms.Select(
                attrs={
                    'class': 'w-full p-4 bg-slate-900 border border-slate-700 rounded-xl text-white'
                }
            ),

            'resume': forms.ClearableFileInput(
                attrs={
                    'class': 'w-full p-4 bg-slate-900 border border-slate-700 rounded-xl text-white'
                }
            ),
        }

        
class ForgotPasswordForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Username',

                'class': 'w-full p-4 bg-gray-800 text-white rounded-xl border border-gray-600'
            }
        )
    )

    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter New Password',

                'class': 'w-full p-4 bg-gray-800 text-white rounded-xl border border-gray-600'
            }
        )
    )