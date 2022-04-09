from django.contrib import admin

# Register your models here.
from .models import Details, UserProfile

admin.site.register(Details)
admin.site.register(UserProfile)