from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import GameForm, ResourceForm, TopicForm


def navigation(active):    
    def decorator(view):
        def wrapper(request, *args, **kwargs):            
            contact = Contact.objects.latest('id')
            navbar = [                
                {'active': '', 'href': "admingames", 'text': "O'yinlar"},
                {'active': '', 'href': "admintopic", 'text': 'Mavzular'},
                {'active': '', 'href': "adminfeedback", 'text': 'Tavsiyalar'}, 
                {'active': '', 'href': "adminprojectdescription", 'text': 'Loyiha tasviri'},   
                {'active': '', 'href': "adminresources", 'text': 'Resurslar'},
                {'active': '', 'href': "adminintro", 'text': 'Kirish qismi'}, 
                {'active': '', 'href': "admincontact", 'text': "Bog'lanish"},
            ]

            for elem in navbar:                
                if elem['href'] == active:
                    elem['active'] = 'active'            
            render_object = view(request, *args, **kwargs)
            if not isinstance(render_object, dict):
                return render_object
            if 'context' not in render_object.keys():
                render_object['context'] = {}
            render_object['context'].update({'navbar': navbar})
            render_object['context'].update({'contact': contact}) 
            return render(request, render_object['html'], render_object['context'])
        return wrapper    
    return decorator


@login_required(login_url='login')
@navigation('admingames')
def adminpannel(request):
    if not request.user.is_staff:
        return redirect(login)
    return {'html': 'mainapp/admin.html'}

@login_required(login_url='login')
@navigation('admingames')
def admingames(request):
    search = request.GET.get('search')
    if search is None:
        games = Game.objects.all().order_by('-id')

    else:
        games = Game.objects.filter(name__icontains = search)
    return {'context': {'games': games}, 'html': 'mainapp/admingames.html'}

@login_required(login_url='login')
@navigation('admingames')
def admingame_detail(request, game_id):
    game = get_object_or_404(Game, id = game_id)

    if request.method == 'GET':
        topics = Topic.objects.all()
        return {'context': {'game': game, 'topics': topics}, 'html': 'mainapp/admingame_detail.html'}
    elif request.method == 'POST':
        # Get form data
        game.author = request.POST.get('author')
        game.desc = request.POST.get('desc')
        game.name = request.POST.get('name')
        game.topic_id = request.POST.get('topic')  # Using topic_id to set the foreign key
        game.lowage = request.POST.get('lowage')
        game.upage = request.POST.get('upage')
        # game.playernum = request.POST.get('playernum')
        # game.time = request.POST.get('time')
        game.lowplayernum = request.POST.get('lowplayernum')
        game.upplayernum = request.POST.get('upplayernum')
        game.lowtime = request.POST.get('lowtime')
        game.uptime = request.POST.get('uptime')
        #changed ^
        game.format = request.POST.get('format')
        game.rules = request.POST.get('rules')
        game.goal = request.POST.get('goal')
        game.target = request.POST.get('target')
        game.outcome = request.POST.get('outcome')
        game.content = request.POST.get('content')

        # Handle file uploads
        if 'pic' in request.FILES:
            game.pic = request.FILES['pic']
        if 'file' in request.FILES:
            game.file = request.FILES['file']

        # Save the game instance with updated data
        game.save()

        # Redirect to some other page after saving, e.g., game detail page
        return redirect('admingame_detail', game_id=game.id) 

@login_required(login_url='login')
@navigation('admintopic')
def admintopic(request):
    search = request.GET.get('search')
    if search is None:
        topic = Topic.objects.all().order_by('-id')
     
    else:
        topic = Topic.objects.filter(name__icontains = search)
    # return render(request, "mainapp/admintopic.html", {"topic": topic})
    return {'context': {'topic': topic}, 'html': 'mainapp/admintopic.html'}


@login_required(login_url='login')
@navigation('adminfeedback')
def adminfeedback(request):
    search = request.GET.get('search')
    if search is None:
        feedback = Feedback.objects.all().order_by('-id')
    else:
        feedback = Feedback.objects.filter(email__icontains = search)
    # return render(request, "mainapp/adminfeedback.html", {"feedback": feedback})
    return {'context': {'feedback': feedback}, 'html': 'mainapp/adminfeedback.html'}


@login_required(login_url='login')
@navigation('admincontact')
def admincontact(request):
    contact = Contact.objects.latest('id')
    return {'context': {'contact': contact}, 'html': 'mainapp/admincontact.html'}

# @login_required(login_url='login')
# @navigation('projectdescription')
# def adminprojectdescription(request):
#     projectdescription =  ProjectDescription.objects.latest('id')
#     return {'context': {'projectdescription': projectdescription}, 'html': 'mainapp/projectdescription.html'}

@login_required(login_url='login')
@navigation('adminresources')
def adminresources(request):
    search = request.GET.get('search')
    if search is None:
        resources = AdditionalResources.objects.all().order_by('-id')
    else:
        resources = AdditionalResources.objects.filter(title__icontains = search)
    return {'context': {'resources': resources}, 'html': 'mainapp/adminresources.html'}

@login_required(login_url='login')
@navigation('adminresources')
def adminresource_detail(request, resource_id):
    resource = get_object_or_404(AdditionalResources, id = resource_id)

    if request.method == 'GET':
        return {'context': {'resource': resource}, 'html': 'mainapp/adminresource_detail.html'}
    elif request.method == 'POST':
        # Get form data
        resource.desc = request.POST.get('desc')
        resource.title = request.POST.get('title')
       
        if 'file' in request.FILES:
            resource.file = request.FILES['file']

        # Save the game instance with updated data
        resource.save()

        # Redirect to some other page after saving, e.g., game detail page
        return redirect('adminresources') 



@login_required(login_url='login')
def delete_game(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Game, id = game_id)
        game.delete()
        return redirect('admingames')

@login_required(login_url='login')
def delete_resource(request, resource_id):
    if request.method == 'POST':
        resource = get_object_or_404(AdditionalResources, id = resource_id)
        resource.delete()
        return redirect('adminresources')

#----------------------------------------------------   
# Is not working
@login_required(login_url='login')
@navigation('add_game')
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admingames')  # Redirect to the page where all games are listed
    else:
        form = GameForm()

    # return render(request, 'mainapp/add_game.html', {'form': form})
    return {'context': {'form': form}, 'html': 'mainapp/add_game.html'}


@login_required(login_url='login')
@navigation('add_type')
def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admintopic')  # Redirect to the page where all games are listed
    else:
        form = TopicForm()

    # return render(request, 'mainapp/add_game.html', {'form': form})
    return {'context': {'form': form}, 'html': 'mainapp/add_topic.html'}


@login_required(login_url='login')
def delete_topic(request, topic_id):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, id = topic_id)
        topic.delete()
        return redirect('admintopic')


@login_required(login_url='login')
@navigation('add_resource')
def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminresources')  # Redirect to the page where all games are listed
    else:
        form = ResourceForm()

    # return render(request, 'mainapp/add_game.html', {'form': form})
    return {'context': {'form': form}, 'html': 'mainapp/add_resource.html'}

@login_required(login_url='login')
@navigation('admintopic_detail')
def admintopic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'GET':
        return {'context': {'topic': topic}, 'html': 'mainapp/admintopic_detail.html'}
    elif request.method == 'POST':
        # Get form data
        topic.name = request.POST.get('name')

        # Save the topic instance with updated data
        topic.save()

        # Redirect to the topic detail page after saving
        # return redirect('admintopic_detail', topic_id=topic.id)
        return redirect('admintopic')

    
@login_required(login_url='login')
@navigation('adminprojectdescription')
def adminprojectdescription(request):
    projectdescription =  ProjectDescription.objects.latest('id')
    if request.method == 'GET':
        return {'context': {'projectdescription': projectdescription}, 'html': 'mainapp/projectdescription.html'}
    elif request.method == 'POST':
        projectdescription.title = request.POST.get("title")
        projectdescription.content = request.POST.get('content')
        projectdescription.save()
        return redirect('admin')
    
@login_required(login_url='login')
@navigation('admincontact')
def admincontact(request):
    contact = Contact.objects.latest('id')
    if request.method == 'GET':
        return {'context': {'contact': contact}, 'html': 'mainapp/admincontact.html'}
    elif request.method == 'POST':
        contact.email = request.POST.get("email")
        contact.phone = request.POST.get('phone')
        contact.telegram = request.POST.get('telegram')
        contact.address = request.POST.get('address')
        contact.save()
        return redirect('admin')

@login_required(login_url='login')
@navigation('adminintro')
def adminintro(request):
    intro = MainIntro.objects.latest('id')
    if request.method == 'GET':
        return {'context': {'intro': intro}, 'html': 'mainapp/adminintro.html'}
    elif request.method == 'POST':
        intro.title = request.POST.get("title")
        intro.desc = request.POST.get("desc")
        if 'pic' in request.FILES:
            intro.img = request.FILES['pic']
        intro.save()
        return redirect('admin')





@navigation('')
def loginview(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('admin')
        return {'html': 'mainapp/login.html'}
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
@navigation('adminfeedback_detail')
def adminfeedback_detail(request, feedback_id):
    feedback = get_object_or_404(Feedback, id = feedback_id)
    if request.method == 'GET':
        return {'context': {'feedback': feedback}, 'html': 'mainapp/adminfeedback_detail.html'}