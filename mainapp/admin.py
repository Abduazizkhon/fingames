from django.contrib import admin
from .models import Game, Topic, Type, AdditionalResources, ProjectDescription, MainIntro, Contact

admin.site.register(Game)  
admin.site.register(Topic)
admin.site.register(Type)
admin.site.register(AdditionalResources)
admin.site.register(ProjectDescription)
admin.site.register(MainIntro)
admin.site.register(Contact)



