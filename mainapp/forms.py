from django import forms
from .models import Game, Topic, AdditionalResources


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'author', 'desc', 'name', 'topic', 'lowage', 'upage',
            'lowplayernum', 'upplayernum', 'lowtime', 'uptime', 'format', 'rules', 'goal',
            'target', 'outcome', 'content', 'pic', 'file'
        ]

        # Optional: Add custom widgets, labels, or help texts
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'topic': forms.Select(attrs={'class': 'form-control'}),
            'lowage': forms.NumberInput(attrs={'class': 'form-control'}),
            'upage': forms.NumberInput(attrs={'class': 'form-control'}),
            'lowplayernum': forms.TextInput(attrs={'class': 'form-control'}),
            'upplayernum': forms.TextInput(attrs={'class': 'form-control'}),
            'lowtime': forms.NumberInput(attrs={'class': 'form-control'}),
            'uptime': forms.NumberInput(attrs={'class': 'form-control'}),
            'format': forms.Select(attrs={'class': 'form-control'}),
            'rules': forms.Textarea(attrs={'class': 'form-control'}),
            'goal': forms.Textarea(attrs={'class': 'form-control'}),
            'target': forms.Textarea(attrs={'class': 'form-control'}),
            'outcome': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'pic': forms.FileInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'author': 'Muallif',
            'desc': 'Tavsifi',
            'name': 'Nomi',
            'topic': 'Mavzu',
            'lowage': 'Yoshdan',
            'upage': 'Yoshgacha',
            'lowplayernum': 'Eng Kam Ishtirokchilar Soni',
            'upplayernum': "Eng Ko'p Ishtirokchilar Soni",
            'lowtime': 'Eng Kam davomiylik vaqti (daqiqa)',
            'uptime': "Eng Ko'p davomiylik vaqti (daqiqa)",
            'format': 'Format',
            'rules': 'Qoidasi',
            'goal': 'Maqsadi',
            'target': 'Vazifalari',
            'outcome': 'Kompetensiyalar',
            'content': 'Materiallar tarkibi',
            'pic': 'Surat',
            'file': 'Fayl',
        }

        help_texts = {
            'author': 'O\'yinning muallifini kiriting.',
            'desc': 'O\'yin haqida batafsil ta\'rif bering.',
            'name': 'O\'yin nomini kiriting.',
            'topic': 'O\'yinga tegishli mavzuni tanlang.',
            'lowage': 'O\'yinchilar uchun minimal yoshni kiriting.',
            'upage': 'O\'yinchilar uchun maksimal yoshni kiriting.',
            'lowplayernum': 'O\'yinda qatnashishi kerak bo\'lgan minimal o\'yinchilar sonini kiriting.',
            'upplayernum': 'O\'yinda qatnashishi mumkin bo\'lgan maksimal o\'yinchilar sonini kiriting.',
            'lowtime': 'O\'yinni tugatish uchun zarur bo\'lgan minimal vaqtni kiriting (daqiqalarda).',
            'uptime': 'O\'yinni tugatish uchun zarur bo\'lgan maksimal vaqtni kiriting (daqiqalarda).',
            'format': 'O\'yin formatini tanlang.',
            'rules': 'O\'yin qoidalarini kiriting.',
            'goal': 'O\'yinning maqsadini yozing.',
            'target': 'O\'yin uchun mo\'ljallangan vazifalarni belgilang.',
            'outcome': 'O\'yinning kutilayotgan kompetensiyalarni tasvirlang.',
            'content': 'Materiallar tarkibini tasvirlab bering.',
            'pic': 'O\'yin uchun rasm yuklang.',
            'file': 'O\'yinga tegishli qo\'shimcha fayllarni yuklang.',
        }



class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Mavzu Nomi',
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = AdditionalResources
        fields = [
            'title', 'desc', 'file'
        ]
