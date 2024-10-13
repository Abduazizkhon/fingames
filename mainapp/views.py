from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from telebot import TeleBot


def navigation(active):    
    def decorator(view):
        def wrapper(request):            
            contact = Contact.objects.latest('id')
            navbar = [                
                {'active': '', 'href': "main", 'text': 'Home'},
                {'active': '', 'href': "game_list", 'text': 'Games'},                
                {'active': '', 'href': "resources", 'text': 'Resources'},
                {'active': '', 'href': "about", 'text': 'About'},            
            ]
            for elem in navbar:                
                if elem['href'] == active:
                    elem['active'] = 'active'            
            render_object = view(request)
            if not isinstance(render_object, dict):
                return render_object
            if 'context' not in render_object.keys():
                render_object['context'] = {}
            render_object['context'].update({'navbar': navbar})
            render_object['context'].update({'contact': contact})            
            return render(request, render_object['html'], render_object['context'])
        return wrapper    
    return decorator

@navigation('game_list')
def game_list(request):
    search = request.GET.get('search')    
    if search is None:        
        games = Game.objects.all().order_by('-id')
    else:        
        games = Game.objects.filter(name__icontains=search)
    return {'context': {'games': games}, 'html': 'mainapp/games.html'}


def game_detail(request, game_id):
    game = get_object_or_404(Game, id = game_id)
    contact = Contact.objects.latest('id') 

    return render(request, 'mainapp/game_detail.html', {'game': game, 'contact': contact})

def resources(request):
    search = request.GET.get('search')
    contact = Contact.objects.latest('id') 

    navbar = [
        {'active': '', 'href': "main", 'text': 'Home'},
        {'active': '', 'href': "game_list", 'text': 'Games'},
        {'active': 'active', 'href': "resources", 'text': 'Resources'},
        {'active': '', 'href': "about", 'text': 'About'},
    ]
    if search is None:
        resources = AdditionalResources.objects.all().order_by('-id')
        return render(request, 'mainapp/resources.html', {'resources': resources, 'contact': contact, 'navbar': navbar})
    resources = AdditionalResources.objects.filter(title__icontains = search)
    return render(request, 'mainapp/resources.html', {'resources': resources, 'contact': contact, 'navbar': navbar})

def about(request):
    about = ProjectDescription.objects.latest('id')
    contact = Contact.objects.latest('id') 
    navbar = [
        {'active': '', 'href': "main", 'text': 'Home'},
        {'active': '', 'href': "game_list", 'text': 'Games'},
        {'active': '', 'href': "resources", 'text': 'Resources'},
        {'active': 'active', 'href': "about", 'text': 'About'},
    ]

    return render(request, 'mainapp/about.html', {'about': about, 'contact': contact, 'navbar': navbar})


def feedback(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        content = request.POST.get('content')
        status = request.POST.get('status')
        feedback = Feedback(email = email, text = content, type = status)
        feedback.save()
        bot = TeleBot("7359886263:AAFwxCySEDxrUL-EGyo6491fRIVEaaSYHGQ")
        bot.send_message("-1002232357914", f"Email:\n{email}\n\nContent:\n{content}\n\nStatus:\n{status}")
        return redirect('main')






    
    

@navigation('main')
def mainpage(request):
    games = Game.objects.all()
    resources = AdditionalResources.objects.all()
    main_intro = MainIntro.objects.latest('id')
    about = ProjectDescription.objects.latest('id')

    context = {
        'games': games, 
        'resources': resources, 
        'main_intro': main_intro,
        'about': about 
        }
    return {'context': context, 'html': 'mainapp/main.html'}





#pervesti html vo blocki,  sozdat main page, formi dlya feedbacka, poiskat pagi 

#templates I chose:
#https://templatemo.com/tm-557-grad-school
#https://codepen.io/caseycallis/pen/pwEWxo (paralax for game cards)
#https://www.free-css.com/free-css-templates/page283/webuild(realy free templates)
#https://www.free-css.com/free-css-templates/page258/venue(check)
#https://www.free-css.com/free-css-templates/page256/it-next
#https://www.free-css.com/free-css-templates/page256/soft-landing