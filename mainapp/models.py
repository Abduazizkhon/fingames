from django.db import models



class Game(models.Model):
    author = models.CharField(max_length=255)
    desc = models.TextField()
    name = models.CharField(max_length=255, null = False, blank = False)
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    lowage = models.PositiveIntegerField()
    upage = models.PositiveIntegerField()
    # playernum = models.TextField()
    lowplayernum = models.PositiveIntegerField(default=0)
    upplayernum = models.PositiveIntegerField(default=0)
    # time = models.PositiveIntegerField()
    lowtime = models.PositiveIntegerField(default=0)
    uptime = models.PositiveIntegerField(default=0)
    format = models.CharField(max_length=255, null = False, blank = False, choices={
        'online': 'online',
        'offline': 'offline',
        'blended': 'blended'
    })
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    rules = models.TextField()
    goal = models.TextField()
    target = models.TextField()
    outcome = models.TextField()
    pic = models.ImageField()
    file = models.FileField()
    download_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False)
    def __str__(self):
        return self.name


class Feedback(models.Model):
    email = models.EmailField()
    text = models.TextField()
    type = models.CharField(max_length=255, null = False, blank = False, choices={
        'teacher': 'teacher',
        'student': 'student',
        'other': 'other'
    })
    def __str__(self):
        return f'Feedback from {self.email}'

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class ProjectDescription(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class AdditionalResources(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    file = models.FileField()

class MainIntro(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField()
    



    
    
