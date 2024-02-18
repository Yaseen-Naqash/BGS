from django.contrib import admin
from .models import User,Deal,Boardgame,Topic

# Register your models here.

admin.site.register(User)
admin.site.register(Deal)
admin.site.register(Boardgame)
admin.site.register(Topic)



