from django.contrib import admin
from .models import User
from .models import Nation, Team, League, Schedule, Match


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbr_name', 'nation']
    fieldsets = [
        (r'基本信息', {'fields': ['name']}),
        (None, {'fields': ['abbr_name']}),
        (None, {'fields': ['nation']}),
    ]
    # inlines = [ChoiceInline]
    list_filter = ['nation']
    search_fields = ['name', 'abbr_name']


class LeagueAdmin(admin.ModelAdmin):
    list_display = ['name', 'season', 'nation']
    fieldsets = [
        (r'基本信息', {'fields': ['name']}),
        (None, {'fields': ['season']}),
        (None, {'fields': ['nation']}),
    ]
    list_filter = ['nation']
    search_fields = ['name']


# class MatchAdmin(admin.ModelAdmin):
#     list_display = ['home_team', 'home_score', 'away_score', 'away_team', 'match_date']
#     fieldsets = [
#         (r'基本信息', {'fields': ['home_team']}),
#         (None, {'fields': ['home_score']}),
#         (None, {'fields': ['away_score']}),
#         (None, {'fields': ['away_team']}),
#         (None, {'fields': ['match_date']}),
#     ]
#     list_filter = ['match_date']
#     search_fields = ['home_team', 'away_team']


class MatchInline(admin.TabularInline):
    model = Match


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['league', 'name', 'start_date', 'end_date']
    fieldsets = [
        (None, {'fields': ['league']}),
        (r'基本信息', {'fields': ['name']}),
        (None, {'fields': ['start_date']}),
        (None, {'fields': ['end_date']}),
    ]
    inlines = [MatchInline]
    list_filter = ['league']
    search_fields = ['name']


admin.site.register(Nation)
admin.site.register(Team, TeamAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(User)
