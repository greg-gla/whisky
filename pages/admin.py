from django.contrib import admin
from pages.models import User,Distillery,Whisky,Rating

# Register your models here.
admin.site.register(User)
admin.site.register(Distillery)
admin.site.register(Whisky)
admin.site.register(Rating)