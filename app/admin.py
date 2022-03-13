from django.contrib import admin
from .models import user_details
# Register your models here.
# @admin.register(user_details)
# class userform(admin.ModelAdmin):
#     list_display = 'all'

admin.site.register(user_details)