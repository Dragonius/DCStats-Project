from turtle import title
from django.contrib import admin

from .models import Aircraft, Mission, Pilot, Rank, Stats, UserProfile


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_filter = ("in_process", "date")
title_str = "21st VAWC Admin"
admin.site.site_header = title_str
admin.site.site_title = title_str
admin.site.index_title = "Welcome to the " + title_str
admin.site.register(Pilot)
admin.site.register(Rank)
admin.site.register(Aircraft)
admin.site.register(Stats)
# admin.site.register(Mission)
admin.site.register(UserProfile)
