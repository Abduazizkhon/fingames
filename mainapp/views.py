from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from telebot import TeleBot
import os


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
    used_filters = False
    search = request.GET.get('search')
    type_game = request.GET.get('type')
    topic_game = request.GET.get('topic')
    time = request.GET.get('time')
    age = request.GET.get('age')
    playernum = request.GET.get('playernum')
    filtered_games = []
    topics = Topic.objects.all()
    filters = {
        'search': search if search else '',
        'type_game': int(type_game) if type_game else '0',
        'topic_game': int(topic_game) if topic_game else '0',
        'time': int(time) if time else '',
        'age': int(age) if age else '',
        'playernum': int(playernum) if playernum else '',
    }

    if search is None:
        games = Game.objects.all().order_by('-id')
    else:
        name = Game.objects.filter(name__icontains=search)
        author = Game.objects.filter(author__icontains=search)
        games = name | author

    # if time != '' and time is not None:
    #     games = games.filter(time=time)
    #     used_filters = True

    # if playernum != '' and playernum is not None:
    #     games = games.filter(playernum=playernum)
    #     used_filters = True

    # they are replaced with conditions below

    if topic_game != '0' and topic_game is not None:
        topic_obj = Topic.objects.get(id=topic_game)
        games = games.filter(topic=topic_obj)
        used_filters = True

    if age != '' and age is not None:
        age = int(age)
        for game in games:
            if game.lowage <= age <= game.upage:
                filtered_games.append(game)
        used_filters = True
        return {'context': {'games': filtered_games,
                            'topics': topics,
                            'filters': filters,
                            'used_filters': used_filters, }, 'html': 'mainapp/games.html'}
    
    if time != '' and time is not None:
        time = int(time)
        for game in games:
            if game.lowtime <= time <= game.uptime:
                filtered_games.append(game)
        used_filters = True
        return {'context': {'games': filtered_games,
                            'topics': topics,
                            'filters': filters,
                            'used_filters': used_filters, }, 'html': 'mainapp/games.html'}
    
    if playernum != '' and playernum is not None:
        playernum = int(playernum)
        for game in games:
            if game.lowplayernum <= playernum <= game.upplayernum:
                filtered_games.append(game)
        used_filters = True
        return {'context': {'games': filtered_games,
                            'topics': topics,
                            'filters': filters,
                            'used_filters': used_filters, }, 'html': 'mainapp/games.html'}

    return {'context': {'games': games,
                        'topics': topics,
                        'filters': filters,
                        'used_filters': used_filters, }, 'html': 'mainapp/games.html'}


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    contact = Contact.objects.latest('id')

    return render(request, 'mainapp/game_detail.html', {'game': game, 'contact': contact})


def download_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    game.download_count += 1
    game.save()

    file_path = game.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read())
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response


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
    resources = AdditionalResources.objects.filter(title__icontains=search)
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
        feedback = Feedback(email=email, text=content, type=status)
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

# pervesti html vo blocki,  sozdat main page, formi dlya feedbacka, poiskat pagi

# templates I chose:
# https://templatemo.com/tm-557-grad-school
# https://codepen.io/caseycallis/pen/pwEWxo (paralax for game cards)
# https://www.free-css.com/free-css-templates/page283/webuild(realy free templates)
# https://www.free-css.com/free-css-templates/page258/venue(check)
# https://www.free-css.com/free-css-templates/page256/it-next
# https://www.free-css.com/free-css-templates/page256/soft-landing
