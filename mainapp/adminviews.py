from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def admingames(request):
    search = request.GET.get('search')
    if search is None:
        games = Game.objects.all().order_by('-id')
        return render(request, 'mainapp/admingames.html', {'games': games})
    games = Game.objects.filter(name__icontains = search)
    return render(request, 'mainapp/admingames.html', {'games': games})

@login_required(login_url='login')
def admintopic(request):
    search = request.GET.get('search')
    if search is None:
        topic = Topic.objects.all().order_by('-id')
        return render(request, "mainapp/admintopic.html", {"topic": topic})
    topic = Topic.objects.filter(name__icontains = search)
    return render(request, "mainapp/admintopic.html", {"topic": topic})

@login_required(login_url='login')
def admintype(request):
    search = request.GET.get('search')
    if search is None:
        type = Type.objects.all().order_by('-id')
        return render(request, "mainapp/admintype.html", {"type": type})
    type = Type.objects.filter(name__icontains = search)
    return render(request, "mainapp/admintype.html", {"type": type})

@login_required(login_url='login')
def adminfeedback(request):
    search = request.GET.get('search')
    if search is None:
        feedback = Feedback.objects.all().order_by('-id')
        return render(request, "mainapp/adminfeedback.html", {"feedback": feedback})
    feedback = Feedback.objects.filter(email__icontains = search)
    return render(request, "mainapp/adminfeedback.html", {"feedback": feedback})

@login_required(login_url='login')
def admincontact(request):
    contact = Contact.objects.get(id=1)
    return render(request, "mainapp/admincontact.html", {"contact": contact})

@login_required(login_url='login')
def adminprojectdescription(request):
    projectdescription = ProjectDescription.objects.get(id = 1)
    return render(request, "mainapp/projectdescription.html", {"projectdescription": projectdescription})

@login_required(login_url='login')
def adminresources(request):
    search = request.GET.get('search')
    if search is None:
        resources = AdditionalResources.objects.all().order_by('-id')
        return render(request, 'mainapp/adminresources.html', {'resources': resources})
    resources = AdditionalResources.objects.filter(title__icontains = search)
    return render(request, 'mainapp/adminresources.html', {'resources': resources})

@login_required(login_url='login')
def adminintro(request):
    intro = get_object_or_404(MainIntro,id = 1)
    return render(request, "mainapp/adminintro.html", {"intro": intro})

