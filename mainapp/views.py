from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def game_list(request):
    search = request.GET.get('search')
    contact = Contact.objects.latest('id') 
    navbar = [
        {'active': '', 'href': "main", 'text': 'Home'},
        {'active': 'active', 'href': "game_list", 'text': 'Games'},
        {'active': '', 'href': "resources", 'text': 'Resources'},
        {'active': '', 'href': "about", 'text': 'About'},
    ]
    if search is None:
        games = Game.objects.all().order_by('-id')
        return render(request, 'mainapp/games.html', {'games': games, 'contact': contact, 'navbar': navbar})
    games = Game.objects.filter(name__icontains = search)
    return render(request, 'mainapp/games.html', {'games': games, 'contact': contact, 'navbar': navbar})


def game_detail(request, game_id):
    game = get_object_or_404(Game, id = game_id)
    return render(request, 'mainapp/game_detail.html', {'game': game})

def resources(request):
    search = request.GET.get('search')
    if search is None:
        resources = AdditionalResources.objects.all().order_by('-id')
        return render(request, 'mainapp/resources.html', {'resources': resources})
    resources = AdditionalResources.objects.filter(title__icontains = search)
    return render(request, 'mainapp/resources.html', {'resources': resources})

def about(request):
    about = ProjectDescription.objects.latest('id')
    contact = Contact.objects.latest('id') 

    return render(request, 'mainapp/about.html', {'about': about, 'contact': contact})

def loginview(request):
    if request.method == 'GET':
        return render(request, 'mainapp/login.html')
    elif request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect(adminpannel)
        return redirect(login)
def logoutview(request):
    logout(request)
    return redirect('login') 

@login_required(login_url='login')
def adminpannel(request):
    if not request.user.is_staff:
        return redirect(login)
    return render(request, 'mainapp/admin.html')

    
    


def mainpage(request):
    games = Game.objects.all()
    resources = AdditionalResources.objects.all()
    main_intro = MainIntro.objects.get(id=1)
    contact = Contact.objects.latest('id')
    navbar = [
        {'active': 'active', 'href': "main", 'text': 'Home'},
        {'active': '', 'href': "game_list", 'text': 'Games'},
        {'active': '', 'href': "resources", 'text': 'Resources'},
        {'active': '', 'href': "about", 'text': 'About'},
    ]
    context = {
        'games': games, 
        'resources': resources, 
        'main_intro': main_intro, 
        'contact': contact,
        'navbar': navbar
        }
    return render(request, 'mainapp/main.html', context)





#pervesti html vo blocki,  sozdat main page, formi dlya feedbacka, poiskat pagi 

#templates I chose:
#https://templatemo.com/tm-557-grad-school
#https://codepen.io/caseycallis/pen/pwEWxo (paralax for game cards)
#https://www.free-css.com/free-css-templates/page283/webuild(realy free templates)
#https://www.free-css.com/free-css-templates/page258/venue(check)
#https://www.free-css.com/free-css-templates/page256/it-next
#https://www.free-css.com/free-css-templates/page256/soft-landing