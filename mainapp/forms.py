from django import forms
from .models import Game, Type, Topic, AdditionalResources

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'author', 'desc', 'name', 'topic', 'lowage', 'upage',
            'playernum', 'time', 'format', 'type', 'rules', 'goal',
            'target', 'outcome', 'pic', 'file'
        ]

        # Optional: Add custom widgets, labels, or help texts
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'topic': forms.Select(attrs={'class': 'form-control'}),
            'lowage': forms.NumberInput(attrs={'class': 'form-control'}),
            'upage': forms.NumberInput(attrs={'class': 'form-control'}),
            'playernum': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.NumberInput(attrs={'class': 'form-control'}),
            'format': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'rules': forms.Textarea(attrs={'class': 'form-control'}),
            'goal': forms.Textarea(attrs={'class': 'form-control'}),
            'target': forms.Textarea(attrs={'class': 'form-control'}),
            'outcome': forms.Textarea(attrs={'class': 'form-control'}),
            'pic': forms.FileInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'author': 'Author',
            'desc': 'Description',
            'name': 'Name',
            'topic': 'Topic',
            'lowage': 'Minimum Age',
            'upage': 'Maximum Age',
            'playernum': 'Number of Players',
            'time': 'Time (minutes)',
            'format': 'Format',
            'type': 'Type',
            'rules': 'Rules',
            'goal': 'Goal',
            'target': 'Target',
            'outcome': 'Outcome',
            'pic': 'Picture',
            'file': 'File',
        }

        help_texts = {
            'author': 'Enter the author of the game.',
            'desc': 'Provide a detailed description of the game.',
            'name': 'Enter the name of the game.',
            'topic': 'Select the topic associated with the game.',
            'lowage': 'Enter the minimum age for players.',
            'upage': 'Enter the maximum age for players.',
            'playernum': 'Enter the number of players required for the game.',
            'time': 'Enter the time required to complete the game (in minutes).',
            'format': 'Select the format of the game.',
            'type': 'Select the type of game.',
            'rules': 'Provide the rules of the game.',
            'goal': 'State the goal of the game.',
            'target': 'Define the target audience for the game.',
            'outcome': 'Describe the expected outcome of the game.',
            'pic': 'Upload an image for the game.',
            'file': 'Upload any additional files related to the game.',
        }

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = [
            'name'
        ]

class ResourceForm(forms.ModelForm):
    class Meta:
        model = AdditionalResources
        fields = [
            'title', 'desc', 'file'
        ]
