from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            'title',
            'description',
            'tech_stack',
            'team_size',
            'role_needed',
            'experience_level',
            'project_status',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter project title',
                    'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-purple-500'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': 'Describe your project...',
                    'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-purple-500'
                }
            ),

            'tech_stack': forms.TextInput(
                attrs={
                    'placeholder': 'React, Django, MongoDB',
                    'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-purple-500'
                }
            ),

            'team_size': forms.NumberInput(
                attrs={
                    'placeholder': '4',
                    'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-purple-500'
                }
            ),

            'role_needed': forms.TextInput(
                attrs={
                    'placeholder': 'Frontend Developer',
                    'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-purple-500'
                }
            ),

            'experience_level': forms.Select(
                attrs={
                    'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-purple-500'
                }
            ),

            'project_status': forms.Select(
                attrs={
                    'class': 'w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-purple-500'
                }
            ),

        }