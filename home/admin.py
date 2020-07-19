from django.contrib import admin

from . import models


myModels = [ models.UserProfile, models.Like,models.Ignore]  
admin.site.register(myModels)

